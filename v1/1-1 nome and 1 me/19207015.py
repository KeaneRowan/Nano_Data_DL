
import sys

print('Python: {}'.format(sys.version))

import pyabf
import numpy as np
import matplotlib.pyplot as plt
from xlwt import Workbook

filename = r'C:\Users\Elijah\Documents\NanoporeData\abfRaw\filtered_bessel8pole_500hz_19207015.abf'

abf = pyabf.ABF(filename)
print(abf)
# abf.headerLaunch() # display header information in a web browser

abf.setSweep(0)
print("sweep data (ADC):", abf.sweepY)
print("sweep command (DAC):", abf.sweepC)
print("sweep times (seconds):", abf.sweepX)

wb = Workbook()
destination = "19207015.xls"
sheet = wb.add_sheet(destination)

counter = 0
def dataPoints(begin, end):
    for n in range(begin, end):
        print(abf.sweepX[n], abf.sweepY[n])
        global counter
        sheet.write(counter, 0, float(abf.sweepX[n])), sheet.write(counter, 1, float(abf.sweepY[n]))
        counter += 1

dataPoints(6662, 6668)
dataPoints(6776, 6781)
dataPoints(6845, 6849)
dataPoints(7366, 15066)
dataPoints(15101, 17378)
dataPoints(17834, 17843)
dataPoints(18190, 18212)
dataPoints(18631, 18635)
dataPoints(18954, 18964)
dataPoints(19110, 24465)
dataPoints(24521, 24585)
dataPoints(24590, 25149)
dataPoints(25240, 25414)
dataPoints(25490, 25519)
dataPoints(25604, 25611)
dataPoints(25694, 25698)
dataPoints(44971, 45021)
dataPoints(66060, 66150)
dataPoints(80232, 80247)
dataPoints(80394, 80405)
dataPoints(80540, 80684)
dataPoints(81071, 81080)
dataPoints(81486, 81489)
dataPoints(81493, 81501)
dataPoints(81569, 81572)
dataPoints(131457, 132954)
dataPoints(151617, 151732)
dataPoints(193492, 193708)
dataPoints(194097, 194105)
dataPoints(194182, 194188)
dataPoints(194364, 194395)
dataPoints(194745, 195029)
dataPoints(195166, 195622)
dataPoints(195677, 201524)
dataPoints(201541, 201607)
dataPoints(201631, 202325)
dataPoints(202692, 202695)
dataPoints(202751, 202770)
dataPoints(202989, 203031)
dataPoints(203088, 210347)
dataPoints(210617, 210624)
dataPoints(210671, 210675)
dataPoints(211552, 211556)
dataPoints(211993, 213885)
dataPoints(213928, 213936)
dataPoints(214117, 214129)
dataPoints(214176, 214798)
dataPoints(215016, 218003)
dataPoints(218656, 218660)
dataPoints(219194, 220434)
dataPoints(221085, 221094)
dataPoints(221205, 221216)
dataPoints(221326, 223162)
dataPoints(262203, 262302)
dataPoints(281105, 288561)
dataPoints(288721, 291823)
dataPoints(292261, 292705)
dataPoints(292715, 292729)
dataPoints(293259, 293267)
dataPoints(293584, 294481)
dataPoints(294504, 294573)
dataPoints(294750, 295065)
dataPoints(295450, 297124)

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