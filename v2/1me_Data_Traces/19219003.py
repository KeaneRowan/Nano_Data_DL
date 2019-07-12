from DataSheet_Read import dataPoints as dp


abfFile = r'C:\Users\Elijah\Documents\NanoporeData\abfRaw\19219003.abf'
dataSheet = r'C:\Users\Elijah\Documents\NanoporeData\abfSheets\1me\19219003.xlsx'
eventFile = '19219003_events.csv'

dp(abfFile, dataSheet, eventFile)