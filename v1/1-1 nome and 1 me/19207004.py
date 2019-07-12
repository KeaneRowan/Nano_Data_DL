
import sys

print('Python: {}'.format(sys.version))

import pyabf
import numpy as np
import matplotlib.pyplot as plt
from xlwt import Workbook

filename = r'C:\Users\Elijah\Documents\NanoporeData\abfRaw\filtered_bessel8pole_500hz_19207004.abf'

abf = pyabf.ABF(filename)
print(abf)
# abf.headerLaunch() # display header information in a web browser

abf.setSweep(0)
print("sweep data (ADC):", abf.sweepY)
print("sweep command (DAC):", abf.sweepC)
print("sweep times (seconds):", abf.sweepX)

wb = Workbook()
destination = "19207004.xls"
sheet = wb.add_sheet(destination)

counter = 0
def dataPoints(begin, end):
    for n in range(begin, end):
        print(abf.sweepX[n], abf.sweepY[n])
        global counter
        sheet.write(counter, 0, float(abf.sweepX[n])), sheet.write(counter, 1, float(abf.sweepY[n]))
        counter += 1

dataPoints(4612.60)
dataPoints(4732.55)
dataPoints(4784.25)
dataPoints(4825.05)
dataPoints(6871.55)
dataPoints(6914.20)
dataPoints(6955.95)
dataPoints(11267.30)
dataPoints(52069.30)
dataPoints(53272.25)
dataPoints(53412.25)
dataPoints(54292.55)
dataPoints(54426.50)
dataPoints(63599.60)
dataPoints(63976.00)
dataPoints(64931.00)
dataPoints(68693.70)
dataPoints(68707.65)
dataPoints(70368.85)
dataPoints(72244.75)
dataPoints(74229.65)
dataPoints(93129.80)
dataPoints(111804.10)
dataPoints(111826.70)
dataPoints(112536.30)
dataPoints(132281.30)
dataPoints(133552.40)
dataPoints(134514.90)
dataPoints(135128.60)
dataPoints(135864.70)
dataPoints(138475.20)
dataPoints(138980.50)
dataPoints(143258.30)
dataPoints(143406.30)
dataPoints(143743.60)
dataPoints(161237.00)
dataPoints(161267.70)
dataPoints(161451.40)
dataPoints(161495.40)
dataPoints(163485.30)
dataPoints(163524.50)
dataPoints(182720.30)
dataPoints(185173.20)
dataPoints(187073.60)
dataPoints(187201.90)
dataPoints(187217.80)
dataPoints(187499.50)
dataPoints(187719.70)
dataPoints(188009.90)
dataPoints(207458.00)
dataPoints(209948.90)
dataPoints(212947.60)
dataPoints(231605.90)
dataPoints(231710.60)
dataPoints(231791.00)
dataPoints(232893.10)
dataPoints(254287.50)
dataPoints(254363.40)
dataPoints(255250.70)
dataPoints(255417.40)
dataPoints(256263.60)
dataPoints(277066.20)
dataPoints(277513.00)
dataPoints(278573.00)
dataPoints(280480.80)
dataPoints(299492.10)

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