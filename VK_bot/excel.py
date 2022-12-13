import os.path
import openpyxl


def ticket_saver(theme, sender, send_time,path):
    my_path = f"/Users/sevak/PycharmProjects/VK_bot/{path}.xlsx"

    if os.path.isfile(my_path):
        wb = openpyxl.load_workbook(my_path)
        wb.active = 0
        sheet = wb.active
    else:
        wb = openpyxl.Workbook()
        wb.active = 0
        sheet = wb.active
        sheet['A1'] = 'Тема тикета'
        sheet['B1'] = 'От кого'
        sheet['C1'] = 'Когда'

    a = 2

    while True:
        if sheet['A' + str(a)].value == None:
            sheet['A' + str(a)].value = theme
            sheet['B' + str(a)].value = sender
            sheet['C' + str(a)].value = send_time
            break
        else:
            a += 1

    wb.save(my_path)
    wb.close()
