# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import matplotlib.pyplot as plt
import numpy as np
import csv

x = []
y = []

tR = []
tF = []
tE = []

dumper = []
fan = []
comp = []
heater = []

sf = []

df_waittime = []
sf_runtime = []

with open('./logs/20230216.log', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=';')
    for row in lines:
        #x.append(row[0])
        tR.append(int(row[2]) /10)
        tF.append(int(row[3]) /10)
        tE.append(int(row[4]) /10)

        dumper.append(int(row[5]) -8)
        fan.append(int(row[6]) -6)
        comp.append(int(row[7]) -4)
        heater.append(int(row[8]) -2)

        sf.append(int(row[12]) +10)

        df_waittime.append(int(row[16]) /60.0/60.0)
        sf_runtime.append(int(row[19]) /60.0/60.0)

print(df_waittime[960])

plt.axes().set_facecolor('#273746')
#plt.plot(x, y, color='g', linestyle='dashed', label="Weather Data")
plt.plot(tR, color='#138D75', linestyle='solid', label="tR")
plt.plot(tF, color='#2E86C1', linestyle='solid', label="tF")
plt.plot(tE, color='#CB4335', linestyle='solid', label="tE")

plt.plot(dumper, color='#F4D03F', linestyle='solid', label="D")
plt.plot(fan, color='#5DADE2', linestyle='solid', label="F")
plt.plot(comp, color='#2ECC71', linestyle='solid', label="C")
plt.plot(heater, color='#C0392B', linestyle='solid', label="H")

plt.plot(sf, color='#3498DB', linestyle='solid', label="SF", linewidth=3)

plt.plot(df_waittime, color='#5DADE2', linestyle='solid', label="DF WaitTime")
plt.plot(sf_runtime, color='#C39BD3', linestyle='solid', label="SF RunTime")

#plt.xlabel('x')

plt.ylabel('tR')
plt.ylabel('tF')
plt.ylabel('tE')
#plt.title('Interesting Graph\nCheck it out')
plt.legend()

plt.minorticks_on()
plt.grid(which='minor', color='#808B96', linestyle='-', linewidth=0.5)

plt.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
