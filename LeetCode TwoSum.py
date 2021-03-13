class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        
        for i in range(len(nums)):
            dic[nums[i]] = []
        
        for i in range(len(nums)):
            dic[nums[i]].append(i)
            
        for key in dic.keys():
            answer = dic[key][0]
            
            if target-key in dic:
                x = dic[target-key].pop()
                
                if x != answer:
                    return [answer, x]
                else:
                    dic[target-key].append(x)
        