# Working with Numbers
from pyscript import display, document

#def greetings(e): # creating function
#    username = document.getElementById("input1").value # getting a value from a textbox
#    display(f'Hello {username}!', target="result")

def adding_numbers(e): 
    document.getElementById('result').innerHTML="" #clearing the previous output
    number1 = float(document.getElementById('num1').value)
    number2 = float(document.getElementById('num2').value)
    sum = number1 + number2

    display(f'The sum of {number1} and {number2} is {sum}', target="result")

def subtracting_numbers(e): 
    document.getElementById('result').innerHTML="" 
    number1 = float(document.getElementById('num1').value)
    number2 = float(document.getElementById('num2').value)
    difference = number1 - number2

    display(f'The difference of {number1} and {number2} is {difference}', target="result")

def multiplying_numbers(e):
    document.getElementById('result').innerHTML = " " 
    number1 = float(document.getElementById('num1').value)
    number2 = float(document.getElementById('num2').value)
    product = number1 * number2

    display(f'The difference of {number1} and {number2} is {product}.', target='result')

def exponentiating_numbers(e):
    document.getElementById('result').innerHTML = " " 
    number1 = float(document.getElementById('num1').value)
    number2 = float(document.getElementById('num2').value)
    power = number1 ** number2

    display(f'{number1} raised to the power of {number2} is {power}.', target='result')

def dividing_numbers(e):
    document.getElementById('result').innerHTML = " " 
    number1 = float(document.getElementById('num1').value)
    number2 = float(document.getElementById('num2').value)
    quotient = number1 / number2

    display(f'The quotient of {number1} and {number2} is {quotient}.', target='result')

def modulo_numbers(e):
    document.getElementById('result').innerHTML = " " 
    number1 = float(document.getElementById('num1').value)
    number2 = float(document.getElementById('num2').value)
    modulo = number1 % number2

    display(f'The quotient of {number1} and {number2} is {modulo}.', target='result')

def floordiv_numbers(e):
    document.getElementById('result').innerHTML = " " 
    number1 = float(document.getElementById('num1').value)
    number2 = float(document.getElementById('num2').value)
    roundown = number1 // number2

    display(f'The quotient of {number1} and {number2} rounded down is {roundown}.', target='result')

