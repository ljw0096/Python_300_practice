#151
ls = [3,-20,-3,44]
for v in ls:
    if(v<0):
        print(v)

#152
ls = [3,100,23,44]
for v in ls:
    if v%3==0:
        print(v)

#153
ls = [13,21,12,14,30,18]
for v in ls:
    if (v%3==0)and(v<20):
        print(v)

#154
ls=["I","study","python","languange","!"]
for v in ls:
    if(len(v)>3):
        print(v)

#155
ls=["A","b","c","D"]
for v in ls:
    if v.isupper():
        print(v)

#156
for v in ls:
    if v.islower():
        print(v)

#157
ls = ['dog','cat','parrot']
for v in ls:
    print(v.capitalize())

#158
ls=['hello.py','ex01.py','intro.hwp']
for v in ls:
    print(v.split(".")[0])

#159
ls=['intra.h','intra.c','define.h','run.py']
for v in ls:
    file_type = v.split(".")[1]
    if file_type=='h':
        print(v)

#160
for v in ls:
    file_type = v.split(".")[1]
    if (file_type=="h")or(file_type=="c"):
        print(v)