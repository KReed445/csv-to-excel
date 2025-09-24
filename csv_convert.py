#This is a simple Python program for converting csv files into Excel files. 
#Created this for general purpose or incase you need to use an Excel but dont have the option to convert it from csv
#Proposed changes:
# -opening a dialogue box and choose what file you want to convert (Instead of writing it directly)
# -

import csv
import openpyxl

csv_data = []
#Choose what CSV you want to convert
with open('./CSV/YOUR_CSV_FILE.csv') as file_obj:
    reader = csv.reader(file_obj, delimiter=';') #Delimiter default is ',' so must change to what the file uses.
    for row in reader:
        csv_data.append(row)
#Reads the CSV and then populates a new excel workbook.
wb = openpyxl.Workbook()
sheet = wb.active
for row in csv_data:
    sheet.append(row)
    
#Save location (File path) of the newly converted file
wb.save('./Excel/NEW_EXCEL_FILE.xlsx')