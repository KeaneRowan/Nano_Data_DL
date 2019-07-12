import sys
from xlwt import Workbook
from xlutils.copy import copy
from xlrd import open_workbook
from xlwt import easyxf


print('Python: {}'.format(sys.version))

import pyabf
import numpy as np
import matplotlib.pyplot as plt

wb = Workbook()
destination = "19122007.xls"
sheet = wb.add_sheet(destination)

filename = r'C:\Users\Elijah\Documents\NanoporeData\abfRaw\filtered_bessel8pole_500hz_19122009.abf'

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
        print(float(abf.sweepX[n]), float(abf.sweepY[n]))
        global counter
        sheet.write(counter, 0, float(abf.sweepX[n])), sheet.write(counter, 1, float(abf.sweepY[n]))
        counter += 1

#https://stackoverflow.com/questions/2725852/writing-to-existing-workbook-using-xlwt

# from xlutils.copy import copy # http://pypi.python.org/pypi/xlutils
# from xlrd import open_workbook # http://pypi.python.org/pypi/xlrd
# from xlwt import easyxf # http://pypi.python.org/pypi/xlwt
#
# START_ROW = 297 # 0 based (subtract 1 from excel row number)
# col_age_november = 1
# col_summer1 = 2
# col_fall1 = 3
#
# rb = open_workbook(file_path,formatting_info=True)
# r_sheet = rb.sheet_by_index(0) # read only copy to introspect the file
# wb = copy(rb) # a writable copy (I can't read values out of this, only write to it)
# w_sheet = wb.get_sheet(0) # the sheet to write to within the writable copy

# for row_index in range(START_ROW, r_sheet.nrows):
#     age_nov = r_sheet.cell(row_index, col_age_november).value
#     if age_nov == 3:
#         #If 3, then Combo I 3-4 year old  for both summer1 and fall1
#         w_sheet.write(row_index, col_summer1, 'Combo I 3-4 year old')
#         w_sheet.write(row_index, col_fall1, 'Combo I 3-4 year old')


dataPoints(33663, 34821)
dataPoints(35332, 37740)
dataPoints(37839, 45095)
dataPoints(45603, 46131)
dataPoints(77321, 77368)
dataPoints(77689, 77699)
dataPoints(77983, 77994)
dataPoints(78419, 93032)
dataPoints(158811, 158822)
dataPoints(159057, 160233)
dataPoints(160903, 164169)
dataPoints(164556, 164632)
dataPoints(179768, 179784)
dataPoints(180480, 180970)
dataPoints(181283, 181299)
dataPoints(181314, 184043)
dataPoints(184100, 194408)
dataPoints(194530, 194535)
dataPoints(194887, 194919)
dataPoints(195021, 195024)
dataPoints(195327, 195340)
dataPoints(195411, 195486)
dataPoints(195519, 195537)
dataPoints(195726, 195903)
dataPoints(196046, 196050)
dataPoints(196257, 196262)
dataPoints(196942, 196964)
dataPoints(196969, 196991)
dataPoints(197027, 197035)
dataPoints(197053, 197065)
dataPoints(197109, 199953)
dataPoints(200075, 200867)
dataPoints(201081, 201121)
dataPoints(218848, 219431)
dataPoints(219569, 220846)
dataPoints(245986, 251821)
dataPoints(252132, 252156)
dataPoints(289608, 289629)
dataPoints(289755, 289764)
dataPoints(289804, 289947)
dataPoints(290140, 290637)
dataPoints(290827, 290838)
dataPoints(291240, 291297)
dataPoints(292093, 292229)

#print(counter)

wb.save(destination)

plt.figure(figsize=(8, 5))
plt.title("Nanopore file:" + filename)
plt.ylabel(abf.sweepLabelY)
plt.xlabel(abf.sweepLabelX)
plt.axis([0, 300, -150, 100])
plt.plot(abf.sweepX, abf.sweepY)
#plt.savefig(filename + '.png')
#plt.show()

