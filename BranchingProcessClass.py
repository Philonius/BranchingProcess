class BranchingProcess:
    def __init__(self,FirstEvent):
        self.InitialEventList = [FirstEvent]
        self.Events = self.InitialEventList
        self.Generations = [BranchingProcessGeneration(self.InitialEventList)]

    def set_envir(self,Envir):
        self.Envir = Envir
    def set_proctype(self,ProcType):
        self.ProcType = ProcType

    def Simulate(self,*arg):
        if self.InitialEventList == []: 
            print "Error: Branching Process requires an initial ancestor."
        elif len(self.InitialEventList) == 1:
            iter = 0
            if arg[0] is None : # Or arg[0] is not a valid integer
                MAX_ITER = 10
                print "Simulating Branching Process: Maximum Generations initialised as ",MAX_ITER,"."
            else:
                MAX_ITER = arg[0]
            CurrentGeneration = BranchingProcessGeneration(self.InitialEventList)
            while iter < MAX_ITER:
                NextGeneration = CurrentGeneration.SimulateNextGeneration()
                if not NextGeneration.is_empty():
                    self.Events.extend(NextGeneration.Events)
                    CurrentGeneration = NextGeneration
                    self.Generations.extend([CurrentGeneration])
                    iter = iter+1
                else: break
            if iter == MAX_ITER:
                print "Process did not die out after ",MAX_ITER," generations."

class BranchingProcessGeneration:
    def __init__(self,
                 EventsList):
        self.Events = [e for e in EventsList if not e is None]

    def is_empty(self):
        return len(self.Events) == 0
        
    def SimulateNextGeneration(self,*arg):
        if not self.is_empty():
            new_events = []
            for e in self.Events:
                Oe = e.rOffspring()
                e.add_child(Oe)
                if not Oe is None:
                    new_events.extend(Oe)
            NextGeneration = BranchingProcessGeneration(new_events)
            return NextGeneration
