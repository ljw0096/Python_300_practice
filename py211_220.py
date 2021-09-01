#215
def print_with_smile(string):
    print(f"{string}:D")

def print_upper_price(now_price):
    upper_price = now_price*1.3
    print(upper_price)
    
def print_sum(a,b):
    print(a+b)

def print_arithmetic_operation(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

def print_max(a,b,c):
    if a>b:
        if a>c:
            print(a)
        else:
            print(c)    
    else:
        if(b>c):
            print(b)
        else:
            print(c)
print_with_smile("hi!")
print_upper_price(100)
print_sum(1,2)
print_arithmetic_operation(3,4)
print_max(1,3,1)