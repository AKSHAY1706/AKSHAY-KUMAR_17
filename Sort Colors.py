class Solution:
    def sortColors(self, nums: List[int]) -> None:
       
        d = {0:0,1:0,2:0}
        for i in nums:
            if i in d:
                d[i]+=1
        
        nums.clear()
        for i in d:
            while d[i]>0:
                nums.append(i)
                d[i]-=1
