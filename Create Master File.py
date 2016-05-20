import os, xlrd

# Constant for EXCEL dirpath
<<<<<<< HEAD
EXCEL = r"C:\Users\Chad\Desktop\Book1.xlsx"
#FOLDER_LOCATION = r"S:\_TDS\TDS JOB MASTER FILES\Master File Builder"
FOLDER_LOCATION = r"C:\Users\Chad\Desktop\New folder"
=======
EXCEL = r"C:\Users\cczilli\Desktop\Book1.xlsx"
#FOLDER_LOCATION = r"S:\_TDS\TDS JOB MASTER FILES\Master File Builder"
FOLDER_LOCATION = r"C:\Users\cczilli\Desktop\New folder"
>>>>>>> origin/master

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
<<<<<<< HEAD
        os.mkdir(FOLDER_LOCATION + '\\' + folder_front + '-' + folder_back.upper())
=======
        os.mkdir(FOLDER_LOCATION + '\\' + str(folder_front) + '-' + folder_back.upper())
        os.mkdir(FOLDER_LOCATION + '\\' + str(folder_front) + '-' + folder_back.upper() + '\\' + '01- INVOICES-RELEASE')
        os.mkdir(FOLDER_LOCATION + '\\' + str(folder_front) + '-' + folder_back.upper() + '\\' + '02- ORDER CONFIRMATION & PO')
        os.mkdir(FOLDER_LOCATION + '\\' + str(folder_front) + '-' + folder_back.upper() + '\\' + '03- QUOTES')
        os.mkdir(FOLDER_LOCATION + '\\' + str(folder_front) + '-' + folder_back.upper() + '\\' + '04- JOB ORDER')
        os.mkdir(FOLDER_LOCATION + '\\' + str(folder_front) + '-' + folder_back.upper() + '\\' + '05- SHIPPING')
        os.mkdir(FOLDER_LOCATION + '\\' + str(folder_front) + '-' + folder_back.upper() + '\\' + '06- DRAWINGS')
        os.mkdir(FOLDER_LOCATION + '\\' + str(folder_front) + '-' + folder_back.upper() + '\\' + '07- PICTURES')
        os.mkdir(FOLDER_LOCATION + '\\' + str(folder_front) + '-' + folder_back.upper() + '\\' + '08- CORRESPONDENCE')
        os.mkdir(FOLDER_LOCATION + '\\' + str(folder_front) + '-' + folder_back.upper() + '\\' + '09- WORKSHEETS')
        os.mkdir(FOLDER_LOCATION + '\\' + str(folder_front) + '-' + folder_back.upper() + '\\' + '10- TIME SHEET')
        os.mkdir(FOLDER_LOCATION + '\\' + str(folder_front) + '-' + folder_back.upper() + '\\' + '11- TRAVEL')
        os.mkdir(FOLDER_LOCATION + '\\' + str(folder_front) + '-' + folder_back.upper() + '\\' + '12- EXPENSE REPORT')
        os.mkdir(FOLDER_LOCATION + '\\' + str(folder_front) + '-' + folder_back.upper() + '\\' + '13- PROD. FINAL')
        print('Adding, ', row, ' folder.')
>>>>>>> origin/master
    except FileExistsError:
        continue



print('Done... No more folders to add.')
input()

