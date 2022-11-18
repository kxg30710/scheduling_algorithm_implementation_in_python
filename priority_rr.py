from sys import argv
import numpy
process = []
input_process = []
f = open("input.txt", "r")
for x in f:
  data = x.split()
  process.append(data)

for x in process[1:]:
    input_process.append(x)

input_process.sort(key=lambda col : col[2])
priority_queue = []
print("Input process")

for x,y,z in process:
    print(x,y,z)
    
for x,y,z in input_process:
    y = int(y)
    z = int(z)
    priority_queue.append(z)
   



def find_count(val):
    return priority_queue.count(val)

exec_queue = []
wait_time = []
w_time = 0
wait_time.append(w_time)
rr_process = []
rr_bt=[]

def round_robin(rr_process,rr_bt,q,w_time):
    c_count = 0
    
    for i in range(len(rr_process)):
        if rr_bt[i] != 0:
            exec_queue.append(rr_process[i])
            if(int(rr_bt[i]) >= q):
                w_time = w_time + q
                wait_time.append(w_time)
                rr_bt[i] = int(rr_bt[i])-q
            else:
                w_time = w_time+int(rr_bt[i])
                wait_time.append(w_time)
                rr_bt[i]=int(rr_bt[i])-int(rr_bt[i])
    for i in range(len(rr_process)):
        if(int(rr_bt[i]) != 0):
            c_count = c_count+1
    if c_count != 0:
        round_robin(rr_process,rr_bt,q,w_time)
    


rows = len(input_process)
i = 0
while(i<rows):
    priority = int(input_process[i][2])
    count = find_count(priority)
    if count == 1:
        exec_queue.append(input_process[i][0])
        w_time = w_time+int(input_process[i][1])
        wait_time.append(w_time)
        i = i+1
    if count > 1:
        rr_process.clear()
        rr_bt.clear()
        while(count != 0):
            rr_proces
            s.append(input_process[i][0])
            rr_bt.append(input_process[i][1])
            count = count - 1
            i = i+1
        round_robin(rr_process,rr_bt,2,w_time)
        w_time = wait_time[-1]

print("Gantt chart")
print(exec_queue)
print(wait_time)

#for i in range(len(exec_queue)):



indexes = []
waiting_time = []
for x in range(len(input_process)):
    indexes.clear()
    pid = input_process[x][0]
    for y in range(len(exec_queue)):
        if pid == exec_queue[y]:
            indexes.append(y)
    length = len(indexes)
    if(length == 1):
        waiting_time.append(wait_time[indexes[0]])
    else:
        temp = wait_time[indexes[-1]]
        temp1 = 0
        for i in range(len(indexes)-1):
            temp1 = temp1 + (wait_time[indexes[i]+1]- wait_time[indexes[i]])
        temp = temp - temp1
        waiting_time.append(temp)

process = []

for i in range(len(input_process)):
    process.append(input_process[i][0])

print("Waiting time")
print(process)
print(waiting_time)    

average_waiting_time = sum(waiting_time)/len(process)
print("Average Waiting time")
print(average_waiting_time)





    

