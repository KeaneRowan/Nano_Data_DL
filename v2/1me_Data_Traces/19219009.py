from DataSheet_Read import dataPoints as dp


abfFile = r'C:\Users\Elijah\Documents\NanoporeData\abfRaw\19219009.abf'
dataSheet = r'C:\Users\Elijah\Documents\NanoporeData\abfSheets\1me\19219009.xls'
eventFile = '19219009_events.csv'

dp(abfFile, dataSheet, eventFile)