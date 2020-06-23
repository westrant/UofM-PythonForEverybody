## Running count and running total
largest = None
smallest = None

while True:
    sval = input("Enter a number: ")
    if sval == "done":
        break
    try:
        ival = int(sval)
    except:
        print("Invalid input")
        continue

    if largest is None:
        largest = ival
    elif ival > largest:
        largest = ival

    if smallest is None:
        smallest = ival
    elif ival < smallest:
        smallest = ival

try:
    print("Maximum is", largest)
    print("Minimum is", smallest)
except:
    print("Divide by zero error - need to enter more numbers")
