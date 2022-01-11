import matplotlib.pyplot as plt
import csv
import numpy as np
plt.rcParams.update({'font.size': 18})
plt.rcParams["figure.figsize"] = (11,7)
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
# plt.style.use('ggplot')
plt.grid(alpha=0.2)
plt.tight_layout()

time_arr = [0]
energy_arr = [0]
with open('LogFiles/Sim1/energyfile1.csv', 'r') as csv_file:
    lines = csv.reader(csv_file)
    for line in lines:
        try:
            time_arr.append(float(line[0]))
            energy_arr.append(float(line[2]))
        except:
            continue
# plt.plot(time_arr, energy_arr, label='EnB1')
# plt.show()

time_arr2 = [0]
energy_arr2 = [0]
with open('LogFiles/Sim1/energyfile2.csv', 'r') as csv_file:
    lines = csv.reader(csv_file)
    for line in lines:
        try:
            time_arr2.append(float(line[0]))
            energy_arr2.append(float(line[2]))
        except:
            continue
# plt.plot(time_arr, energy_arr,label='enb2', color='tab:red')
# plt.show()


# plt.plot(time_arr2, bits_arr)
# plt.show()

init_t = 0
sum_e = 0
energy_s = []
for t, e in zip(time_arr, energy_arr):
    sum_e += e
    if t > init_t+1:
        init_t += 1
        energy_s.append(sum_e)
        sum_e = 0

init_t = 0
sum_e = 0
energy_s2 = []

for t, e in zip(time_arr2, energy_arr2):
    sum_e += e
    if t > init_t+1:
        init_t += 1
        energy_s2.append(sum_e)
        sum_e = 0




# plt.scatter(hand1, yhand1, marker='^', color='tab:blue')
# plt.scatter(hand2, yhand2, marker='^', color='tab:orange')
plt.plot(energy_s, label='eNb1')
plt.plot(energy_s2, label='eNb2')
plt.plot()
# plt.scatter(hand1, red_star, marker='^', label='eNb2 to eNb1')
# plt.scatter(hand2, blue_star, marker='o', label='eNb1 to eNb2')
plt.ylabel('Energy Consumption(J/s)')
plt.xlabel('Time(s)')
plt.legend()
plt.show()
