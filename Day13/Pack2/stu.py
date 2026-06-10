class Student():
    def __init__(self, sid, sname, sgrade):
        self.sid = sid
        self.sname = sname
        self.sgrade = sgrade

    def displaystu(self):
        print("stuid:{},stuName:{}, stuGrade:{}".format(self.sid, self.sname, self.sgrade))