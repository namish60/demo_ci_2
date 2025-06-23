#calculator

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b


def div(a,b):
    if b==0:
        print("enter division by 0 is not possible")
        return
    return a/b

def menu():
    print("enter 1 for add")
    print("enter 2 for sub")
    print("enter 3 for mul")
    print("enter 4 for div")
    print("enter 5 for exit")

if __name__ == "__main__":
    while True:
        menu()
        ch = int(input("enter your choice"))
        if ch==1:
            a = int(input("enter the number 1"))
            b=  int(input("enter the number 2"))
            ans = add(a,b)
            print(f"the result is {ans}")
        
        elif ch==2:
            a = int(input("enter the number 1"))
            b=  int(input("enter the number 2"))
            ans = sub(a,b)
            print(f"the result is {ans}")

        elif ch==3:
            a = int(input("enter the number 1"))
            b=  int(input("enter the number 2"))
            ans = mul(a,b)
            print(f"the result is {ans}")

        elif ch==4:
            a = int(input("enter the number 1"))
            b=  int(input("enter the number 2"))
            ans = div(a,b)
            print(f"the result is {ans}")
        
        elif ch==5:
            print("exiting the program..")
            break