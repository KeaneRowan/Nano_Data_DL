import pandas as pd
import pyabf
import csv
from keras_preprocessing.sequence import pad_sequences

def dataPoints(abfFile ,sheet, newCSVname):
    abf = pyabf.ABF(abfFile)
    with open(newCSVname, mode='w') as csvNew:
        writer = csv.writer(csvNew, delimiter=',')
        frame = pd.read_excel(sheet)
        start = frame['Start Time'].dropna()
        end = frame['End Time'].dropna()
        eventLengths = []
        for n in range(start.count()):
            eventStats = []
            eventStart = int(start[n])
            eventEnd = int(end[n])
            counter = 0
            limit = 0
            for n in range(eventStart, eventEnd):
                Y = abf.sweepY[n]
                eventStats.append(Y)
                limit += 1
            if len(eventStats) > 70000 and len(eventStats) < 80000:
                for n in range(len(eventStats),80000):
                    eventStats.append(0)
                print(len(eventStats))
                writer.writerow(eventStats)

            eventLengths.append(counter)
    csvNew.close()


# def dataPoints(abfFile ,sheet, newCSVname):
#     abf = pyabf.ABF(abfFile)
#     with open(newCSVname, mode='w') as csvNew:
#         writer = csv.writer(csvNew, delimiter=',')
#         frame = pd.read_excel(sheet)
#         start = frame['Start Time'].dropna()
#         end = frame['End Time'].dropna()
#         eventLengths = []
#         for n in range(start.count()):
#             eventStats = []
#             eventStart = int(start[n])
#             eventEnd = int(end[n])
#             counter = 0
#             limit = 0
#             for n in range(eventStart, eventEnd):
#                 Y = abf.sweepY[n]
#                 eventStats.append(Y)
#                 counter += 1
#                 limit += 1
#             # eventStats.append(111111111111111111111111)
#             writer.writerow(eventStats)
#             eventLengths.append(counter)
#     csvNew.close()
#     print(eventLengths)
