# python program to multiply all the numbers in a listA
list1=[8,2,3,-1,7]
def multiply(list1):
    total=1
    i=0
    while i<len(list1):
        total*=list1[i]
        i+=1
    return total
print("The product of the elements present inside a list is", multiply(list1))

#python program to reverse a string
string="1234abcd"
def reverse_string(string):
    reverse_string=""
    a=len(string)-1
    while a>=0:
        reverse_string+=string[a]
        a-=1
    return reverse_string
print(reverse_string(string))
