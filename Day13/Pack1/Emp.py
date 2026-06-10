class Employee:
        def __init__(self,eid,ename,esal):
            self.eid = eid
            self.ename = ename
            self.esal = esal

        def displayemp(self):
            print("empid:{},empName:{}, empsal:{}".format(self.eid, self.ename, self.esal))


