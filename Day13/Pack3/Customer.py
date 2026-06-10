
#Approach 1
# from Pack1.Emp import Employee
# from Pack2.stu import Student
#
# Eobj=Employee(101,"Dany", 1250000)
# Eobj.displayemp()
#
# Sobj=Student(201,"Ebi", 'A')
# Sobj.displaystu()

#Approach 2
import sys
sys.path.append("C:/Automation/PWpython/Day13/Pack1")

from Emp import Employee

Eobj=Employee(101,"Dany", 1250000)
Eobj.displayemp()


sys.path.append("C:/Automation/PWpython/Day13/Pack2")

from stu import Student

Sobj=Student(201,"Ebi", 'A')
Sobj.displaystu()

