class Employee:
    def setnumberofworkinghours(self):
        self.numberofworkinghours = 40
    def displaythenumberworkinghours(self):
        print(self.numberofworkinghours)
 class trainee(Employee):
    def setnumberofworkinghours(self):
        self.numberofworkinghours = 45
    def resetnumberofworkinghours(self):
        super().setnumberofworkinghours()
employee = Employee()
employee.setnumberofworkinghours()
print("number of working hours of the employee:",end='')
employee.displaythenumberworkinghours()

trainee = trainee()
trainee.setnumberofworkinghours()
print("number of workinghours of the trainee:",end='')
trainee.displaythenumberworkinghours()
trainee.resetnumberofworkinghours()
print("number of working hours has been reset:",end='')
trainee.displaythenumberworkinghours()