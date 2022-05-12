"""
Start
get the number of sheets
sheets / 5
round answer to next number
output the results to the user
end
"""
import math

# input: sheet
def calculate(sheet):
    # step 1
    answer = sheet / 5
    # step 2
    rounded = round(answer)
    print("sheet is : ", sheet)
    print("The answer is: ", answer)
    print("rounded is: ", answer)
    print("=================================")
    # output: number of stamps needed
    return rounded

output = calculate(10000)

print("the return statement is: ", output)
