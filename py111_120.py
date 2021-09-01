#113
"""integer = int(input())
if integer%2 == 0:
    print("even")
else:
    print("odd")"""

#114
"""integer = int(input())
if (integer+20)>255:
    print(255)
else :
    print(integer+20)"""

#115
"""integer = int(input())
result = integer - 20
if (result<0)or(result>255):
    print(0)
else :
    print(result)"""

#116
"""time = input()
minute = time.split(":")
if minute[1]=="00":
    print("정각")
else :
    print("No")"""

#117
"""fruit = ["apple","grape","pear"]
val = input()
if val in fruit:
    print("right")
else :
    print("Wrong")"""

#119
fruit = {"spring":"starwberry","summer":"tomato","fall":"apple"}
val = input()
if val in fruit.values():
    print("right")
else : 
    print("worng")