from DataSheet_Read import dataPoints as dp


abfFile = r'C:\Users\Elijah\Documents\NanoporeData\abfRaw\19219010.abf'
dataSheet = r'C:\Users\Elijah\Documents\NanoporeData\abfSheets\1me\19219010.xls'
eventFile = '19219010_events.csv'

dp(abfFile, dataSheet, eventFile)