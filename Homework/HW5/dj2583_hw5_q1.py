def arithmetic_expressions(text, variables):
    stack = []
    for string in text:
        if string.isdigit():
            stack.append(int(string))
        elif string.isalpha():
            value = next((val for name, val in variables if name == string), None)
            if value is not None:
                stack.append(value)
            else:
                raise Exception(f"Variable '{string}' is not defined.")
        elif string in ['+', '-', '*', '/']:
            try:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if string == '+':
                    stack.append(operand1 + operand2)
                elif string == '-':
                    stack.append(operand1 - operand2)
                elif string == '*':
                    stack.append(operand1 * operand2)
                elif string == '/':
                    stack.append(operand1 / operand2)
            except IndexError:
                raise ValueError("Invalid expression or insufficient operands.")

    if len(stack) != 1:
        raise Exception("Invalid expression.")

    return stack[0]


def handle_assignment(user_input, variables):
    new_input = user_input.split()
    if new_input[0].isalpha() and len(new_input) > 2 and new_input[1] == "=":
        var_name = new_input[0]
        expression = new_input[2:]
        try:
            value = arithmetic_expressions(expression, variables)
            variables.append((var_name, value))
            print(f"{var_name}")
        except ValueError as e:
            print(f"Error: {e}")


def main():
    variables = []

    user_input = input("--> ").strip()

    while user_input.lower() != "done()":
        if '=' in user_input:
            handle_assignment(user_input, variables)
        else:
            new_input = user_input.split()
            try:
                result = arithmetic_expressions(new_input, variables)
                print(result)
            except ValueError as e:
                print(f"Error: {e}")

        user_input = input("--> ").strip()

main()

