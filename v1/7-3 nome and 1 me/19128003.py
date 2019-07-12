




import sys
import xlwt
from xlwt import Workbook

#wb = Workbook()
#outfile = "19122007output"
#sheet = wb.add_sheet(outfile)

print('Python: {}'.format(sys.version))

import pyabf
import numpy as np
import matplotlib.pyplot as plt

filename = r'C:\Users\Elijah\Documents\NanoporeData\abfRaw\filtered_bessel8pole_500hz_19128003.abf'

abf = pyabf.ABF(filename)
print(abf)
# abf.headerLaunch() # display header information in a web browser

abf.setSweep(0)
print("sweep data (ADC):", abf.sweepY)
print("sweep command (DAC):", abf.sweepC)
print("sweep times (seconds):", abf.sweepX)


counter = 0
def dataPoints(begin, end):
    for n in range(begin, end):
        print(abf.sweepX[n], abf.sweepY[n])
        #sheet.write(counter, 0, str(abf.sweepX[n])), sheet.write(counter, 1, str(abf.sweepY[n]))
        global counter
        counter += 1

dataPoints(23147, 37409)
dataPoints(37698, 37918)
dataPoints(38065, 38069)
dataPoints(38162, 38252)
dataPoints(38490, 38506)
dataPoints(39073, 39502)
dataPoints(39562, 44364)
dataPoints(44549, 44577)
dataPoints(44638, 45625)
dataPoints(66590, 67170)
dataPoints(67351, 72347)
dataPoints(72348, 73622)
dataPoints(73637, 73644)
dataPoints(73670, 74496)
dataPoints(74516, 75931)
dataPoints(76142, 76154)
dataPoints(76182, 76204)
dataPoints(76271, 76368)
dataPoints(76555, 78991)
dataPoints(79118, 79201)
dataPoints(79365, 79490)
dataPoints(79786, 79831)
dataPoints(120939, 124900)
dataPoints(125128, 126616)
dataPoints(126778, 126782)
dataPoints(126989, 127055)
dataPoints(127203, 127218)
dataPoints(127387, 128371)
dataPoints(128445, 129711)
dataPoints(129725, 130238)
dataPoints(130540, 138582)
dataPoints(138590, 151291)
dataPoints(151352, 151457)
dataPoints(151499, 151504)
dataPoints(151512, 151666)
dataPoints(152264, 152267)
dataPoints(152531, 152535)
dataPoints(152576, 153649)
dataPoints(153845, 153853)
dataPoints(154115, 154774)
dataPoints(175874, 175928)
dataPoints(176322, 177887)
dataPoints(199074, 199079)
dataPoints(199097, 199475)
dataPoints(199493, 200009)
dataPoints(200373, 207916)
dataPoints(208206, 208297)
dataPoints(208321, 208342)
dataPoints(208386, 209180)
dataPoints(230527, 230541)
dataPoints(230911, 230935)
dataPoints(268727, 268743)
dataPoints(268752, 268838)
dataPoints(289493, 289522)
dataPoints(289664, 290799)
dataPoints(290803, 290810)
dataPoints(290823, 291690)
dataPoints(291922, 293521)

print(counter)

# with open('19213006.txt', 'w') as f:
#     for item in abf.sweepY:
#         f.write("%s\n" % item)

# plt.figure(figsize=(8, 5))
# #plt.title("Nanopore file:" + filename)
# plt.ylabel(abf.sweepLabelY)
# plt.xlabel(abf.sweepLabelX)
# plt.axis([0, 300, -150, 300])
# plt.plot(abf.sweepX, abf.sweepY)
# plt.savefig(filename + '.png')
# plt.show()

#wb.save(outfile + ".xls")









