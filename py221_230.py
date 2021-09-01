def print_reverse(string):
    print(string[::-1])

def print_scores(score):
    sum = 0
    
    for i in score:
        sum+=i
    print(sum/len(score))

def print_even(ls):
    for val in ls:
        if val%2==0:
            print(val)

def print_keys(dic):
    for key in dic.keys():
        print(key)

def print_value_by_key(my_dict,key):
    print(my_dict[key])
        
def print_5xn(string):
    for i in range(0,len(string)-4,5):
        print(string[i:i+5])

def calc_monthly_salary(annual_salary):
    print(int(annual_salary/12))


my_dict = {"10/26":[100,130,100,100],
            "10/27":[10,12,10,11]}

print_reverse("abcde")
print_scores([1,2,3])
print_even([1,3,2,10,12,11,15])
print_keys({"이름":"김말똥","나이":30,"성별":0})
print_value_by_key(my_dict,"10/26")
print_5xn("아이엠어보이유알어걸")
calc_monthly_salary(12000000)