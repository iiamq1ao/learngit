vertices = [[] for ii in range(5680)]
v = []
f = []
count = 0


dir = "nmap-os-db.txt"

for line in open(dir, "r"):

    values = line.split()

    v.append(values)

#print(v)

k = 0

for i in range(len(v)):

    if len(v[i])==0:
        k = k + 1

    else:
        for j in range(len(v[i])):
            vertices[k].append(v[i][j])


count = 0
router = []
for i in range(len(vertices)):
    for j in range(len(vertices[i])):
        if ("router" in vertices[i][j]) or ("Router" in vertices[i][j]) or ("ROUTER" in vertices[i][j]):
            count = count + 1
            router.append(vertices[i])
#            print(router)
            break
            
             
print("router:",count)
#print(router)

count_new = 0
huawei = []

for i in range(len(router)):
    for j in range(len(router[i])):
        if ("huawei" in router[i][j]) or ("Huawei" in router[i][j]) or ("HUAWEI"in router[i][j]) or ("HUAwei" in router[i][j]) :
            count_new = count_new + 1
            huawei.append(router[i])
            #break

print("huawei:",count_new)


count_h3c=0
h3c = []
for i in range (len(router)):
    for j in range(len(router[i])):
        if ("H3C" in router[i][j]): 
            count_h3c=count_h3c+1
            h3c.append(router[i])
            #break
print("H3C:",count_h3c)
"""
count_ab=0
ab = []
for i in range (len(router)):
    for j in range(len(router[i])):
        if ("Allen" in router[i][j]):
            count_ab=count_ab+1
            ab.append(router[i])
            #break
print("Allen Bradley:",count_ab)
"""
