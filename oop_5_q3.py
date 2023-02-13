import time
class Test:
    def __init__(self):
        print("List has been created")
     
    def __del__(self):
        print("List is deleted")

list1=[Test(),Test(),Test(),Test()]
print()
time.sleep(3)

list1=None