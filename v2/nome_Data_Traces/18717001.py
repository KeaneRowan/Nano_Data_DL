from DataSheet_Read import dataPoints as dp


abfFile = r'C:\Users\Elijah\Documents\NanoporeData\abfRaw\18717001.abf'
dataSheet = r'C:\Users\Elijah\Documents\NanoporeData\abfSheets\nome\18717001.xlsx'
eventFile = '18717001_events.csv'

dp(abfFile, dataSheet, eventFile)