import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 30})
plt.rcParams["figure.figsize"] = (11, 7)
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"

all_idle = [4.1, 7.4]
all_tx = [5.8, 2.6]
all_ctrl = [0.32, 0.56]
all_data = [0.007, 0.05]
N = 2
ind = np.arange(N)
width = 0.25

bar1 = plt.bar(ind, all_idle, width / 2, color='r', label='IDLE')
bar2 = plt.bar(ind + width / 2, all_tx, width / 2, color='g', label='TX')
bar3 = plt.bar(ind + width, all_ctrl, width / 2, color='b', label='RX_CTRL')
bar4 = plt.bar(ind + width * 3 / 2, all_data, width / 2, color='y', label='RX_DATA')
plt.ylabel('Time(s)')

plt.xticks(ind + 3 * width / 4, ['eNB1', 'eNB2'])
# plt.legend((bar1, bar2, bar3, bar4), ('IDLE', 'TX', 'RX_CTRL', 'RX_DATA'))
plt.grid()

plt.legend(bbox_to_anchor=(0.65, 1.35), ncol=2, prop={'size': 26})
plt.tight_layout()
plt.show()
