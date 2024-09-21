from typing import *

class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        curr_sum = 0
        max_reward = float('-inf')
        
        for reward in rewardValues:
            if curr_sum < reward:
                curr_sum += reward
            max_reward = max(curr_sum, max_reward)
            if curr_sum < 0:
                curr_sum = 0
        
        return max_reward

sol = Solution()
rewardValues = [1,1,3,3]