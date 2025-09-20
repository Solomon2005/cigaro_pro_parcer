import xlsxwriter
from parcer import array

def writer(index):
    book = xlsxwriter.Workbook(r"C:\Users\SOLOMON\Desktop\data.xlsx")
    page = book.add_worksheet('Алкоголь')

    row = 0
    col = 0

    page.set_column("A:A", 60)
    page.set_column("B:B", 60)
    page.set_column("C:C", 10)


    for item in index():
        page.write(row, col, item[0])
        page.write(row, col+1, item[1])
        page.write(row, col+2, item[2])
        row += 1

    book.close()

writer(array)
