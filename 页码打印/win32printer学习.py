import win32print
import win32ui
import win32con


INCH = 1440
# 实例化huo
hDC = win32ui.CreateDC()
# 获取打印机句柄
hDC.CreatePrinterDC(win32print.GetDefaultPrinter())
# 设置打印位置
ulc_x = 200  # 左上X
ulc_y = -200  # 左上Y
lrc_x = 11350  # 右下X
lrc_y = -11350  # 右下Y
# # 开始打印
hDC.StartDoc("add page")
    # 获取打印机状态
hPrinter = win32print.OpenPrinter('HP LaserJet 1020')
dic = win32print.GetPrinter(hPrinter, 10)
# if dic['cJobs'] == 1:
#     for i in range(1, 99):
#         hDC.StartPage()
#         hDC.SetMapMode(win32con.MM_TWIPS)
#         hDC.DrawText(str(i), (ulc_x, ulc_y, lrc_x, lrc_y), win32con.DT_RIGHT)
#         hDC.EndPage()
# else:
#     print('打印机缺纸，无法打印')
print(dic)
hDC.EndDoc()
