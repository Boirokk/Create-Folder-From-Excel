import os, xlrd

# Constant for EXCEL dirpath
EXCEL = r"C:\Users\cczilli\Desktop\Book1.xlsx"
FOLDER_LOCATION = r"S:\_TDS\TDS JOB MASTER FILES"

# Create an object for workbook and sheet
workbook = xlrd.open_workbook(EXCEL)
sheet = workbook.sheet_by_index(0)

# Iterate through excel sheet
for row in range(sheet.nrows):

    try:
        # Get excel data
        folder_front = str(sheet.cell_value(row, 0))
        folder_back = sheet.cell_value(row, 1)
        # Create directory with excel data
        os.mkdir(FOLDER_LOCATION + '\\' + folder_front + ' - ' + folder_back)
    except FileExistsError:
        continue




