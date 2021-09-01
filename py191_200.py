#191
data=[
    [2000,3050,2050,1980],
    [7500,2050,2050,1980],
    [15450,15050,15550,14900]
]
result = []
rows=[]
for row in data:
    for col in row:
        rows.append(col*1.00014)
    result.append(rows)
    rows=[]
print(result)

#195
ohlc=[
    ["open","high","low","close"],
    [100,110,70,100],
    [200,210,180,190],
    [300,310,300,310]]

for row in ohlc[1:]:
    close = row[3]
    if(close>150):
        print(close)

for row in ohlc[1:]:
    if(row[3]>=row[0]):
        print(row[3])

volatility = []

for row in ohlc[1:]:
    volatility.append(row[1]-row[2])
print(volatility)

for row in ohlc[1:]:
    if(row[3]>row[0]):
        print(row[1]-row[2])

sum=0
for row in ohlc[1:]:
    sum+=row[0]-row[3]
print(sum)