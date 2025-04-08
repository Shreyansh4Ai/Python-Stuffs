class csvtu:
    def __init__(self,utd1,utd2,utd3,utd4):
       self.utd1=utd1
       self.utd2=utd2
       self.utd3=utd3
       self.utd4=utd4

    def getutd1(self):
        print("NO. of students in utd1",self.utd1)

    def getutd2(self):
     print("NO. of students in utd2",self.utd2)   

    def getutd3(self):
     print("NO. of students in utd3",self.utd3)   
          
    def getutd4(self):
     print("NO. of students in utd4",self.utd4) 


c=csvtu(430,428,32,10)
c.getutd1()
c.getutd2()
c.getutd3()
c.getutd4()
     

