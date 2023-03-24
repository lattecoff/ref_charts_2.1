# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from matplotlib.widgets import Cursor
import matplotlib.pyplot as plt
import numpy as np
import csv

y_shift_dumper = 10
y_shift_fan = 6
y_shift_comp = 4
y_shift_heater = 2 
y_shift_sf = 10
y_shift_df_vec = 30

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

df_vec = []

df_waittime = []
sf_runtime = []

''' Calculate dumper open time in frame. '''
def calc_sumtime_open_dumper():
    run_time = 0

    for i in dumper[2597:3649]:
        i = i +8
        
        if (i == 1):
            run_time = run_time + y_shift_dumper


    return (run_time /2)

''' Calculate compressor run time in frame. '''
def calc_sumtime_run_compressor():
    run_time = 0

    for i in comp[2597:3649]:
        i = i +4
        
        if (i == 1):
            run_time = run_time + y_shift_comp


    return (run_time /2)

''' Parsing CSV-file. '''
#with open('./logs/r509_comp_thaw.log', 'r') as csvfile:
#with open('./logs/common_mode.log', 'r') as csvfile:
#with open('./logs/run_comp_e2_error.log', 'r') as csvfile:
#with open('./logs/run_comp_6h_test3.log', 'r') as csvfile:
#with open('./logs/run_comp_6h_test2.log', 'r') as csvfile:
#with open('./logs/run_comp_6h.log', 'r') as csvfile:
#with open('./logs/serial_20230227_153054.txt', 'r') as csvfile:
#with open('./logs/r509_normal_mode_2.log', 'r') as csvfile:
#with open('./logs/r509_edefrost_2.log', 'r') as csvfile:
#with open('./logs/r510_dumper_thaw.log', 'r') as csvfile:
#with open('./logs/new_r510_normal_mode.log', 'r') as csvfile:
#with open('./logs/46new/dumper_thaw.log', 'r') as csvfile:
#with open('./logs/46new/r514_debug_restart.log', 'r') as csvfile:
#with open('./logs/46new/r514_debug_restart_continue.log', 'r') as csvfile:
#with open('./logs/46new/r514_normal_mode.log', 'r') as csvfile:
#with open('./logs/46new/r516_normal_mode_df1_16h.log', 'r') as csvfile:
#with open('./logs/46new/r516_sf.log', 'r') as csvfile:
with open('./logs/46new/r519_normal_mode_wait_H_45min.log', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=';')
    for row in lines:
        #x.append(row[0])
        tR.append(int(row[2]) /10)
        tF.append(int(row[3]) /10)
        tE.append(int(row[4]) /10)

        dumper.append(int(row[5]) - y_shift_dumper)
        fan.append(int(row[6]) - y_shift_fan)
        comp.append(int(row[7]) - y_shift_comp)
        heater.append(int(row[8]) - y_shift_heater)

        sf.append(int(row[12]) + y_shift_sf)

        df_vec.append(int(row[14]) + y_shift_df_vec)

        df_waittime.append(int(row[16]) /60.0/60.0)
        sf_runtime.append(int(row[19]) /60.0/60.0)

#print(df_waittime[960])



print("time open dumper: " + str(calc_sumtime_open_dumper()))
print("time run compressor: " + str(calc_sumtime_run_compressor()))

''' Set backgrownd. '''
plt.axes().set_facecolor('#273746')

''' Draw charts. '''
#plt.plot(x, y, color='g', linestyle='dashed', label="Weather Data")
plt.plot(tR, color='#138D75', linestyle='solid', label="tR")
plt.plot(tF, color='#2E86C1', linestyle='solid', label="tF")
plt.plot(tE, color='#CB4335', linestyle='solid', label="tE")

plt.plot(dumper, color='#F4D03F', linestyle='solid', label="D")
plt.plot(fan, color='#5DADE2', linestyle='solid', label="F")
plt.plot(comp, color='#2ECC71', linestyle='solid', label="C")
plt.plot(heater, color='#C0392B', linestyle='solid', label="H")

plt.plot(sf, color='#3498DB', linestyle='solid', label="SF", linewidth=3)

plt.plot(df_vec, color='#C0392B', linestyle='solid', label="DF Vector")

plt.plot(df_waittime, color='#5DADE2', linestyle='solid', label="DF WaitTime")
plt.plot(sf_runtime, color='#C39BD3', linestyle='solid', label="SF RunTime")



#plt.xlabel('x')

plt.ylabel('tR')
plt.ylabel('tF')
plt.ylabel('tE')
#plt.title('Interesting Graph\nCheck it out')
plt.legend()

''' Grid - ON. '''
plt.minorticks_on()
plt.grid(which='minor', color='#808B96', linestyle='-', linewidth=0.5)

#cursor = Cursor(plt, horizOn=True, vertOn=True, useblit=True, color='red', linewidth=2)
plt.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
