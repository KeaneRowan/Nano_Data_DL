from DataSheet_Read import dataPoints as dp


abfFile = r'C:\Users\Elijah\Documents\NanoporeData\abfRaw\18717004.abf'
dataSheet = r'C:\Users\Elijah\Documents\NanoporeData\abfSheets\nome\18717004.xlsx'
eventFile = '18717004_events.csv'

dp(abfFile, dataSheet, eventFile)