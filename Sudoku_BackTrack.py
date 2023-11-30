#default sudoku
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(bo):
    #to add horizontal lines just after the third elements of a list
    for i in range(len(bo)):
        if (i%3==0 and i!=0):
            print("-"*20)
    #lines to seperate each 3rd element of a list element...
        for j in range(len(bo[i])):
            if (j%3==0 and j!=0):
                print("|",end="")
            if j==8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def find_empty(bo): #finds the empty boxes and returns the row,col position of that  box
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if (bo[i][j]==0):
                return (i,j)
    return None

def valid(bo,num,pos): #bo=board,num=number(1-9),pos(empty spaces)
    
    #check row
    for i in range(len(bo[0])):      #checks specific row's all element (given by find_empty )
        if bo[pos[0]][i]==num and pos[1]!=i:
            return False
        
    #check column
    for j in range(len(bo)):         #checks specific column's all element (given by find_empty)
        if bo[j][pos[1]]==num and pos[0]!=j:
            return False
        
    #check box              #check's specific box's all element (given by find_empty)
    box_x=pos[1]//3
    box_y=pos[0]//3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    return True


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True 
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0
    return False

print_board(board)
solve(board)
print("___________Final Sudoku___________")
print_board(board)