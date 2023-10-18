from art import logo
def add(x,y):
  return x + y

def Sub(x,y):
  return x - y

def Mul(x,y):
  return x * y

def Div(x,y):
  return x / y

operations = {'+':add,
              '-':Sub, 
              '*':Mul,
              '/':Div}


# function = operations['*']
# print(function(2,3))
def calculator():
  print(logo)
  num1 = float(input('Enter the first number for operation :'))
 
  for key in operations:
    print(key)
  should_continue = True
  
  while should_continue:
    operation_symbo = input('Pick a symbol for the operation :')
    num2 = float(input('Enter the Next number for operation :'))
    fucntion = operations[operation_symbo]
    answer = fucntion(num1,num2)
    print(f'{num1} {operation_symbo} {num2} = {answer}')
    
    
    # other_operation = input('pick another operand : ')
    # num3 = int(input("what's the next number :"))
    # fucntion = operations[operation_symbo]
    # second_answer = fucntion(first_answer,num3)
    
    # print(f'{num1} {operation_symbo} {num2} = {answer}')
    if input(f"Do you want to continue with {answer} ? if yes then type 'y' or if no then type 'n' to start a new Calculation.") == 'y':
      num1 = answer
    else:
      should_continue  = False
      calculator()
    


calculator()