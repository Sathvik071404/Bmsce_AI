
import re

def parse_expression(text):
    text = text.replace(" ", "")

    if not text:
        return ""

    if "(" not in text:
        return text

    match = re.match(r"^([A-Za-z0-9_]+)\((.*)\)$", text)

    if not match:
        raise ValueError("Invalid expression: " + text)

    name = match.group(1)
    args_string = match.group(2)

    args = []
    current = ""
    depth = 0

    for char in args_string:
        if char == "," and depth == 0:
            args.append(current)
            current = ""
        else:
            current += char

            if char == "(":
                depth += 1
            elif char == ")":
                depth -= 1

    if current:
        args.append(current)

    return [name] + [parse_expression(arg) for arg in args]

def format_expression(expr):
    if isinstance(expr, str):
        return expr

    if isinstance(expr, list):
        name = expr[0]

        if len(expr) == 1:
            return name

        return name + "(" + ", ".join(format_expression(arg) for arg in expr[1:]) + ")"

    return str(expr)

def is_variable(term):
    if not isinstance(term, str):
        return False

    return len(term) == 1 and term.isalpha()

def occurs(variable, expression):
    if variable == expression:
        return True

    if isinstance(expression, list):
        for argument in expression[1:]:
            if occurs(variable, argument):
                return True

    return False

def apply_substitution(substitution, expression):
    if isinstance(expression, str):
        visited = set()

        while expression in substitution:
            if expression in visited:
                break

            visited.add(expression)
            expression = substitution[expression]

        return expression

    if isinstance(expression, list):
        return [expression[0]] + [apply_substitution(substitution, arg) for arg in expression[1:]]

    return expression

def unify(x, y, substitution=None):
    if substitution is None:
        substitution = {}

    x = apply_substitution(substitution, x)
    y = apply_substitution(substitution, y)

    if x == y:
        return substitution

    if is_variable(x):
        if occurs(x, y):
            print("Occurs check failed:", x, "in", format_expression(y))
            return None

        print("Substitute:", x, "->", format_expression(y))
        substitution[x] = y
        return substitution

    if is_variable(y):
        if occurs(y, x):
            print("Occurs check failed:", y, "in", format_expression(x))
            return None

        print("Substitute:", y, "->", format_expression(x))
        substitution[y] = x
        return substitution

    if isinstance(x, list) and isinstance(y, list):
        if x[0] != y[0]:
            print("Function mismatch:", x[0], "!=", y[0])
            return None

        if len(x) != len(y):
            print("Arity mismatch:", x[0])
            return None

        for i in range(1, len(x)):
            print("Matching:", format_expression(apply_substitution(substitution, x[i])), "with", format_expression(apply_substitution(substitution, y[i])))

            substitution = unify(x[i], y[i], substitution)

            if substitution is None:
                return None

        return substitution

    print("Cannot unify:", format_expression(x), "with", format_expression(y))
    return None

def main():
    print("FIRST ORDER LOGIC UNIFICATION")

    expression1 = input("Enter Expression 1: ")
    expression2 = input("Enter Expression 2: ")

    try:
        expr1 = parse_expression(expression1)
        expr2 = parse_expression(expression2)

        print("\nExpression 1:", format_expression(expr1))
        print("Expression 2:", format_expression(expr2))

        print("\nUNIFICATION TRACE")

        result = unify(expr1, expr2)

        if result is None:
            print("\nResult: UNIFICATION FAILED")
        else:
            print("\nResult: UNIFICATION SUCCESSFUL")

            if not result:
                print("MGU: {}")
            else:
                print("MGU:")

                for variable, value in result.items():
                    value = apply_substitution(result, value)
                    print(variable, "->", format_expression(value))

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
