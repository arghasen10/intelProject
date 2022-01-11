from numpy.core.fromnumeric import sort
import pandas as pd

df = pd.read_csv('/home/argha/Documents/github/intelProject/LogFiles/Sim1/energyfile1.csv')
eng = df['DiffEnergy']/5
eng2 = eng.unique()
print(sort(eng2))