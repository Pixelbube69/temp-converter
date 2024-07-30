"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 3
---------------------------------------------------------------------------------
- File Name: lab3.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Learn how to format numbers for display.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Ask the user for a decimal number and store it in a variable 'num1', converting to a float


# Round the number to 2 decimal places using the round function


# Define a large integer


# Print the large integer with commas as thousands separators using f-strings


# Define a small floating-point number


# Print the number in scientific notation using f-strings


# Define a small integer


# Print the number with leading zeros using f-strings


a=float(input("Please enter a decimal number"))
result = (round(a, 2))
print(f"Rounded to 2 decimal places is: {result} ")
print(f"lage number: {a}")
print(f"My small number: {result:.2e}")
print(f"My large number: {a:.2e}")