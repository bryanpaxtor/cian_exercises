# Calculadora en Python

## Caracteristicas del programa

- Operadores:  
  suma(+), resta(-), multiplicacion(\*), division(/), y potencia(^)
- Precedencia en el orden: ^, \*, /, +, -
- Maximo de 20 caracteres
- Incluye pruebas unitarias para verificar la converios a postfix y evalua el resultado.

# Calculadora en notacion postfix

Esta es una calculadora en Python que convierte una expresion
de notacion infix a postfix, despues evalua el resultado.

## Proceso de solucion

1. **Funcion de precedencia**:
   La función `get_precedence()` evalúa la precedencia de un operador (`+`, `-`, `*`, `/`, `^`).
   Precedencia:
   suma y resta = 1  
   multiplicacion y division = 2  
   potencia = 3  
   otros = 0

2. **Conversión a notación postfix**:
   La funcion `infix_to_postfix()` recibe una expresion en notacion infix como input, utiliza una pila y reglas de precedencia para convertir la expresion a una notacion postfix, se asegura de procesar cada caracter de la expresion y lo agrega a la salida en notacion postfix, si encuentra operadores los mueve desde la la pila(stack) a la salida(output) segun su precedencia.

3. **Evaluación de la expresión postfix**:
   La funcion `evaluate_postfix()` recibe una expresion postfix como input, utiliza una pila para evaluar la expresion paso a paso, si encuentra un operando lo agrega a la pila, si encuentra un operador, toma los operandos mas recientes de la pila, realiza la operacion y agrega el resultado nuevamente a la pila, al final el resultado final siempre esta en la cima de la pila.

4. **Función principal**:
   La funcion `__main__` es la funcion principal del programa, solo funciona cuando se ejecuta el script directamente (no funciona cuando se importa como modulo).

## Ejecución del programa

Para ejecutar el programa, favor de seguir los siguientes pasos:

1. Abrir una terminal

2. Ejecuta el comando `python3 calculadora.py`.

3. Ingresar una expresión matemática, favor de tomar en cuenta que para utilizar `potencia` usar  
   la expresion `a^b` y no a\*\*b.

4. El programa imprimirá el resultado de la expresión.

Gracias!
