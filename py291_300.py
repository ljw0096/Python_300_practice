#291
"""f = open("C:/Users/ljw00/OneDrive/바탕 화면/매수종목1.txt", mode='wt', encoding="utf-8")
f.write("005930\n")
f.write("005380\n")
f.write("035420\n")
f.close()"""

#292
"""f = open("C:/Users/ljw00/OneDrive/바탕 화면/매수종목2.txt", mode='wt', encoding="utf-8")
f.write("005930 삼성전자\n")
f.write("005380 현대차\n")
f.write("035420 NAVER\n")
f.close()"""

#294

f = open("C:/Users/ljw00/OneDrive/바탕 화면/매수종목1.txt",mode="r",encoding="utf-8")
lines = f.readlines()

codes = []
for line in lines:
    code = line.strip()
    codes.append(code)
print(codes)

f.close()

f = open("C:/Users/ljw00/OneDrive/바탕 화면/매수종목2.txt",mode="r",encoding="utf-8")
lines = f.readlines()

codes = {}
for line in lines:
    line.strip()
    splited = line.split(" ")
    code = splited[0]
    name = splited[1]
    codes[code] = name

print(codes)

f.close()