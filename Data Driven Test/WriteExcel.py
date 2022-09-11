# Install openpyxl module to work with excel

import openpyxl

file = "C:\\Users\\ialmu\\PycharmProjects\\data2.xlsx"

#file -> Workbook -> Sheets -> rows -> Cells
workbook = openpyxl.load_workbook(file)  #will load the workbook from the file
sheet = workbook["Sheet1"]      #we can use sheet name instead of sheet1 but sheet1 is recommended in case of a lot of sheet

#write data in excel
for row in range(1,6):                                  #write in 1st to 5th row
    for column in range(1,4):                           #write in 1st to 3rd column
        sheet.cell(row,column).value="welcome"          # read and write data

workbook.save(file)   #will save the data