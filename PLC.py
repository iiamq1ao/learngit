vertices = [[] for ii in range(5680)]
v = []
f = []
count = 0


dir = "nmap-os-db.txt"

for line in open(dir, "r"):

    values = line.split()

   # v.append(values)

    if len(values)!=0 and values[0]=="Fingerprint":
        v.append(values)

    #if len(values)!=0 and values[0]=="fingerprint":
     #   v.append(values)
     
#print(v)

#k = 0

#for i in range(len(v)):
    
 #   if len(v[i])==0:
       
#        k  =  k + 1
    
#    else:
#        for j in range(len(v[i])):
#            vertices[k].append(v[i][j])
#print(vertices)

#count = 0 
#plc =[]
for i in range(len(v)):
    for j in range(len(v[i])):
        if ("PLC" in v[i][j]) or ("Programmable" in v[i][j]) or ("programmable" in v[i][j]):
            count = count + 1
            f.append(v[i][j])
            #plc.append(vertices[i][j])
            #if vertices[i] == vertices[i-1]:
            #    del vertices[i]
            #    count = count -1
            #log = open("plc.txt",mode="a",encoding="utf-8")
            #print(vertices[i],file=log)
            print(v[i])
            log = open("plcfinal.txt",mode="a",encoding="utf-8")
            print(v[i],file=log)
            break
#log.close()
print('PLC数量:',count)


#count_new = 0
#siemens = []


#print("siemens:",count_new)

       
