


process = []
input_process = []
f = open("input_1.txt", "r")
for x in f:
  data = x.split()
  process.append(data)

for x in process[1:]:
    input_process.append(x)



for x,y in process: 
    print(x,y)

waiting_time = []
w = 0
fcfs_process = []
for i in range(len(input_process)):
   fcfs_process.append(input_process[i][0])

waiting_time.append(w)

for i in range(len(input_process)-1):
    w = w + int(input_process[i][1])
    waiting_time.append(w)

print("FCFS order of execution")
print(fcfs_process)
print(waiting_time)
   
for i in range(len(fcfs_process)):
    print("waiting time of " + fcfs_process[i] + " is : " + str(waiting_time[i]))

Average_waiting_time = sum(waiting_time)/len(waiting_time)

print("Average waiting time :" + str(Average_waiting_time))



