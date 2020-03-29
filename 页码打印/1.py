# encoding: utf-8
import win32ui
import win32print
import win32con
import time
import logging
from logging.handlers import TimedRotatingFileHandler


def send_to_printer(title, txt):
    hDC = win32ui.CreateDC()
    hDC.CreatePrinterDC(win32print.GetDefaultPrinter())
    hDC.StartDoc(title)
    hDC.StartPage()
    hDC.SetMapMode(win32con.MM_TWIPS)
    ulc_x = 10
    ulc_y = -10
    lrc_x = 11
    lrc_y = -11
    hDC.DrawText(txt, (ulc_x, ulc_y, lrc_x, lrc_y), win32con.DT_LEFT)
    hDC.EndPage()
    hDC.StartPage()
    hDC.SetMapMode(win32con.MM_TWIPS)
    ulc_x = 1000
    ulc_y = -1000
    lrc_x = 11500
    lrc_y = -11500
    hDC.DrawText(txt, (ulc_x, ulc_y, lrc_x, lrc_y), win32con.DT_CENTER)
    hDC.EndPage()
    hDC.EndDoc()
    print(u"正在运行第"+str(count)+u"次")
    looger.info(u"正在运行第 %s 次" % str(count))

send_to_printer('ttt','ttt')
# def hello(count):

# if count % 6 == 1:
#     f = open(r"D:\test\FP00001.txt")
#     lines1 = f.read()
#     f.close()
#     send_to_printer("lines", lines1)
# elif  count % 6 == 2:
#     f = open(r"D:\test\FP00002.txt")
#     lines2 = f.read()
#     f.close()
#     send_to_printer("lines", lines2)
# elif  count % 6 == 3:
# f = open(r"D:\test\FP00003.txt")
#     lines3 = f.read()
#     f.close()
#     send_to_printer("lines", lines3)
# elif  count % 6 == 4:
#     f = open(r"D:\test\FP00004.txt")
#     lines4 = f.read()
#     f.close()
#     send_to_printer("lines", lines4)
#          elif  count % 6 == 5:
#                 f = open(r"D:\test\FP00005.txt")
#                 lines5 = f.read()
#                 f.close()
#                 send_to_printer("lines", lines5)
#          elif  count % 6 == 0:
#                 f = open(r"D:\test\FP00006.txt")
#                 lines6 = f.read()
#                 f.close()
#                 send_to_printer("lines", lines6)
# if __name__ == '__main__':
#         looger = logging.getLogger('UsbPrint')
#         formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#         LogHandLer = TimedRotatingFileHandler(r'E:\count.log', when="midnight")
#         LogHandLer.setFormatter(formatter)
#         looger.addHandler(LogHandLer)
#         looger.setLevel(logging.INFO)
#     
#         count = 1
#          while(1):
#                 hello(count)
#                 count = count + 1
#                 f = open(r"D:\time.txt")
#                 line = f.read()  
#                 time.sleep(int(line))
#                 f.close()
