# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# print(matrix,'\n')

# transpose=[[0,0,0],[0,0,0],[0,0,0]]
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         transpose[i][j]=matrix[j][i]

# print(transpose)
def hello_func():     #make our code more concise
    return 'hello om.'
print(hello_func().upper())

#using function help us to keep our code DRY(Don't Repeat Yourself)
#x='global x'
def test(z):
    #global x
    x= 'local x'
    print(z)

test('local z')

# print(dir(__builtins__))

def hello(greeting, name=input("Enter your name: ")):
    return "{}, {}".format(greeting,name)

print(hello("hello"))

#positional keyword
def student_info(*subject, **names):
    print(subject)
    print(names)
courses=('Math', 'Art')
info={'name': 'Rahul', 'age': 19}

student_info(*courses, **info)


