import re


def arithmetic_solver(operand_1, operator, operand_2):
    if operator == "-":
        return int(operand_1) - int(operand_2)
    elif operator == "+":
        return int(operand_1) + int(operand_2)


def arithmetic_dashes(operand_1, operand_2):
    length_of_operand = (
        len(operand_1) if len(operand_1) > len(operand_2) else len(operand_2)
    )
    if length_of_operand == 1:
        return ["-", "-", "-"]
    elif length_of_operand == 2:
        return ["-", "-", "-", "-"]
    elif length_of_operand == 3:
        return ["-", "-", "-", "-", "-"]
    elif length_of_operand >= 4:
        return ["-", "-", "-", "-", "-", "-"]


def arithmetic_arranger(problems, show_answers=False):
    first_operand_row = []
    operation_row = []
    dashes_row = []
    answers_row = []

    # validates if prblems length list is greater than 5
    if len(problems) > 5:
        # raise Exception("Error: Too many problems.")
        return "Error: Too many problems."
    else:
        # iterate through prblems list
        for problem in problems:
            # split problem by space and injects in a list
            split = problem.split(" ")

            # validates operator whether it is + or -
            if split[1] != "+" and split[1] != "-":
                # raise Exception("Error: Operator must be '+' or '-'.")
                return "Error: Operator must be '+' or '-'."
            # validates whether operands' length are greater than 4
            elif (
                len(split[0]) if len(split[0]) > len(
                    split[2]) else len(split[2])
            ) > 4:
                # raise Exception("Error: Numbers cannot be more than four digits.")
                return "Error: Numbers cannot be more than four digits."
            # validates whether operands contain non-numeric characters
            elif re.search(r"\D", split[0]) or re.search(r"\D", split[2]):
                # raise Exception("Error: Numbers must only contain digits.")
                return "Error: Numbers must only contain digits."
            # arrange arithmetic expressions
            else:
                # list representing rows

                # minimum width of presentation
                width = len(arithmetic_dashes(split[0], split[2]))
                # minimum dashes based on operand char length; 2 => 4 dashes, 3 => 5 dashes, 4 => 6 dashes
                dashes = "".join(arithmetic_dashes(split[0], split[2]))

                # append first operand to first row list
                first_operand_row.append(f"{split[0]:>{width}}")

                # append operator and second operand to second row list
                operation_row.append(f"{split[1]}{split[2]:>{width - 1}}")

                # append dashes to dashes row list
                dashes_row.append(f"{dashes:>{width}}")

                # append answers to answers row list
                answers_row.append(
                    f"{arithmetic_solver(
                        split[0], split[1], split[2]):>{width}}"
                )

    #                 # prints individual problems to terminal for debugging
    #                 match show_answers:
    #                     case True:
    #                         return f"""
    # {split[0]:>{width}}
    # {split[1]}{split[2]:>{width - 1}}
    # {dashes:>{width}}
    # {arithmetic_solver(split[0], split[1], split[2]):>{width}}
    # """
    #                     case False:
    #                         print(f"""
    # {split[0]:>{width}}
    # {split[1]}{split[2]:>{width - 1}}
    # {dashes}
    # """)

    match show_answers:
        case True:
            return f"{'    '.join(first_operand_row)}\n{'    '.join(operation_row)}\n{'    '.join(dashes_row)}\n{'    '.join(answers_row)}"
        case False:
            return f"{'    '.join(first_operand_row)}\n{'    '.join(operation_row)}\n{'    '.join(dashes_row)}"


if __name__ == "__main__":
    problems = ["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]

    # title
    print("""
python arithmetic formatter / arranger
######################################
""")

    print(f"\n{arithmetic_arranger(problems, show_answers=True)}")

    # expected output
    # print("  3801      123\n-    2    +  49\n------    -----")


"""
Build an Arithmetic Formatter Project
#####################################

Students in primary school often arrange arithmetic problems vertically to make them easier to solve.
For example, "235 + 52" becomes:

  235
+  52
-----
Finish the arithmetic_arranger function that receives a list of strings which are arithmetic problems,
and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument.
When the second argument is set to True, the answers should be displayed.

Example
Function Call:

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
Output:

   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
Function Call:

arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
Output:

  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474

Rules
#####

The function will return the correct conversion if the supplied problems are properly formatted,
otherwise, it will return a string that describes an error that is meaningful to the user.

Situations that will return an error:
- If there are too many problems supplied to the function.
- The limit is five, anything more will return: 'Error: Too many problems.'
- The appropriate operators the function will accept are addition(+) and subtraction(-).
  Multiplication(*) and division(/) will return an error.
  Other operators not mentioned in this bullet point will not need to be tested.
  The error returned will be: "Error: Operator must be '+' or '-'."
- Each number (operand) should only contain digits. Otherwise, the function will return:
  'Error: Numbers must only contain digits.'
- Each operand (aka number on each side of the operator) has a max of four digits in width.
  Otherwise, the error string returned will be:
  'Error: Numbers cannot be more than four digits.'
- If the user supplied the correct format of problems, the conversion you return will follow these rules:
  There should be a single space between the operator and the longest of the two operands,
  the operator will be on the same line as the second operand,
  both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).
- Numbers should be right-aligned.
- There should be four spaces between each problem.
- There should be dashes at the bottom of each problem.
- The dashes should run along the entire length of each problem individually.
- (The example above shows what this should look like.)
Note: open the browser console with F12 to see a more verbose output of the tests.
"""
