class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sd={0:1}
        c=0
        s=0
        n=len(nums)
        for num in nums:
            s+=num
            if s-k in sd:
                c+=sd[s-k]
            if s in sd:
                sd[s]+=1
            else:
                sd[s]=1
        return c
        
