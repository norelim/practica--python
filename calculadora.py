# def add(numberOne,numberTwo):
#  return numberOne + numberTwo
#  print(add(10,30))

# def substract(numberOne,numberTwo):
#  return numberOne + numberTwo
#  print(add(10,30))

# def substract(numberOne,numberTwo):
#  return numberOne + numberTwo
#  print(add(10,30))

# def substract(numberOne,numberTwo):
#  return numberOne + numberTwo
#  print(add(10,30))

# UNA FORMA
numberOne = 5
numberTwo = 5
add = numberOne + numberTwo
print(add)

# OTRA FORMA
add = lambda numberOne, numberTwo: numberOne + numberTwo
print(add(40,30))

rest = lambda numberOne, numberTwo: numberOne - numberTwo
print(rest(40,30))

multiplicar = lambda numberOne, numberTwo: numberOne * numberTwo
print(multiplicar(40,30))

dividir = lambda numberOne, numberTwo: numberOne / numberTwo
print(dividir(40,30))