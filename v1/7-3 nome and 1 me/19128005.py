




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

filename = r'C:\Users\Elijah\Documents\NanoporeData\abfRaw\filtered_bessel8pole_500hz_19128005.abf'

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

dataPoints(4872, 10972)
dataPoints(11380, 13286)
dataPoints(13306, 21765)
dataPoints(21781, 21818)
dataPoints(52571, 56912)
dataPoints(56927, 66193)
dataPoints(66527, 66531)
dataPoints(66588, 66607)
dataPoints(66694, 67057)
dataPoints(125242, 125384)
dataPoints(125405, 140390)
dataPoints(162726, 162732)
dataPoints(162760, 162766)
dataPoints(185801, 186269)
dataPoints(186317, 186320)
dataPoints(206198, 206212)
dataPoints(206308, 206312)
dataPoints(206371, 206409)
dataPoints(206586, 206592)
dataPoints(206644, 206923)
dataPoints(207102, 207151)
dataPoints(207462, 207466)
dataPoints(207572, 207591)
dataPoints(208039, 208522)
dataPoints(209014, 209018)
dataPoints(209212, 209215)
dataPoints(250334, 251088)
dataPoints(272668, 272970)

print(counter)