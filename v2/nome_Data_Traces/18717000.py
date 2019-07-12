from DataSheet_Read import dataPoints as dp


abfFile = r'C:\Users\Elijah\Documents\NanoporeData\abfRaw\18717000.abf'
dataSheet = r'C:\Users\Elijah\Documents\NanoporeData\abfSheets\nome\18717000.xlsx'
eventFile = '18717000_events.csv'

dp(abfFile, dataSheet, eventFile)

