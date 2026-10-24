class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        '''
        maxH = max(height)
        maxInd = height.index(maxH) #retrieves first index of max height

        res = 0
        n = len(height)
        lStack = []
        rStack = []

        #find starting point for l
        l = 0
        while l < n-1 and height[l] <= height[l+1]:
            l += 1
        if l == n - 1:
            return 0
        r = n-1
        while r > 0 and height[r] <= height[r-1]:
            r -= 1
        if r == 0:
            return 0
        print(l, r)
        
        #some form of loop to get mono stack for l and r
        for i in range(l, maxInd + 1):
            if not lStack or lStack[-1][1] <= height[i]:
                lStack.append([i, height[i]])
        for i in range(r, maxInd, -1):
            if not rStack or rStack[-1][1] <= height[i]:
                rStack.append([i, height[i]])
        rStack.append([maxInd, maxH])

        #do left first
        q = len(lStack)
        for i in range(1, q):
            ind1, h1 = lStack[i][0], lStack[i][1]
            ind2, h2 = lStack[i-1][0], lStack[i-1][1]
            minH = min(h1, h2)
            res += (ind1 - ind2 - 1) * (minH) #0, 2
            #deal with blcoks in btwn
            res -= sum(height[ind2 + 1: ind1])


        #right side
        r = len(rStack)
        for i in range(1, r):
            ind1, h1 = rStack[i][0], rStack[i][1]
            ind2, h2 = rStack[i-1][0], rStack[i-1][1]
            minH = min(h1, h2)
            res += (ind2 - ind1 - 1) * (minH) 
            res -= sum(height[ind1 + 1: ind2])
        return res
            




            
        

        print(lStack)
        print(rStack)







