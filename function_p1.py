# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# print(matrix,'\n')

# transpose=[[0,0,0],[0,0,0],[0,0,0]]
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         transpose[i][j]=matrix[j][i]

# print(transpose)
def hello_func():     #make our code more concise
    return 'hello om.'
print(len('Test'))

#using function help us to keep our code DRY(Don't Repeat Yourself)
#x='global x'
def test(z):
    #global x
    x= 'local x'
    print(z)

test('local z')

# print(dir(__builtins__))


