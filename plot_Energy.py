import matplotlib.pyplot as plt
import csv
import numpy as np
plt.rcParams.update({'font.size': 26})
plt.rcParams["figure.figsize"] = (11,7)
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
# plt.style.use('ggplot')
plt.grid(alpha=0.2)


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


plt.plot(energy_s, label='eNb1', linestyle='-')
plt.plot(energy_s2, label='eNb2', linestyle='--')
plt.plot()
plt.ylabel('Energy Consumption(J/s)')
plt.xlabel('Time(s)')

plt.legend(bbox_to_anchor=(0.75, 1.15), ncol=3, prop={'size': 26})
plt.tight_layout()
plt.show()

time_arr = [0]
energy_arr = [0]
with open('LogFiles/Sim2/energyfile1.csv', 'r') as csv_file:
    lines = csv.reader(csv_file)
    for line in lines:
        try:
            time_arr.append(float(line[0]))
            energy_arr.append(float(line[2]))
        except:
            continue

time_arr2 = [0]
energy_arr2 = [0]
with open('LogFiles/Sim2/energyfile2.csv', 'r') as csv_file:
    lines = csv.reader(csv_file)
    for line in lines:
        try:
            time_arr2.append(float(line[0]))
            energy_arr2.append(float(line[2]))
        except:
            continue

time_arr3 = [0]
energy_arr3 = [0]
with open('LogFiles/Sim2/energyfile3.csv', 'r') as csv_file:
    lines = csv.reader(csv_file)
    for line in lines:
        try:
            time_arr3.append(float(line[0]))
            energy_arr3.append(float(line[2]))
        except:
            continue

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

init_t = 0
sum_e = 0
energy_s3 = []
for t, e in zip(time_arr3, energy_arr3):
    sum_e += e
    if t > init_t+1:
        init_t += 1
        energy_s3.append(sum_e)
        sum_e = 0


plt.plot(energy_s, label='eNb1', linestyle='-')
plt.plot(energy_s2, label='eNb2', linestyle='--')
plt.plot(energy_s3, label='eNb3', linestyle='-.')
plt.plot()
plt.ylabel('Energy Consumption(J/s)')
plt.xlabel('Time(s)')

plt.legend(bbox_to_anchor=(0.75, 1.15), ncol=3, prop={'size': 26})
plt.grid(alpha=0.2)
plt.tight_layout()
plt.show()
