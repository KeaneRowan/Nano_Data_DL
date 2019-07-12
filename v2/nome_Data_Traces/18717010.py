from DataSheet_Read import dataPoints as dp


abfFile = r'C:\Users\Elijah\Documents\NanoporeData\abfRaw\18717010.abf'
dataSheet = r'C:\Users\Elijah\Documents\NanoporeData\abfSheets\nome\18717010.xls'
eventFile = '18717010_events.csv'

dp(abfFile, dataSheet, eventFile)