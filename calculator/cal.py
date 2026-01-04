print("\n**simple calculator**\n")

while True:
    try : 
        a = float(input("\nEnter 1st number : "))

        print ("\n**choose the operations to be performed**\n")
        print ("1. for addition ")
        print ("2. for subtraction")
        print ("3. division")
        print ("4. multiplication")
        print ("5. no operation .. exit")

        n  = int(input("\nEnter choice :\n"))
        b = float(input("\nEnter 2nd number : "))

        match (n):
            case 1:
                print(f"Addition of {a}+{b} = {a+b}")
            case 2:
                print(f"Substraction of {a}-{b}= {a-b}")
            case 3:
                try:
                    print(f"Dividing {a}/{b}= {a/b}")
                except ZeroDivisionError:
                    print("Division by zero not possible")
            case 4:
                print(f"Multiplying {a}*{b}= {a*b}")
            case 5:
                print("exiting\n")
                break

            case _:
                print("invalid choice")
    except ValueError:
        print("enter a valid number !!!")
          


    