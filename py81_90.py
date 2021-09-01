#81
scores = [1,2,3,4,5,6,7,8,9,10]
*a,b,c = scores
print(a)

#82
a,b,*c = scores
print(c)

#83
a,*b,c = scores
print(b)

#84
temp = {}
print(type(temp))

#85
ice = {"메로나":1000,"폴라포":1200,"빵빠레":1800}
print(ice)

#86
ice["죠스바"] =1200
ice["월드콘"] = 1500
print(ice)

#87
ice["메로나"] = 1300
print(ice)

#88
ice.pop("메로나")
print(ice)