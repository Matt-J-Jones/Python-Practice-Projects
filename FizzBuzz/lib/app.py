import fizzbuzz

end = input("Enter the number you want to end the FizzBuzz at: ")
for i in range(1, int(end) + 1):
    print(fizzbuzz.fizzbuzz(i))