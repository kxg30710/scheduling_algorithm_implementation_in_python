import numpy

index = 0
process = []
input_process = []
f = open("input_1.txt", "r")
for x in f:
  data = x.split()
  process.append(data)

for x in process[1:]:
    input_process.append(x)

input_process.sort(key=lambda col : col[1])

for x,y in process: 
    print(x,y)

waiting_time = []
w = 0
sjf_process = []
for i in range(len(input_process)):
   sjf_process.append(input_process[i][0])

waiting_time.append(w)

for i in range(len(input_process)-1):
    w = w + int(input_process[i][1])
    waiting_time.append(w)

print("SJF order of execution")
print(sjf_process)
print(waiting_time)
   
for i in range(len(sjf_process)):
    print("waiting time of " + sjf_process[i] + " is : " + str(waiting_time[i]))

Average_waiting_time = sum(waiting_time)/len(waiting_time)

print("Average waiting time :" + str(Average_waiting_time))



