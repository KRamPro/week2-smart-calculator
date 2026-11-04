"""A basic calculator and a brute-force equation solver."""

import ast
import operator


# These are the only operations allowed in an equation expression.
_BINARY_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
}
_UNARY_OPERATORS = {ast.UAdd: operator.pos, ast.USub: operator.neg}


def evaluate_expression(expression, x_value):
    """Evaluate an arithmetic expression containing x."""
    tree = ast.parse(expression, mode="eval").body

    def evaluate(node):
        """Evaluate one expression-tree node if its syntax is supported."""
        # Match each supported node type so other Python syntax is rejected.
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

    return evaluate(tree)


def basic_calculate(first_number, second_number, operation):
    """Perform one basic arithmetic operation."""
    # Choose the requested operation and guard division against a zero divisor.
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
    raise ValueError("Choose +, -, *, or /.")


def solve_for_x(expression, target, start=-100, end=100, show_steps=False):
    """Search in steps of 0.1 and return the x closest to the target."""
    best_x = start
    best_difference = float("inf")
    number_of_steps = round((end - start) / 0.1)

    for index in range(number_of_steps + 1):
        x_value = start + index * 0.1
        result = evaluate_expression(expression, x_value)
        difference = abs(result - target)

        # Print this guess when requested, then keep it if it is the closest so far.
        if show_steps:
            print(f"x = {x_value:.1f}: result = {result:.2f}, difference = {difference:.2f}")
        if difference < best_difference:
            best_x = x_value
            best_difference = difference

    return best_x, best_difference


def equation_solver_menu():
    """Ask for an expression and target, then print the closest x."""
    expression = input("Enter an expression containing x (for example, x + 5): ")
    target = float(input("What should the expression equal? "))
    x_value, difference = solve_for_x(expression, target)
    print(f"Closest x: {x_value:.1f} (difference: {difference:.2f})")


def visualize_search():
    """Show the search steps for x + 5 = 12."""
    expression = "x + 5"
    target = 12
    # Print -10 through 10 instead of the full -100 through 100 search range:
    # 201 visible guesses explain the process without flooding the terminal with
    # roughly 2,000 lines of output.
    x_value, difference = solve_for_x(expression, target, -10, 10, show_steps=True)
    print(f"Closest x: {x_value:.1f} (difference: {difference:.2f})")


def explain_search_algorithm():
    """Explain brute-force search and name a smarter alternative."""
    print(
        "Brute-force search tries every candidate and keeps the closest one. "
        "It is slow because it does not skip guesses. Binary search is smarter "
        "for an ordered range because it repeatedly cuts that range in half."
    )


def main():
    """Show the menu repeatedly until the user chooses to exit."""
    while True:
        print("\nSmart Calculator")
        print("1. Basic calculation\n2. Equation solver\n3. Search visualisation")
        print("4. What is a search algorithm?\n5. Exit")
        choice = input("Choose an option: ").strip()

        # Run the selected feature; the final branch handles invalid choices.
        if choice == "1":
            try:
                first = float(input("First number: "))
                operation = input("Operation (+, -, *, /): ").strip()
                second = float(input("Second number: "))
                print("Result:", basic_calculate(first, second, operation))
            except (ValueError, ZeroDivisionError) as error:
                print("Could not calculate:", error)
        elif choice == "2":
            try:
                equation_solver_menu()
            except (SyntaxError, ValueError, ZeroDivisionError) as error:
                print("Could not solve that expression:", error)
        elif choice == "3":
            visualize_search()
        elif choice == "4":
            explain_search_algorithm()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 5.")


# Start the menu only when this file is run directly, not when imported.
if __name__ == "__main__":
    main()
