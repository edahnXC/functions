#python program to find maximum of three numbers
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the thrd number: "))

def max_num(num1,num2,num3):
    return max(num1,num2,num3)
print("The maximum number among the three numbers is:",max_num(num1,num2,num3))

#python function to sum all the numbers in a list
list1=[8,2,3,0,7]
def sum(list1):
    total=0
    a=len(list1)
    i=0
    while i<a:
        total+=int(list1[i])
        i+=1
    return total
print("sum of the elements within the  list is",sum(list1))

