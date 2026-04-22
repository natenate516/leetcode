class Solution(object):
    def minCostClimbingStairs(self, cost):

        for i in range(2, len(cost)):
            minCost = float('inf')
            minCost = min(cost[i-1] + cost[i], cost[i-2] + cost[i])
            cost[i] = minCost

        return min(cost[len(cost) - 1], cost[len(cost) - 2])



        