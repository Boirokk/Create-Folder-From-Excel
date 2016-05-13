import os, xlrd

# Constant for EXCEL dirpath
EXCEL = r"\\T13d-02\c$\Users\jblaner\Desktop\ESTHEC CUT OFFS.xlsx"
FOLDER_LOCATION = r"C:\Users\cczilli\Desktop\New folder\test-t"

# Create an object for workbook and sheet
workbook = xlrd.open_workbook(EXCEL)
sheet = workbook.sheet_by_index(0)

# Iterate through excel sheet
for row in range(sheet.nrows):
    folder_front = sheet.cell_value(row,0)
    folder_back = sheet.cell_value(row,1)
    print(str(folder_front) + ' - ' + folder_back

    # # Create directory with excel data
    # try:
    #     os.mkdir(FOLDER_LOCATION)
    # except FileExistsError:
    #     pass




