class MyCalendar:
    '''
    calendar = [[1,4],, [5, 7], etc]
    end time = endTime - 1
    '''

    def __init__(self):
        self.calendar = []
    def book(self, startTime: int, endTime: int) -> bool:
        for s, e in self.calendar:
            if (s <= startTime < e) or (s < endTime <= e) or (s >= startTime and e < endTime) :
                return False
        self.calendar.append([startTime, endTime])
        return True

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)