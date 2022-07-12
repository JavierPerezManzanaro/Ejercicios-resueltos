dic = {}

for i in range(0, 70):
    dic2 = {'nombre_'+str(i+1): i+1}
    dic.update(dic2)


for key in dic:
    print(key, '=', dic[key])
