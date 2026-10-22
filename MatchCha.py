day = int(input("Enter day number: "))

match day:
    case 1:
        print("Monday")
    case 3:
        print("Wednesday")
    case _:
        print("Other day")