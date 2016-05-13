import os, xlrd

# Constant for EXCEL dirpath
EXCEL = r"C:\Users\cczilli\Desktop\Book1.xlsx"
FOLDER_LOCATION = r"S:\_TDS\TDS JOB MASTER FILES\Master File Builder"
#FOLDER_LOCATION = r"C:\Users\cczilli\Desktop\New folder"

# Create an object for workbook and sheet
workbook = xlrd.open_workbook(EXCEL)
sheet = workbook.sheet_by_index(0)

# Iterate through excel sheet
for row in range(sheet.nrows):

    try:
        # Get excel data
        folder_front = int(sheet.cell_value(row, 0))
        folder_back = sheet.cell_value(row, 1)
        # Create directory with excel data
        os.mkdir(FOLDER_LOCATION + '\\' + str(folder_front) + '-' + folder_back.upper())
    except FileExistsError:
        continue




