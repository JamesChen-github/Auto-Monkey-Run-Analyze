import openpyxl as xl
import get_path
import os



def create_xlsx():
    xlsx_path = get_path.get_xlsx_path()
    #print(xlsx_path)
    #print('***** 开始写入excel文件 ' + xlsx_path + ' ***** \n')
    # if os.path.exists(xlsx_path):
    #     print('***** excel已存在，在表后添加数据 ' + xlsx_path + ' ***** \n')
    #     workbook = xl.load_workbook(xlsx_path)
    # else:
    #print('创建excel ' + xlsx_path + ' ***** \n')
    workbook = xl.Workbook()
    sheet = workbook.active
    
    # 设置列宽行高
    sheet.column_dimensions['A'].width=18
    sheet.column_dimensions['B'].width=150
    for i in range(1, 201):
        sheet.row_dimensions[i].height = 18
    
    # 写内容
    sheet.append(["日期", get_path.get_date()])
    sheet.append([])
    sheet.append([])
    sheet.append(["logcat", get_path.get_logcat_hyperlink()])
    cell = sheet['B4']
    cell.hyperlink = get_path.get_logcat_hyperlink()
    cell.value = get_path.get_logcat_hyperlink()
    cell.style = "Hyperlink"
    
    sheet.append(["串口", get_path.get_serial_hyperlink()])
    cell = sheet['B5']
    cell.hyperlink = get_path.get_serial_hyperlink()
    cell.value = get_path.get_serial_hyperlink()
    cell.style = "Hyperlink"
    
    sheet.append(["monkey_info", get_path.get_monkey_info_hyperlink()])
    cell = sheet['B6']
    cell.hyperlink = get_path.get_monkey_info_hyperlink()
    cell.value = get_path.get_monkey_info_hyperlink()
    cell.style = "Hyperlink"
    
    sheet.append(["monkey_error", get_path.get_monkey_error_hyperlink()])
    cell = sheet['B7']
    cell.hyperlink = get_path.get_monkey_error_hyperlink()
    cell.value = get_path.get_monkey_error_hyperlink()
    cell.style = "Hyperlink"
    #cell.value = '=HYPERLINK("{}", "{}")'.format("\\\\192.168.0.195\\RND Share\\SW\\Android\\05_Log\\monkey_test_Jiahao\\2022-07-19\\logcat.log", "\\\\192.168.0.195\\RND Share\\SW\\Android\\05_Log\\monkey_test_Jiahao\\2022-07-19\\logcat.log")
    
    sheet.append([])
    sheet.append([])
    sheet.append(["测试报告概要:"])
    
    workbook.save(xlsx_path)
    #print('***** 生成Excel文件 ' + xlsx_path + ' ***** \n')

if __name__ == "__main__":
    create_xlsx()