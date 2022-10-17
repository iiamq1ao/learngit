vertices = []
v = []
f = []
count = 0


dir = "nmap-os-db.txt"
for line in open(dir, "r"):

    values = line.split()

    if len(values)!=0 and values[0]=="Fingerprint":
        v.append(values)

    if len(values)!=0 and values[0]=="fingerprint":
        v.append(values)


print(len(v))

for i in range(len(v)):
    for j in range(len(v[i])):
        if ("switch" in v[i][j]) :
            count = count + 1
            f.append(v[i][j])
            break
print('switch',count)
#print(f)


