#21
letters = 'python'
print(letters[0],letters[2])

#22
license_plate = "24가 2210"
print(license_plate[-4:])

#23
string="OEOEOE"
print(string[::2])

#24
string="PYTHON"
print(string[::-1])

#25
phone_number  = "010-1111-2222"
phone_number_replaced = phone_number.replace("-"," ")
print(phone_number_replaced)

#26
phone_number_replaced = phone_number_replaced.replace(" ","")
print(phone_number_replaced)

#27
url="http://sharebook.kr"
parsed_url  = url.split(".")
print(parsed_url[-1])


