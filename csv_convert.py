#This is a simple Python program for converting csv files into Excel files. 
#Created this for general purpose or incase you need to use an Excel but dont have the option to convert it from csv
#Proposed changes:
#Make into an executable? 
#Finished:
# - opening a dialogue box and choose what file you want to convert (Instead of writing it directly) DONE!
# - Open a dialogue box and choose where to save said file. DONE!!

import csv
import openpyxl
from tkinter import Tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename

Tk().withdraw()


#Opens dialogue box and user chooses what file to convert
csvFile = askopenfilename()

#Array for saving csv data
csv_data = []

#Program reads and appends the csv data into an array
with open(csvFile) as file_obj:
    reader = csv.reader(file_obj, delimiter=',') #Delimiter default is ',' so must change to what the file uses.
    for row in reader:
        csv_data.append(row)

#Creates and populates a new excel workbook.
wb = openpyxl.Workbook()
sheet = wb.active
for row in csv_data:
    sheet.append(row)

#Save location and file name of the newly converted excel file
excelFile = filedialog.asksaveasfilename(
    defaultextension = ".xlsx",
    filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")]
)
if excelFile:
    wb.save(excelFile)