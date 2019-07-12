from DataSheet_Read import dataPoints as dp


abfFile = r'C:\Users\Elijah\Documents\NanoporeData\abfRaw\18717002.abf'
dataSheet = r'C:\Users\Elijah\Documents\NanoporeData\abfSheets\nome\18717002.xlsx'
eventFile = '18717002_events.csv'

dp(abfFile, dataSheet, eventFile)
