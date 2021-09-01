def make_url(string):
    return f"www.{string}.com"

def make_list(string):
    ls=[]
    for i in string:
        ls.append(i)
    return ls

def pickup_even(nums):
    ls=[]
    for val in nums:
        if val%2==0:
            ls.append(val)
    return ls

def convert_int(string):
    comma_removed = string.replace(",","")
    return int(comma_removed)

print(make_url("naver"))
print(make_list("abcd"))
print(pickup_even([3,4,5,6,7,8]))
print(convert_int("1,234,567"),type(convert_int("1,234,567")))