from DataSheet_Read import dataPoints as dp



abfFile = r'C:\Users\Elijah\Documents\NanoporeData\abfRaw\18713001.abf'
dataSheet = r'C:\Users\Elijah\Documents\NanoporeData\abfSheets\nome\18713001.xlsx'
eventFile = '18713001_events.csv'

dp(abfFile, dataSheet, eventFile)



