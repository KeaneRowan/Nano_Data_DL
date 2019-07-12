
import sys

print('Python: {}'.format(sys.version))

import pyabf
import numpy as np
import matplotlib.pyplot as plt
from xlwt import Workbook

filename = r'C:\Users\Elijah\Documents\NanoporeData\abfRaw\filtered_bessel8pole_500hz_19122010.abf'

abf = pyabf.ABF(filename)
print(abf)
# abf.headerLaunch() # display header information in a web browser

abf.setSweep(0)
print("sweep data (ADC):", abf.sweepY)
print("sweep command (DAC):", abf.sweepC)
print("sweep times (seconds):", abf.sweepX)

wb = Workbook()
destination = "19122010.xls"
sheet = wb.add_sheet(destination)

counter = 0
def dataPoints(begin, end):
    for n in range(begin, end):
        print(abf.sweepX[n], abf.sweepY[n])
        global counter
        sheet.write(counter, 0, float(abf.sweepX[n])), sheet.write(counter, 1, float(abf.sweepY[n]))
        counter += 1

dataPoints(243, 1421)
dataPoints(1851, 1874)
dataPoints(2115, 5614)
dataPoints(5922, 5957)
dataPoints(5963, 5969)
dataPoints(6001, 6781)
dataPoints(7135, 15835)
dataPoints(15990, 16010)
dataPoints(16043, 22583)
dataPoints(49738, 49748)
dataPoints(49888, 49952)
dataPoints(50092, 55022)
dataPoints(55292, 55837)
dataPoints(57030, 60024)
dataPoints(60237, 62981)
dataPoints(63223, 63391)
dataPoints(87093, 90495)
dataPoints(138470, 138740)
dataPoints(139004, 140457)
dataPoints(140521, 141102)
dataPoints(167504, 167791)
dataPoints(169331, 169348)
dataPoints(169468, 169473)
dataPoints(169515, 169685)
dataPoints(170225, 170232)
dataPoints(170428, 170560)
dataPoints(170910, 170915)
dataPoints(202263, 202266)
dataPoints(202382, 202391)
dataPoints(202395, 202826)
dataPoints(202874, 203014)
dataPoints(203052, 208391)
dataPoints(208416, 211993)
dataPoints(212005, 212022)
dataPoints(212330, 212430)
dataPoints(213261, 214305)
dataPoints(214512, 214774)
dataPoints(214865, 216127)
dataPoints(216127, 216149)
dataPoints(241484, 241515)
dataPoints(241696, 241814)
dataPoints(241855, 241880)
dataPoints(296335, 296340)

#print(counter)



# with open('19213006.txt', 'w') as f:
#     for item in abf.sweepY:
#         f.write("%s\n" % item)

plt.figure(figsize=(8, 5))
plt.title("Nanopore file:" + filename)
plt.ylabel(abf.sweepLabelY)
plt.xlabel(abf.sweepLabelX)
plt.axis([0, 300, -150, 100])
plt.plot(abf.sweepX, abf.sweepY)
#plt.savefig(filename + '.png')
#plt.show()

wb.save(destination)