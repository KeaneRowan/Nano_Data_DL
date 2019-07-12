import matplotlib
import pyabf
import pandas as pd
import matplotlib.pyplot as plt
import csv


eventLengths = []

def plot(sheet):
    # with open("EventTimes.csv", mode='a') as csvNew:
        # writer = csv.writer(csvNew, delimiter = ',')
        frame = pd.read_excel(sheet)
        start = frame['Start Time'].dropna()
        end = frame['End Time'].dropna()
        global eventLengths
        for n in range(start.count()):
            eventStart = int(start[n])
            eventEnd = int(end[n])
            counter = 0
            for n in range(eventStart, eventEnd):
                counter += 1
            eventLengths.append(counter)
    # csvNew.close()




sheet18713001 = r'C:\Users\Elijah\Documents\NanoporeData\abfSheets\nome\18713001.xlsx'

sheet18717000 = r'C:\Users\Elijah\Documents\NanoporeData\abfSheets\nome\18717000.xlsx'

sheet18717001 = r'C:\Users\Elijah\Documents\NanoporeData\abfSheets\nome\18717001.xlsx'

sheet18717002 = r'C:\Users\Elijah\Documents\NanoporeData\abfSheets\nome\18717002.xlsx'

sheet18717004 = r'C:\Users\Elijah\Documents\NanoporeData\abfSheets\nome\18717004.xlsx'

sheet18717010 = r'C:\Users\Elijah\Documents\NanoporeData\abfSheets\nome\18717010.xls'

sheet18n12012 = r'C:\Users\Elijah\Documents\NanoporeData\abfSheets\1me\18n12012.xls'

sheet19219003 = r'C:\Users\Elijah\Documents\NanoporeData\abfSheets\1me\19219003.xlsx'

sheet19219006 = r'C:\Users\Elijah\Documents\NanoporeData\abfSheets\1me\19219006.xlsx'

sheet19219008 = r'C:\Users\Elijah\Documents\NanoporeData\abfSheets\1me\19219008.xls'

sheet19219009 = r'C:\Users\Elijah\Documents\NanoporeData\abfSheets\1me\19219009.xls'

sheet19219010 = r'C:\Users\Elijah\Documents\NanoporeData\abfSheets\1me\19219010.xls'

sheets = []
sheets.append(sheet18713001)
sheets.append(sheet18717000)
sheets.append(sheet18717001)
sheets.append(sheet18717002)
sheets.append(sheet19219003)
sheets.append(sheet19219006)
sheets.append(sheet19219008)
sheets.append(sheet19219009)
sheets.append(sheet19219010)
sheets.append(sheet18n12012)
# sheets.append(sheet18717010)
# sheets.append(sheet18717004)

for sheet in sheets:
    plot(sheet)

range = (0, 100000)
bins = 500

plt.hist(eventLengths, bins, range, color = 'green', histtype = 'bar', rwidth = 0.8)
plt.xlabel("Event Times")
plt.ylabel("Frequency")
plt.show()