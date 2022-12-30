d = []
print("Enter the number of process: ")
n = int(input())
print("Enter the burst time of the processes: \n")
for i in range(n):
    d.append(list(input().split()))
print(d)
duration = []
tat = []
arrivalT = []
avgtat = 0
duration.insert(0, d[0][2])
tat.insert(0, d[0][2])
for i in range(1, len(d)):
    #duration.insert(i, duration[i-1]+d[i][2])
    duration.insert(i, d[i][2])
    #tat.insert(i, duration[i]+d[i][2])
    arrivalT.insert(i - 1, d[i][3])
    tat.insert(i, duration[i]+tat[i-1]-arrivalT[i])
    avgtat += tat[i]
avgtat = float(avgtat)/n
print("\n")
print("Seq.No.  ProcessName  Timeline  Turnaround")
for i in range(0, n):
    print(f'{str(d[i][0])}\t\t{str(d[i][1])}\t\t\t{str(tat[i])}')
print(f'A.T.T = {avgtat}')