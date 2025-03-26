# Complex Number Categorization

num = complex(input("Enter a complex number (e.g., 3+4j): "))

if num.real == 0 and num.imag == 0:
    print("The number is Zero")
elif num.real == 0:
    print("Purely Imaginary Number")
elif num.imag == 0:
    print("Purely Real Number")
else:
    print("Complex Number with both real and imaginary parts")
