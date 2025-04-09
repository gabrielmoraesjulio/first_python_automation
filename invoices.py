import os
from openpyxl import Workbook

directory = 'pdf_invoices' #invoices directory
files = os.listdir(directory) #what are the invoices
files_quantity = len(files) #quantity of invoices

if files_quantity == 0: #if the folder are empty
    raise Exception("No files found in the directory") #raise a exception to warn the user

wb = Workbook() #creating workbook
ws = wb.active
ws.title = 'Invoice Imports'

#structuring excel file
ws['A1'] = 'Invoice #'
ws['B1'] = 'Date'
ws['C1'] = 'File Name'
ws['D4'] = 'Status' 