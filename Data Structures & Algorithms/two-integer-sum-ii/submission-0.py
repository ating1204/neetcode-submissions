class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers) - 1

        sum = numbers[l] + numbers[r]
        
        while sum != target:
            
            if target > sum:

                l += 1

            else:
                r -= 1

            sum = numbers[l] + numbers[r]
            
        return [l+1,r+1]

        