class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #two binary searches, first one to identify what list to choose, second one to find elem in list

        l, r = 0, len(matrix) - 1
        
        
        while l <= r:
            m = (l+r) // 2 #list in list
            list = matrix[m]

            if target < list[0]:
                r = m - 1
            elif target > list[-1]:
                l = m + 1
            else: 
                l, r = 0, len(list) - 1
                
                while l <= r:
                    m = (l+r) // 2
                    if target < list[m]:
                        r = m - 1
                    elif target > list[m]:
                        l = m + 1
                    elif target == list[m]:
                        return True
                return False

        return False




