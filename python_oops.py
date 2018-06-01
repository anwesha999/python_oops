# check if an employee has achieved his weekly target or not
class employee:
    name = "Ben"
    designation = "Sales Executive"
    salesMadeThisWeek = 6
    def hasAchievedTarget(self):
        if self.salesMadeThisWeek >= 5:
                    print("target has been achieved")
        else: 
                    print("target has not been achieved")
employeeOne = employee()
employeeOne.name
employeeOne.hasAchievedTarget()
employeeTwo = employee()
employeeTwo.name
