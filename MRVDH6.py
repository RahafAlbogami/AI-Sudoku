# IMPLEMENTATION OF BACKTRACKING SOLUTION FOR SUDOKU

from CSP import *
from copy import deepcopy

minemum_unassigned_variables = []

#BACKTRACKING SEARCH INITIALIZES THE INITIAL ASSIGNMENT AND CALLS THE BACKTRACK FUNCTION
def BacktrackingMRVDH_Search(csp):
	return Backtrack({}, csp)



#THE RECURSIVE FUNCTION WHICH ASSIGNS VALUE USING BACKTRACKING 
def Backtrack(assignment, csp):
	if isComplete(assignment):
		return assignment

	var = Select_Unassigned_Variables(assignment, csp)
	domain = deepcopy(csp.values)

	for value in csp.values[var]:
		if isConsistent(var, value, assignment, csp):
			assignment[var] = value
			inferences = {}
			inferences = Inference(assignment, inferences, csp, var, value)
			if inferences!= "FAILURE":
				result = Backtrack(assignment, csp)
				if result!="FAILURE":
					return result

			del assignment[var]
			csp.values.update(domain)

	return "FAILURE"



#FORWARD CHECKING USING THE CONCEPT OF INFERENCES
def Inference(assignment, inferences, csp, var, value):
	inferences[var] = value

	for neighbor in csp.peers[var]:
		if neighbor not in assignment and value in csp.values[neighbor]:
			if len(csp.values[neighbor])==1:
				return "FAILURE"

			remaining = csp.values[neighbor] = csp.values[neighbor].replace(value, "")

			if len(remaining)==1:
				flag = Inference(assignment, inferences, csp, neighbor, remaining)
				if flag=="FAILURE":
					return "FAILURE"

	return inferences

			
#CHECKS IF THE ASSIGNMENT IS COMPLETE
def isComplete(assignment):
	return set(assignment.keys())==set(squares)



def Select_Unassigned_Variables(assignment, csp):
        minemum = []
        largest_DH = -1
        d = []
        unassigned_variables = dict((squares, len(csp.values[squares])) for squares in csp.values if squares not in assignment.keys())
        mrv = int(min(unassigned_variables.values()))
        for key, num in unassigned_variables.items():
                if num == mrv:
                        minemum.append(key)

        for x in range(0,len(csp.constraints)):
                if csp.constraints[x][1] not in assignment.keys():
                        d.append(csp.constraints[x][0])

        for ra in minemum:
                counted = d.count(ra)
                if counted > largest_DH:
                        largest_DH = counted
                        nextVar = ra
                
                        

        #next_Variable = DegreeHeuristic(minemum_unassigned_variables)
        return nextVar#min(unassigned_variables, key=unassigned_variables.get)
        

#RETURNS THE STRING OF VALUES OF THE GIVEN VARIABLE 
def Order_Domain_Values(var, assignment, csp):
	return csp.values[var]



#CHECKS IF THE GIVEN NEW ASSIGNMENT IS CONSISTENT
def isConsistent(var, value, assignment, csp):
	for neighbor in csp.peers[var]:
		if neighbor in assignment.keys() and assignment[neighbor]==value:
			return False
	return True



#PERFORMS FORWARD-CHECKING
def forward_check(csp, assignment, var, value):
	csp.values[var] = value
	for neighbor in csp.peers[var]:
		csp.values[neighbor] = csp.values[neighbor].replace(value, '')



#DISPLAYS THE SOLVED SUDOKU IN THE GRID FORMAT
def display(values):
    for r in rows:
    	if r in 'DG':
    		print ("-------------------------------------------")
    	for c in cols:
    		if c in '47':
    			print (' | ', values[r+c], ' ',end=' ')
    		else:
    			print (values[r+c], ' ',end=' ')
    	print (end='\n')


#WRITES THE SOLVED SUDOKU IN THE FORM OF A STRING
def write(values):
	output = ""
	for variable in squares:
		output = output + values[variable]
	return output
