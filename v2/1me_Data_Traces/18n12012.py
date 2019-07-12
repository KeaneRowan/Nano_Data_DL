import pandas
import csv
import pyabf
from DataSheet_Read import dataPoints as dp

abfFile = r'C:\Users\Elijah\Documents\NanoporeData\abfRaw\18n12012.abf'
dataSheet = r'C:\Users\Elijah\Documents\NanoporeData\abfSheets\1me\18n12012.xls'
eventFile = '18n12012_events.csv'

dp(abfFile, dataSheet, eventFile)
