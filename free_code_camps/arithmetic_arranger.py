# Students in primary school often arrange arithmetic problems
# vertically to make them easier to solve. For example,
# "235 + 52" becomes:
#
#   235
# +  52
# -----
# Create a function that receives a list of strings that are arithmetic problems
# and returns the problems arranged vertically and side-by-side.
# The function should optionally take a second argument.
# When the second argument is set to True, the answers should be displayed.


# Example
# Function Call:
#
# arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
# Output:
#
#    32      3801      45      123
# + 698    -    2    + 43    +  49
# -----    ------    ----    -----
# Function Call:
#
# arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
# Output:
#
#   32         1      9999      523
# +  8    - 3801    + 9999    -  49
# ----    ------    ------    -----
#   40     -3800     19998      474


# Rules
# The function will return the correct conversion if the supplied problems are properly formatted,
# otherwise, it will return a string that describes an error that is meaningful to the user.
#
# Situations that will return an error:
# If there are too many problems supplied to the function. The limit is five, anything
# more will return: Error: Too many problems.
# The appropriate operators the function will accept are addition and subtraction.
# Multiplication and division will return an error. Other operators not mentioned in
# this bullet point will not need to be tested. The error returned will be: Error: Operator must be '+' or '-'.
# Each number (operand) should only contain digits. Otherwise, the function will return:
# Error: Numbers must only contain digits.
# Each operand (aka number on each side of the operator) has a max of four digits in width.
# Otherwise, the error string returned will be: Error: Numbers cannot be more than four digits.
# If the user supplied the correct format of problems, the conversion you return will follow these rules:
# There should be a single space between the operator and the longest of the two operands,
# the operator will be on the same line as the second operand, both operands will be in the same
# order as provided (the first will be the top one and the second will be the bottom).
# Numbers should be right-aligned.
# There should be four spaces between each problem.
# There should be dashes at the bottom of each problem. The dashes should run along the entire
# length of each problem individually. (The example above shows what this should look like.)

def arithmetic_arranger(operations: [str], display_answer=False):
    top_operand = ""
    bottom_operand = ""
    lines = ""
    totals = ""

    # Split the string into operands and operator
    for n in operations:
        first_number, opt, second_number = operations[operations.index(n)].split(' ')

        # Operands must only contain digits
        if not first_number.isdigit() or not second_number.isdigit():
            return print("Error: Numbers must only contain digits")

        # Operators must only be addition or subtraction
        if opt not in ['+', '-']:
            return print("Error: Operator must be '+' or '-'")

        # Max of four digits for operands
        if len(first_number) > 4 or len(second_number) > 4:
            return print("Error: Numbers cannot be more than four digits")

        # Make the arithmetic operation
        if opt == "+":
            result = int(first_number) + int(second_number)
        else:
            result = int(first_number) - int(second_number)

        # Get distance for longest operator
        operator_distance = max(len(first_number), len(second_number)) + 2

        second_number = opt + second_number.rjust(operator_distance - 1)
        top_operand = top_operand + first_number.rjust(operator_distance) + (4 * " ")
        bottom_operand = bottom_operand + second_number + (4 * " ")
        lines = lines + len(second_number) * "-" + (4 * " ")
        totals = totals + str(result).rjust(operator_distance) + (4 * " ")

    if display_answer:
        return top_operand + '\n' + bottom_operand + '\n' + lines + '\n' + totals

    return top_operand + '\n' + bottom_operand + '\n' + lines


if __name__ == '__main__':
    print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], display_answer=True))
