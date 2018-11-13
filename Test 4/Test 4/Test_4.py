
'''
Aaron McCormick
11/13/18
Test 3
'''

def main():
    argA = int(input("Enter value for Argument A : "))
    argB = int(input("Enter value for Argument B : "))
    argC = int(input("Enter value for Argument C : "))

    answer = crazy_formula(argA, argB, argC)
    
    #invoke the crazy_formula function
    #send in argA, argB and argC as arguments to function call
    #place value returned by function in the answer variable
    print("Answer from crazy_formula is", format(answer, ".2f"))

'''
define the crazy_formula function
'''
def crazy_formula(numb1, numb2, numb3):
    total = (numb1 + numb2 * 14) / numb3
    return total

main()