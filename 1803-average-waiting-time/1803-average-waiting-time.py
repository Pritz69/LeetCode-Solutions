class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        pt=customers[0][0]+customers[0][1]
        ans=pt-customers[0][0]
        for i in range(1,len(customers)) :
            pt=max(pt+customers[i][1], customers[i][0]+customers[i][1])
            ans += pt-customers[i][0]
        return ans/len(customers)