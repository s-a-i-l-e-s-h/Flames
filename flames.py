emplis = []
emplis2 = []

a = input("Enter the Name: ")
b = input("Enter your Crush Name: ")

a = a.strip()
b = b.strip()

for i in a:
    if i != ' ':
        #print(i)
        emplis.append(i)

for j in b:
    if j != ' ':
        #print(j)
        emplis2.append(j)

#print(emplis)
#print(emplis2)

emplis_copy = emplis.copy()
emplis2_copy = emplis2.copy()

for k in emplis_copy:
    if k in emplis2:
        emplis.remove(k)
        emplis2.remove(k)

#print(emplis)
#print(emplis2)

combined_list = emplis + emplis2
#print(combined_list)

vantom = len(combined_list)
#print(vantom)

flames = ['Friends','Lovers','Affection','Marriage','Enemy','Sister']

for i in range(len(flames) - 1):
    count = vantom % len(flames)
    flames = flames[count:] + flames[:count]

print("Relationalship Result :",flames[0])
