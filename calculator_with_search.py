"""A basic calculator and a brute-force equation solver."""

import ast
import operator


_BINARY_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
}
_UNARY_OPERATORS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


def evaluate_expression(expression, x_value):
    """Evaluate arithmetic with x, allowing only basic arithmetic syntax."""
    tree = ast.parse(expression, mode="eval")

    def evaluate(node):
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value
        if isinstance(node, ast.Name) and node.id == "x":
            return x_value
        if isinstance(node, ast.BinOp) and type(node.op) in _BINARY_OPERATORS:
            left = evaluate(node.left)
            right = evaluate(node.right)
            return _BINARY_OPERATORS[type(node.op)](left, right)
        if isinstance(node, ast.UnaryOp) and type(node.op) in _UNARY_OPERATORS:
            return _UNARY_OPERATORS[type(node.op)](evaluate(node.operand))
        raise ValueError("Use x, numbers, parentheses, and +, -, *, /, or ** only.")

    return evaluate(tree.body)


def basic_calculate(first_number, second_number, operation):
    """Perform one basic arithmetic operation and return its result."""
    if operation == "+":
        return first_number + second_number
    if operation == "-":
        return first_number - second_number
    if operation == "*":
        return first_number * second_number
    if operation == "/":
        if second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first_number / second_number
    raise ValueError("Choose one of: +, -, *, /. ")


def search_for_x(expression, target, start=-100, end=100, step=0.1, show_steps=False):
    """Try values in a range and return the one closest to the target."""
    number_of_steps = round((end - start) / step)
    best_x = start
    best_difference = float("inf")

    for index in range(number_of_steps + 1):
        x_value = start + index * step
        result = evaluate_expression(expression, x_value)
        difference = abs(result - target)

        if show_steps:
            print(f"x = {x_value:.1f} -> result = {result:.2f}, difference = {difference:.2f}")

        if difference < best_difference:
            best_x = x_value
            best_difference = difference

    return best_x, best_difference


def solve_for_x(expression, target):
    """Search from -100 to 100 in steps of 0.1 for the closest x."""
    return search_for_x(expression, target)


def equation_solver_menu():
    """Ask for an expression and target, then report the closest x found."""
    expression = input("Enter an expression containing x (for example, x + 5): ")
    target = float(input("What should the expression equal? "))

    x_value, difference = solve_for_x(expression, target)
    print(f"Closest x: {x_value:.1f} (difference from target: {difference:.2f})")


def visualize_search():
    """Show the search steps for the example x + 5 = 12."""
    expression = "x + 5"
    target = 12
    # Use a smaller range so the demonstration does not flood the terminal.
    start = -10
    end = 10

    print(f"Searching for x in: {expression} = {target}")
    x_value, difference = search_for_x(
        expression, target, start=start, end=end, step=0.1, show_steps=True
    )
    print(f"Closest x: {x_value:.1f} (difference from target: {difference:.2f})")


def explain_search_algorithm():
    """Print a brief explanation of brute-force and a smarter search."""
    print(
        "Brute-force search tries every candidate and keeps the closest one. "
        "It is slow because it does not use clues to skip candidates. "
        "Binary search is smarter when the search space is ordered: it repeatedly "
        "cuts the remaining range in half."
    )


def main():
    """Run the calculator menu until the user chooses to exit."""
    while True:
        print("\nSmart Calculator")
        print("1. Basic calculation")
        print("2. Equation solver")
        print("3. Search visualisation")
        print("4. What is a search algorithm?")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            try:
                first_number = float(input("First number: "))
                operation = input("Operation (+, -, *, /): ").strip()
                second_number = float(input("Second number: "))
                result = basic_calculate(first_number, second_number, operation)
                print(f"Result: {result}")
            except (ValueError, ZeroDivisionError) as error:
                print(f"Could not calculate: {error}")
        elif choice == "2":
            try:
                equation_solver_menu()
            except (SyntaxError, ValueError, ZeroDivisionError) as error:
                print(f"Could not solve that expression: {error}")
        elif choice == "3":
            visualize_search()
        elif choice == "4":
            explain_search_algorithm()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
