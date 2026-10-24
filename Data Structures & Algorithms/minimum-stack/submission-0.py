class MinStack:
    ''' if i had 3 4 2 1 1 5 min would be [3, 2, 1, 1] but if i popped 5, 1, then min still 1 right? to check if we need to pop the min stack we gotta see if its eqqual to curr min so we should make it <='''
    def __init__(self):
        self.s = []
        self.min = []

    def push(self, val: int) -> None:
        if not self.s:
            self.min.append(val)
        elif val <= self.min[-1]:
            self.min.append(val)
        self.s.append(val)


    def pop(self) -> None:
        x = self.s.pop()
        if x == self.min[-1]:
            self.min.pop()
        


    def top(self) -> int:
        return self.s[-1]
        

    def getMin(self) -> int:
        return self.min[-1]

        
