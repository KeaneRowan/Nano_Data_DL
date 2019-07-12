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

filename = r'C:\Users\Elijah\Documents\NanoporeData\abfRaw\filtered_bessel8pole_500hz_19128004.abf'

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

dataPoints(8264, 14826)
dataPoints(14858, 27423)
dataPoints(27511, 27528)
dataPoints(49191, 49244)
dataPoints(49350, 49519)
dataPoints(49916, 50694)
dataPoints(50993, 51005)
dataPoints(51043, 51084)
dataPoints(51130, 63453)
dataPoints(63535, 66278)
dataPoints(87787, 87791)
dataPoints(110141, 112116)
dataPoints(112548, 113251)
dataPoints(155677, 155704)
dataPoints(155751, 155759)
dataPoints(175947, 176284)
dataPoints(176516, 176969)
dataPoints(177087, 177096)
dataPoints(177167, 177172)
dataPoints(177353, 182850)
dataPoints(182875, 182880)
dataPoints(183031, 183072)
dataPoints(183087, 183145)
dataPoints(183373, 183381)
dataPoints(224253, 224731)
dataPoints(224764, 233137)
dataPoints(233277, 233280)
dataPoints(233323, 235526)
dataPoints(235854, 235866)
dataPoints(235950, 236010)
dataPoints(236171, 236189)
dataPoints(236266, 239359)
dataPoints(239464, 240060)
dataPoints(240107, 254651)
dataPoints(280254, 281395)
dataPoints(281434, 290216)
dataPoints(290354, 291749)
dataPoints(292001, 292012)
dataPoints(292177, 293837)
dataPoints(293888, 293908)
dataPoints(293912, 293923)
dataPoints(294807, 294811)
dataPoints(294899, 295203)
dataPoints(295309, 295322)
dataPoints(295351, 295358)
dataPoints(295361, 295373)

print(counter)