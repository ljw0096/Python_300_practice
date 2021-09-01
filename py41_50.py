#41
ticker = "btc_krw"
ticker_upper = ticker.upper()
print(ticker_upper)

#42
ticker_lower = ticker_upper.lower()
print(ticker_lower)

#43
s = 'hello'
s = s.capitalize
print(s)

#44
f_name = "report.xlsx"
print(f_name.endswith(".xlsx"))

#45
f_name2 = "rep.xls"
print(f_name.endswith((".xlsx",".xls")))

#46
f_name = "2020_report.xlsx"
print(f_name.startswith("2020"))

#47
a="hello world"
a=a.split(" ")
print(a[0],a[1])
