#33
print("-"*80)

#34
t1='python'
t2='java'
added = t1+t2
print(added*3)

#35
name1 = "Lee"
age1 = 10
name2 = "Park"
age2 = 20
print("name : %s age: %d" % (name1,age1))
print("name : %s age : %d" % (name2,age2))

#36
print("이름 : {} 나이: {}".format(name1,age1))
print("이름 : {} 나이 : {}".format(name2,age2))

#37
print(f"이름 : {name1} 나이 : {age1}")

#38
상장주식수 = "5,213,432,123"
get_rid_comma = int(상장주식수.replace(",",""))
print(get_rid_comma,type(get_rid_comma))

#39
p = "2020/03(E) (ifrs연결)"
parsed = p.split("(")
print(parsed[0])

#40
data = " SAMSUNG "
data = data.strip()
print(data)