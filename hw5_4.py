def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
    except SyntaxError:
        print("Error: Operand error")
    except:
        print("Error: An unknown error occurred")

def check_parentheses(expression):
    opening = expression.count('(')
    closing = expression.count(')')
    if opening != closing:
        print("Error: Unbalanced parentheses")
        return False
    return True

def validate_expression(expression):
    operators = ['+', '-', '*', '/']
    valid_chars = set(operators + ['(', ')'] + [str(i) for i in range(10)])
    for char in expression:
        if char not in valid_chars:
            print("Error: Unsupported character")
            return False
    return True

def main():
    while True:
        user_input = input("Enter an arithmetic expression (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break

        if not check_parentheses(user_input) or not validate_expression(user_input):
            continue

        result = evaluate_expression(user_input)
        if result is not None:
            print("Result:", result)

main()
