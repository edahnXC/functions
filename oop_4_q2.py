class Interest():
    def __init__(self,principal,rate,time):
        self.principal=principal
        self.rate=rate
        self.time=time

    def Simple_Interest(self):
        return self.principal*self.rate/100*self.time

    def Compound_Interest(self):
        return self.principal*(1+self.rate/100)**self.time-self.principal

IN=Interest(4000,7,2)
print("Simple interest=",IN.Simple_Interest())
print("Compound Interest=",IN.Compound_Interest())