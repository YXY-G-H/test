Note 1: The Sample input entries will be not shown at the Sample Output
# Note 2: You need to put a print() after every input().
# Note 3: Your output generated MUST be EXACTLY the same as shown at the Sample Output

# Write your codes below
upper = 0
bottom = 0
moduleList = ["IT1111", "IT1213", "IT1101", "ITP111", "IT1110"]
gradeList = ["A", "B+", "B", "C+", "C", "D+", "D", "F"]
GPA = [4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]
valid = True
counter = 0

while True:
    module = input("Enter the module code (type end to finish) :")
    print()
    
    if module == "end":
        break
    else:
        if module in moduleList:
            credit = int(input("Enter the credit for module %s :" % module))
            print()
            
            while True:
                grade = input("Enter your grade for %s :" % module)
                print()
                
                if grade in gradeList:
                    gpa = GPA[gradeList.index(grade)]
                    upper += (credit * gpa)
                    bottom += credit
                    
                    
                    gradePoint = gpa * credit
                    print("Your GPA is %.1f for module %s that has %d credit point.  You earned %.1f grade points" %(gpa, module, credit, gradePoint), end="\n")
                    counter += 1
                    break
                else:
                    print("You have entered an invalid grade!", end="\n")
        else:
            print("You have entered an invalid module code", end="\n")
cumGPA = upper/bottom
print("Your cumulative GPA for %d modules are %.2f" %(counter, cumGPA), end="\n")







#Click on Run Code button to test your codes and verify it passes all the test cases
