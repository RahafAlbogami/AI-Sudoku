# MAIN DRIVER PROBLEM TO SOLVE AN INPUT SUDOKU PUZZLE


import sys 					#For getting the values from command line 
import time 
from CSP import csp
from Backtrack import *
from AC3 import *			#Uncomment this if you want to test AC3
from MRVDH6 import *


#THE MAIN FUNCTION GOES HERE
if __name__ == "__main__":
    '''
    The function takes arguments from commandline
    Argument 1 - Python file name 
    Argument 2 - Input String Showing the Sudoku 
    '''
    #if len(sys.argv)==2:
    grid = input("Enter the numbers of Sudoku (0 indicate a blank sqaure):\n")#"003020600900305001001806400008102900700000008006708200002609500800203009005010300"
    #sys.argv[1]
    choice = input("Choose the algorithm to solve thE Sudoku:  1 - Backtracking  2 - Backtraking with MRV&DH  3- AC-3 \n")
    assert len(grid) == 81
    start = time.time()
    sudoku = csp(grid=grid)
    if (choice == "1"):
        solved = Backtracking_Search(sudoku)
    elif(choice == "2"):
        solved = BacktrackingMRVDH_Search(sudoku)
    elif(choice == "3"):
        solved = AC3(sudoku)
    else:
        print("wrong choice")
        sys.exit()


    
    
    if solved!="FAILURE":
        if (choice == "1" or choice == "2" ):
            display(solved) 		#Displays the solved puzzle in the sudoku format
            print ("\n")
            
        print ("This puzzle was solved in: ", time.time()-start," seconds")
        print ("Perfectly solved")
    else:
        print ("Not solved")

    '''	
    if isComplete(sudoku) and solved:
            display(solved) 		#Displays the solved puzzle in the sudoku format
            print ("This puzzle was solved in: ", time.time()-start," seconds")
            print ("Perfectly solved")
    else:
            print ("Not solved")

    '''
    #else:
     #   print ("INVALID NUMBER OF INPUTS") 
