'''
Created on 28 Sep 2015

@author: tobydobbs
'''

#===============================================================================
# Find k such that matrix[k][k] can be anything but row k must be exclusively 0 and column k must be exclusively 1
#===============================================================================
def findKK(matrix):
    res = False # initialize with assumption that the row satisfies the condition
    kk = -1
    n = len(matrix)
    for i in range(n): # iterate through the rows
        print matrix[i]
        for j in range(n): # iterate through the column entries of each row
            print "row: " + str(i) + ", column: " + str(j) + ", value: " + str(matrix[i][j])
            if matrix[i][j] == 0 or i == j: # skip over matrix[k][k]
                res = True
            else:
                res = False
                break
        if res == True:
            for k in range(n): # iterate through all rows of index i
                print "row: " + str(k) + ", column: " + str(i) + ", value: " + str(matrix[k][i])
                if matrix[k][i] == 1 or i == k:
                    res = True
                else:
                    res = False
                    break
        if res == True:
            kk = i 
            break
    return "K is " + str(kk) 
    
def main():
    print "In the main method:\n"
    matrix = [
        [1,0,0,1,1],
        [1,0,1,1,0],
        [1,0,1,1,1],
        [0,0,0,0,0],
        [0,0,0,1,1],
    ]
    print findKK(matrix) 

if __name__ == "__main__":
    main()
