class Employee:
    def __init__(self, EmpId, EmpName, EmpSal):
        self.EmpId = EmpId
        self.EmpName = EmpName
        self.EmpSal = EmpSal

    def setEmpId(self, EmpId):
        self.EmpId = EmpId

    def setEmpName(self, EmpName):
        self.EmpId = EmpName

    def setEmpSal(self, EmpSal):
        self.Empsal = EmpSal

    def getEmpSal(self):
        print(
            f"Salary of Emp#{self.EmpId} Emp name{self.EmpName} is {self.EmpSal}")
