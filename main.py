from replit import clear
from art import logo
def start():
  i=0
  loop=True
  print(logo)
  first_number=float(input('What is the first number :'))
  symbol=input('''pick a symbol from the following

+
-
*
/
//
^

''')
  while loop: 
      i+=1
      if i>1:
       symbol=input('pick a symbol :\n')
      print()
      second_number=float(input('What is the other number :'))
      print()

      def operation(first_number,second_number):
        global result
        if symbol=='+':
          result=first_number + second_number
        elif symbol=='-':
          result=first_number-second_number  
        elif symbol=='*':
          result=first_number*second_number
        elif symbol=='/':
          result=first_number/second_number 
        elif symbol=='//':
          result=first_number//second_number
        elif symbol=='^':
          result=first_number**second_number 
        return print(f'{first_number} {symbol} {second_number}=',result)

      operation(first_number,second_number) 
      print()   
      ask=input(f"type 'y' to continue with {result} or 'n' to start a new calculation :")
      print() 

      if ask=='y':
        first_number=result
      
      else:
        clear() 
        start()      
start()