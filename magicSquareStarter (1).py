# Complete the 5 "TODO" functions to determine if a square is "magic"

def fillSquare(n, sqArr):
    '''
    This procedure prompts the user for n^2 inputs to populate a
    2D square array which has alreay been declared
    precondition:  sqArr has been declared with a size of nxn
    '''

    #note: I could have used len(sqArr) instead of passing n in as a parameter
    # but I thought it would be easier for you to understand if it was passed...
    for r in range(n):
        print("----ROW " + str(r + 1) + "----")
        for c in range(n):
            sqArr[r][c] = int(input("Enter value: "))
    

def printSquare(n, sqArr):
    '''
    This procedure "pretty" prints a 2D square array of size n
    '''
    for r in range(n):
        for c in range(n):
            print(sqArr[r][c], end="\t")
        print("\n")
    
def checkRow(n, sqArr, mNum):
    '''
    This procedure will return true if every row of sqArr has a sum of mNum
    It's left for you to do.
    '''

    count = 0
    for i in range (len(sqArr)):
        
        for j in range (len(sqArr[i])):
            count = count + sqArr[i][j]

        if count == mNum:
            return True
        else:
            return False

def checkCol(n, sqArr, mNum):

    '''
    This procedure will return true if every column of sqArr has a sum of mNum
    '''

    count = 0
    for i in range (len(sqArr)):
        
        for j in range (len(sqArr[i])):
            count = count + sqArr[j][i]

        if count == mNum:
            return True
        else:
            return False


def checkDiag1(n, sqArr, mNum):

    
    '''
    This procedure will return true if digaonal 1 of sqArr has a sum of mNum
    '''
    
    count = 0 
    for i in range (len(sqArr)):
        count = count + sqArr[i][i]

    if count == mNum:
        return True
    else:
        return False

def checkDiag2(n, sqArr, mNum):

    
    '''
    This procedure will return true if diagonal 2 of sqArr has a sum of mNum
    '''

    count = 0 
    for i in range (len(sqArr)):
        count = count + (sqArr[i][2-i])

    if count == mNum:
        return True
    else:
        return False 
    

def checkUnique(n, sqArr):

    
    '''
    This procedure will return true if every number in sqArr is unique. It goes through every number and checks it with an array of used numbers.
    '''

    usedNums = []

    for i in range (len(sqArr)):

        for j in range (len(sqArr[i])):

            for num in range (len(sqArr[i])):
                if sqArr[i][j] not in usedNums:
                    usedNums.append(sqArr[i][j])

                elif sqArr[i][j] in usedNums:
                    return False


    return True

def checkSquare(size, square):
    '''
    Returns True if inputed square is magic, and False if not.
    '''
    magicNum = s*(((s**2)+1)/2)  # You will need to calculate the magic number here 
    if(checkRow(size, square, magicNum) and  \
       checkCol(size, square, magicNum) and  \
       checkDiag1(size, square, magicNum) and  \
       checkDiag2(size, square, magicNum) and   \
       checkUnique(size, square)):
       return True
    else:
       return False

# ---MAIN---
s = int(input("Enter square side length:  "))
sq = [[0 for x in range(s)] for y in range(s)]
fillSquare(s, sq)




'''
if you get tired of typing in the square multiple times,
for testing purposes, you may want to comment out the 3 lines above and
uncomment the 2 lines below.  It will make your testing life *much* easier :)
'''
#s = 3
#sq = [[2,7,6], [9,5,1], [4,3,8]]

printSquare(s, sq)
print(checkSquare(s, sq))
   

