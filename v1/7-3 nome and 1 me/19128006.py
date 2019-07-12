




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

filename = r'C:\Users\Elijah\Documents\NanoporeData\abfRaw\filtered_bessel8pole_500hz_19128006.abf'

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

dataPoints(10386, 10401)
dataPoints(10421, 10434)
dataPoints(10448, 11881)
dataPoints(12134, 12137)
dataPoints(54381, 54760)
dataPoints(55081, 55091)
dataPoints(55182, 55600)
dataPoints(55619, 55623)
dataPoints(77558, 78691)
dataPoints(78754, 82998)
dataPoints(83023, 83052)
dataPoints(83222, 83642)
dataPoints(122220, 122226)
dataPoints(122701, 126430)
dataPoints(126433, 126451)
dataPoints(126491, 127173)
dataPoints(127479, 127485)
dataPoints(127575, 127578)
dataPoints(127721, 142435)
dataPoints(142508, 142513)
dataPoints(142582, 142697)
dataPoints(142767, 142850)
dataPoints(142855, 142860)
dataPoints(142965, 142979)
dataPoints(164160, 171818)
dataPoints(171872, 171922)
dataPoints(188633, 188636)
dataPoints(208388, 220899)
dataPoints(236402, 238862)
dataPoints(239394, 239420)
dataPoints(239510, 241188)
dataPoints(241429, 241432)
dataPoints(241582, 241677)
dataPoints(241718, 241971)
dataPoints(260766, 260769)
dataPoints(261338, 261345)
dataPoints(261495, 261508)
dataPoints(261552, 261730)
dataPoints(261739, 262106)
dataPoints(262213, 262255)
dataPoints(262371, 262482)
dataPoints(262594, 263960)
dataPoints(289646, 290163)
dataPoints(290330, 290348)
dataPoints(290576, 291226)
dataPoints(291602, 291662)
dataPoints(291715, 291721)
dataPoints(291894, 291906)
dataPoints(291965, 291969)
dataPoints(292158, 293638)
dataPoints(293678, 297579)
dataPoints(297870, 298438)
dataPoints(298450, 299772)

print(counter)