class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        s = []
        for i in range(len(position)):
            s.append([position[i], speed[i]])
        s.sort(key= lambda x: x[0], reverse = True) 
        
        times = []
        for pos, speed in s:
            times.append((target - pos) / speed)

            if len(times) >= 2 and times[-1] <= times[-2]:
                times.pop()

        return len(times)