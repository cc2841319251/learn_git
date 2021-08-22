import openpyxl
import xlrd
from xlutils.copy import copy

'''
此方法用于读取excel，txt，yaml文件
'''


class OperateFile:

    def read_excel_by_openpyxl(self, workbook_name, sheet_name):
        '''
        使用openpyxl读取excel文件
        :param workbook_name:
        :param sheet_name:
        :return:
        '''
        try:
            wb = openpyxl.load_workbook(workbook_name)
            ws = wb[sheet_name]
            rows = ws.rows
            for row in rows:
                content = [i.value for i in row]
                return content
        except Exception as e:
            print('打开失败，失败的原因是%s' % e)

    def write_excel_by_xlrd(self, workbook_name, sheet_name, row: int, col: int, value, file_name):
        '''
        利用 xlutils.copy 拷贝一份 Excel.
        xlutils.copy 可以实现以下功能:
        1. 读取表格信息的功能
        2. 在表格中写入数据的功能
        相当于 xlrd 和 xlwt 的结合体.
        但请注意, xlrd 读取的 xlsx 具有完整的读取功能, 但保存为新表格文件时, 必须以 '.xls' 格
        式保存, 因为 xlwt 只支持 '.xls' 格式的保存.
        :return:
        '''
        data = xlrd.open_workbook(workbook_name)
        data_copy = copy(data)
        sheet = data_copy.get_sheet(sheet_name)
        sheet.write(row, col, value)
        data_copy.save(file_name)

    def read_file_by_xlrd(self, workbook_name, sheet_name):
        '''
        也可以通过xlrd读取文件内容
        :param workbook_name:
        :param sheet_name:
        :return:
        '''
        try:
            wb = xlrd.open_workbook(workbook_name)
            ws = wb.sheet_by_name(sheet_name)
            all_content = []
            for row in range(ws.nrows):
                row_content = []
                for col in range(ws.ncols):
                    row_content.append(ws.cell_value(row, col))
                all_content.append(row_content)
            return all_content
        except Exception as e:
            print('文件打开失败，失败的原因是%s' % e)

    def read_txt_file(self, file_name):
        '''
        用来读取txt文本文件内容
        :param file_name:
        :return:
        '''
        try:
            with open(file_name, 'r', encoding='utf8') as f:
                lines = f.readlines()
                content = []
                for line in lines:
                    content.append(line.strip('\n').split(','))
                return content
        except Exception as e:
            print('文件打开失败，失败的原因是%s' % e)

    def write_txt_file(self, file_name, data):
        with open(file_name, 'w', encoding='utf8') as f:
            f.write(data)
