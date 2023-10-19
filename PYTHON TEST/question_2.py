#(i)
#function to find the average of two numbers.
def average_of_two_numbers(x, y):
    output = (x + y) / 2
    print(f"the average {output}")

average_of_two_numbers(1, 3)
average_of_two_numbers(4, 10)
average_of_two_numbers(90, 100)



    
#(ii)  programe that asks user to input two numbers and finds the minimum number
def find_min_two_numbers():
    number1 = float(input("Enter the first number: "))     #float accomodates both int and float
    number2 = float(input("Enter the second number:"))

    output = min(number1, number2)
    print(f"The minimum number is {output}")

find_min_two_numbers()




  
    