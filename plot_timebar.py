import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size': 30})
plt.rcParams["figure.figsize"] = (11,7)
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"

rxctrl = []
rxctrl1 = []
rxctrl2 = []

idle, idle1, idle2 = [], [], []
data, data1, data2 = [], [], []
tx, tx1, tx2 = [], [], []
with open('/home/argha/Desktop/ns3-mmwave/my_output_file', 'r') as file:
    lines = file.readlines()
    for line in lines:
        word = line.split()
        if word[0] == 'idle':
            if word[-1] == '0':
                idle.append(float(word[1]))
            elif word[-1] == '1':
                idle1.append(float(word[1]))
            elif word[-1] == '2':
                idle2.append(float(word[1]))
        if word[0] == 'rxctrl_time':
            if word[-1] == '0':
                rxctrl.append(float(word[1]))
            elif word[-1] == '1':
                rxctrl1.append(float(word[1]))
            elif word[-1] == '2':
                rxctrl2.append(float(word[1]))
        if word[0] == 'data_time':
            if word[-1] == '0':
                data.append(float(word[1]))
            elif word[-1] == '1':
                data1.append(float(word[1]))
            elif word[-1] == '2':
                data2.append(float(word[1]))
        if word[0] == 'tx_time':
            if word[-1] == '0':
                tx.append(float(word[1]))
            elif word[-1] == '1':
                tx1.append(float(word[1]))
            elif word[-1] == '2':
                tx2.append(float(word[1]))


all_idle = (idle[-1], idle1[-1], idle2[-1])
all_ctrl = (rxctrl[-1], rxctrl1[-1], rxctrl2[-1])
all_data = (data[-1], data1[-1], data2[-1])
all_tx = (tx[-1], tx1[-1], tx2[-1])



N = 3
ind = np.arange(N)
width = 0.25

bar1 = plt.bar(ind, all_idle, width/2, color='r', label='IDLE')
bar2 = plt.bar(ind + width/2, all_tx, width/2, color='g', label='TX')
bar3 = plt.bar(ind + width , all_ctrl, width/2, color='b', label='RX_CTRL')
bar4 = plt.bar(ind + width * 3/2, all_data, width/2, color='y', label='RX_DATA')
plt.ylabel('Time(s)')

plt.xticks(ind + 3*width/4, ['eNB1', 'eNB2', 'eNB3'])
# plt.legend((bar1, bar2, bar3, bar4), ('IDLE', 'TX', 'RX_CTRL', 'RX_DATA'))
plt.grid()

plt.legend(bbox_to_anchor=(0.65, 1.35), ncol=2, prop={'size': 26})
plt.tight_layout()
plt.show()
