#!/usr/bin/env python3


# Devuelve la precedencia de los operadores
#
# + -
# * /
# ^ -> potencia - ej: a^b
def precedence(operator):
    if operator == "+":
        return 1
    elif operator == "-":
        return 1
    elif operator == "*":
        return 2
    elif operator == "/":
        return 2
    elif operator == "^":
        return 3
    else:
        return 0


# Convierte una expresion matematica en notacion infija a notacion postfija
def infix_to_postfix(expression):
    output = []  # Lista para almacenar la salida en notacion postfija
    stack = []  # Lista para almacenar los operadores temporalmente
    operators = {"+": 0, "-": 0, "*": 0, "/": 0, "^": 0}

    for character in expression:
        if character.isdigit():
            output.append(
                character
            )  # Agrega directamente los dígitos a la salida
        elif character in operators:
            # Verifica si hay operadores en la pila con mayor o igual precedencia
            while (
                stack
                and stack[-1] in operators
                and precedence(stack[-1]) >= precedence(character)
            ):
                output.append(
                    stack.pop()
                )  # Extrae los operadores de la pila y los agrega a la salida
            stack.append(character)  # Agrega el operador actual a la pila

    while stack:
        output.append(
            stack.pop()
        )  # Extrae los operadores restantes de la pila y los agrega a la salida

    return "".join(
        output
    )  # Concatena los caracteres de la salida y la devuelve como cadena


# Evalua una expresión en notación postfija y devuelve el resultado
def evaluate_postfix(expression):
    stack = []

    for character in expression:
        if character.isdigit():
            stack.append(
                int(character)
            )  # Convierte los digitos a enteros y los agrega a la pila
        else:
            b = stack.pop()  # Extrae los operandos de la pila
            a = stack.pop()

            if character == "+":
                stack.append(
                    a + b
                )  # Realiza la suma y agrega el resultado a la pila
            elif character == "-":
                stack.append(
                    a - b
                )  # Realiza la resta y agrega el resultado a la pila
            elif character == "*":
                stack.append(
                    a * b
                )  # Realiza la multiplicacion y agrega el resultado a la pila
            elif character == "/":
                stack.append(
                    a / b
                )  # Realiza la division y agrega el resultado a la pila
            elif character == "^":
                stack.append(
                    a**b
                )  # Realiza la potencia y agrega el resultado a la pila

    return stack[0]  # Devuelve el resultado final


# Realiza pruebas de las funciones infix_to_postfix() y evaluate_postfix()
def test_calculator():
    assert infix_to_postfix("4-7+8+9/2*3") == "47-8+92/3*+"
    assert evaluate_postfix("47-8+92/3*+") == 18.5

    assert infix_to_postfix("2^3") == "23^"
    assert evaluate_postfix("23^") == 8


if __name__ == "__main__":
    # Para utilizar potencia utiliza a^b
    prompt = "Ingrese una expresión ej:(4-7+8+9/2*3^2): "
    expr = input(prompt)
    while True:
        if len(expr) > 20:
            print("Por favor ingrese una expresión no mayor a 20 caracteres. ")
            expr = input(prompt)
        else:
            break

    # Convierte la expresion a notación postfija
    postfix_expr = infix_to_postfix(expr)

    # Evalua la expresion postfija
    result = evaluate_postfix(postfix_expr)
    print(f"Resultado: {result}")

    # Ejecuta las pruebas, si hay un error genera un AssertionError
    # Si genera un AssertionError significa que la salida no fue la esperada.
    print(f"Tests para: calculadora.py")
    test_calculator()
