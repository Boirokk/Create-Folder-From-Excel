import os, xlrd

# Constant for EXCEL dirpath
EXCEL = r"C:\Users\Chad\Desktop\Book1.xlsx"
#FOLDER_LOCATION = r"S:\_TDS\TDS JOB MASTER FILES\Master File Builder"
FOLDER_LOCATION = r"C:\Users\Chad\Desktop\New folder"

# Create an object for workbook and sheet
workbook = xlrd.open_workbook(EXCEL)
sheet = workbook.sheet_by_index(0)

# Iterate through excel sheet
for row in range(sheet.nrows):

    try:
        # Get excel data
        folder_front = str(sheet.cell_value(row, 0))
        if '.0' in folder_front:
            folder_front = folder_front.replace('.0','')

        #folder_front = str(folder_front)
        folder_back = str(sheet.cell_value(row, 1))
        # Create directory with excel data
        os.mkdir(FOLDER_LOCATION + '\\' + folder_front + '-' + folder_back.upper())
    except FileExistsError:
        continue




