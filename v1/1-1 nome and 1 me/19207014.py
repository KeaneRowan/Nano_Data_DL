
import sys

print('Python: {}'.format(sys.version))

import pyabf
import numpy as np
import matplotlib.pyplot as plt
from xlwt import Workbook

filename = r'C:\Users\Elijah\Documents\NanoporeData\abfRaw\filtered_bessel8pole_500hz_19207014.abf'

abf = pyabf.ABF(filename)
print(abf)
# abf.headerLaunch() # display header information in a web browser

abf.setSweep(0)
print("sweep data (ADC):", abf.sweepY)
print("sweep command (DAC):", abf.sweepC)
print("sweep times (seconds):", abf.sweepX)

wb = Workbook()
destination = "19207014.xls"
sheet = wb.add_sheet(destination)

counter = 0
def dataPoints(begin, end):
    for n in range(begin, end):
        print(abf.sweepX[n], abf.sweepY[n])
        global counter
        sheet.write(counter, 0, float(abf.sweepX[n])), sheet.write(counter, 1, float(abf.sweepY[n]))
        counter += 1

dataPoints(5239, 5787)
dataPoints(30172, 35021)
dataPoints(54328, 54536)
dataPoints(54900, 55521)
dataPoints(55618, 55632)
dataPoints(55730, 55734)
dataPoints(55762, 55766)
dataPoints(56410, 56414)
dataPoints(56447, 57919)
dataPoints(58779, 58845)
dataPoints(79555, 79583)
dataPoints(101413, 101432)
dataPoints(101646, 101649)
dataPoints(102732, 104062)
dataPoints(104121, 107763)
dataPoints(108029, 108037)
dataPoints(108377, 108671)
dataPoints(108740, 108806)
dataPoints(128896, 128902)
dataPoints(129669, 132059)
dataPoints(157640, 157777)
dataPoints(157965, 157981)
dataPoints(158000, 158013)
dataPoints(158074, 159037)
dataPoints(159162, 159175)
dataPoints(199057, 199064)
dataPoints(199165, 204332)
dataPoints(204372, 205701)
dataPoints(225604, 225696)
dataPoints(225766, 226717)
dataPoints(226964, 227020)
dataPoints(227075, 227115)
dataPoints(247353, 247464)
dataPoints(247721, 254612)
dataPoints(254698, 254708)
dataPoints(254715, 254728)
dataPoints(275258, 275264)
dataPoints(297062, 297068)
dataPoints(297335, 297343)

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