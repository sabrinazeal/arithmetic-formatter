def arithmetic_arranger(problems, show_answers=False):
    """Displays a formatted version of the given problems."""

    if len(problems) > 5:
        return "Error: Too many problems."

    first_line, second_line, third_line, fourth_line = "", "", "", ""

    while problems:

        # Grabs the first problem from the input
        # If there are still more to come afterwards, includes the 4-space separator
        problem = problems.pop(0)
        if len(problems) > 0:
            problem_separator = " " * 4
        else:
            problem_separator = ""

        # Validates input operators and grabs operands
        if "+" in problem and "-" not in problem:
            operator = "+"
            operands_list = problem.split("+")
        elif "-" in problem and "+" not in problem:
            operator = "-"
            operands_list = problem.split("-")
        else:
            return "Error: Operator must be '+' or '-'."

        # Normalizes and validates operands
        first_operand = operands_list[0].strip()
        second_operand = operands_list[1].strip()

        if (not first_operand.isdigit()) or (not second_operand.isdigit()):
            return "Error: Numbers must only contain digits."
        if (len(first_operand) > 4) or (len(second_operand) > 4):
            return "Error: Numbers cannot be more than four digits."

        # Determines problem length and required alignment for each line
        problem_length = max(len(first_operand), len(second_operand)) + 2
        first_line_spaces = " " * (problem_length - len(first_operand))
        second_line_spaces = " " * (problem_length - len(second_operand) - 2)
        third_line_dashes = "-" * problem_length

        # Assembles the three mandatory lines
        first_line = f"{first_line}{first_line_spaces}{first_operand}{problem_separator}"
        second_line = f"{second_line}{operator} {second_line_spaces}{second_operand}{problem_separator}"
        third_line = f"{third_line}{third_line_dashes}{problem_separator}"

        # Assembles the optional fourth line with the results
        if show_answers:
            if operator == "+":
                result = int(first_operand) + int(second_operand)
            elif operator == "-":
                result = int(first_operand) - int(second_operand)
            else:
                return "Error: Operator must be '+' or '-'."

            fourth_line_spaces = " " * (problem_length - len(str(result)))
            fourth_line = f"{fourth_line}{fourth_line_spaces}{result}{problem_separator}"

    # Joins all lines together into the final output
    arranged_problems = f"{first_line}\n{second_line}\n{third_line}"
    if show_answers:
        arranged_problems = f"{arranged_problems}\n{fourth_line}"

    return arranged_problems
