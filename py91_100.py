#91
ice = {"melon":[300,20],"bibi":[400,3],"jaws":[250,100]}
print(ice)

#92
print(ice["melon"][0])

#93
print(ice["melon"][1])

#94
ice["world"] = [500,7]
print(ice)

#95
name_list = list(ice.keys())
print(name_list)

#96
val_list = list(ice.values())
print(val_list)

#97
icecream = {"tank":1300,"pola":1200,"pab":1800}
price_list = list(icecream.values())
print(sum(price_list))

#98
new_product={"pat":2700,"amat":1000}
icecream.update(new_product)
print(icecream)

#99
keys=("apple","pear","peach")
vals=(300,250,400)

result = dict(zip(keys,vals))
print(result)

#100
data = ['09/05','09/06','09/07','09/08','09/09']
close_price=[10500,10300,10100,10800,11000]
close_table = dict(zip(data,close_price))
print(close_table)