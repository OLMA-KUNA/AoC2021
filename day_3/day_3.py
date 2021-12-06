
f=open('input.txt', 'r+')
my_data = f.read().splitlines()
f.close()

# Part one
gamma = ''
epsilon =''

for i in range(0,len(my_data[0])-1):
	counter_1 = 0
	counter_0 = 0
    for j in range(0,len(my_data)):
		if my_data[j][i]=='1':
			counter_1+=1
		else:
			counter_0+=1
	if counter_1>counter_0:
		gamma+='1'
		epsilon+='0'
	else:
		gamma+='0'
		epsilon+='1'

result1 = int(gamma,2) * int(epsilon,2)
print(result1)

# Part 2
oxygen = my_data
co2 = my_data

for i in range(0,len(oxygen[0])-1):
    counter_1 = 0
    counter_0 = 0
    oxygen1 = []
    oxygen0 = []
    for j in range(0,len(oxygen)):
        if oxygen[j][i]=='1':
            counter_1+=1
            oxygen1.append(oxygen[j])
        else:
            counter_0+=1
            oxygen0.append(oxygen[j])
    if counter_1<counter_0:
            oxygen = oxygen0
    else:
            oxygen = oxygen1
		
for i in range(0,len(co2[0])-1):
    counter_1 = 0
    counter_0 = 0
    co_1 = []
    co_0 = []
    for j in range(0,len(co2)):
        if co2[j][i]=='1':
            counter_1+=1
            co_1.append(co2[j])
        else:
            counter_0+=1
            co_0.append(co2[j])
    if counter_1 < counter_0:
            co2 = co_1
    else:
            co2 = co_0
		

result2 = int(oxygen[0],2) * int(co2[0],2)
print(result2)