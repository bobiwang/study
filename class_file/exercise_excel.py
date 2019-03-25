# 打开 Excel
import xlrd
import xlwt
import os


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
    )

path =
def readfile(file):
    data = xlrd.open_workbook(file)

readfile('ABCC测试用例.excel')