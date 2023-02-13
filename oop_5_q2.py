#create one class Test contains constructor and destructor
import time
class Test:
    def __init__(self):
        print("This is a Constructor")
     
    def __del__(self):
        print("This is a Destructor")
    
T1=Test()
T2=Test()
T3=Test()
T4=Test()
time.sleep(4)

T1=None
T3=None
time.sleep(2)

T2=None
T3=None
