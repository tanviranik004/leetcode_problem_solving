class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        newSalary=[]

        for i in range(1, len(salary)-1):
            newSalary.append(salary[i])
        return sum(newSalary)/len(newSalary)