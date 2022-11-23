#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@File    :   main.py
@Time    :   2022/11/08 16:37:57
'''
# 本程序许建立一个excel表格由于存储截图和动作类型，用法看excel文件第一行的说明
from PIL import Image
from openpyxl import load_workbook
from openpyxl_image_loader import SheetImageLoader
import pyperclip, pyautogui, time, xlrd, sys, os

def main():
    # 在2s内去到第一张图片点击的页面
    time.sleep(2)
    # 一些需要用的变量
    x, y, width, height = 0, 0, 0, 0
    nums = 0

    for i in range(7):

        # 通过读取excel数据确定动作类型
        wb = xlrd.open_workbook("digital.xlsx")
        sheet0 = wb.sheet_by_index(0)
        # 因为excel第一行内容为标题
        Action_type = sheet0.row_values(i + 1)[0]

        if Action_type != 3:
            # 打开文件，读取需要的页
            pxl_doc = load_workbook('digital.xlsx')
            sheet = pxl_doc['Sheet1']

            # calling the image_loader
            image_loader = SheetImageLoader(sheet)

            # get the image (put the cell you need instead of 'A1')
            image = image_loader.get('C' + str(i + 2))

            # showing the image
            # image.show()

            # saving the image
            image.save(str(i+1) + '.jpg')
            time.sleep(0.5)

            name = str(i+1) + '.jpg'

            # 事先对按钮截图
            Img = Image.open(name)

            # 截图当前屏幕并找到之前加载的按钮图
            Image_elements = pyautogui.locateOnScreen(Img, confidence=0.9)
            while Image_elements is None:
                Image_elements = pyautogui.locateOnScreen(Img, confidence=0.9)
                print("没找到")
                time.sleep(0.5)
                if nums == 6:
                    sys.exit(0)
            else:
                # 将图片的位置、大小信息提取出来
                x, y, width, height = Image_elements
                nums = 0
        if Action_type == 1:
            # 左键点击屏幕上的这个位置,x+width/3, y+height/3是为了不要点击到边缘
            pyautogui.click(x+width/3, y+height/3, button='left')
            time.sleep(0.2)
        elif Action_type == 2:
            # 左键点击屏幕上的这个位置,x+width/3, y+height/3是为了不要点击到边缘
            pyautogui.click(x+width/3, y+height/3, button='left')
            time.sleep(0.2)
            # 输入时先复制再粘贴
            content = sheet0.row_values(i + 1)[1]
            pyperclip.copy(content)
            pyautogui.hotkey('ctrl', 'v')
        elif Action_type == 3:
            # 取出要按下键的名字
            content = sheet0.row_values(i + 1)[1]
            pyautogui.press(content)
            time.sleep(0.2)
            continue

        os.remove(str(i + 1) + '.jpg')
        time.sleep(0.2)


if __name__ == "__main__":
    main()




