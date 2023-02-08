#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import sys
import time
import requests
import webbrowser

print("小树科技KMS软件激活 V2.0.0")
try:
    print("网络连接中....")
    offPwd = requests.get('https://wanghanduo.github.io/storehouse/Ufish/password/office.txt').text
    winPwd = requests.get('https://wanghanduo.github.io/storehouse/Ufish/password/windows.txt').text
    offRev = requests.get('https://wanghanduo.github.io/storehouse/Ufish/version/version-office.txt').text
    winRev = requests.get('https://wanghanduo.github.io/storehouse/Ufish/version/version-win.txt').text
    office = requests.get('https://wanghanduo.github.io/storehouse/Ufish/Office.txt').text
    windows = requests.get('https://wanghanduo.github.io/storehouse/Ufish/Windows.txt').text
    print("网络连接成功！")
    sys.path.append("libs")
    webbrowser.open('https://xiaoshukeji.github.io/KMS/Pro.html')
except:
    print("ERROR:网络连接失败！请检查网络或以管理员运行本程序！")
    time.sleep(8)
    exit()
print("[1]兑换Windows激活")
print("[2]兑换Office激活")
print("[3]小树KMS激活协议")
print("[4]下载器更新")
number = int(input("请输入操作数字："))
if number == 1:
    key = input("请输入密钥：")
    if key == winPwd:
        print("兑换成功[Windows]")
        try:
            with open("winRev.ini", "r", encoding='utf-8') as winver:
                if winver.read() != winRev:
                    os.remove("win.bat")
                    with open("winRev.ini", 'w') as winver:
                        winver.write(winRev)
                        winver.close()
                    print("更新完成!")
        except:
            with open("winRev.ini", 'w') as winver:
                winver.write(winRev)
                winver.close()
        try:
            os.startfile(r".\win.bat")
            print("完成!")
            time.sleep(5)
        except:
            try:
                with open("win.bat", 'w') as win:
                    win.write(windows)
                    win.close()
                    os.startfile(r".\win.bat")
                    print("完成!")
                    time.sleep(5)
            except:
                print("ERROR:文件创建错误，请以管理员运行！")
    else:
        print("密码错误！")
elif number == 2:
    key = input("请输入密钥：")
    if key == offPwd:
        print("兑换成功[Office]")
        try:
            with open("offRev.ini", "r", encoding='utf-8') as offver:
                if offver.read() != winRev:
                    os.remove("win.bat")
                    with open("offRev.ini", 'w') as offver:
                        offver.write(offRev)
                        offver.close()
                    print("更新完成!")
        except:
            with open("offRev.ini", 'w') as offver:
                offver.write(offRev)
                offver.close()
        try:
            os.startfile(r".\off.bat")
            print("完成!")
            time.sleep(5)
        except:
            try:
                with open("off.bat", 'w') as off:
                    off.write(office)
                    off.close()
                    os.startfile(r".\off.bat")
                    print("完成!")
                    time.sleep(5)
            except:
                print("ERROR:文件创建错误，请以管理员运行！")
    else:
        print("密码错误！")
elif number == 3:
    sys.path.append("libs")
    webbrowser.open('https://xiaoshukeji.github.io/Pro.html')
elif number == 4:
    sys.path.append("libs")
    webbrowser.open('https://xiaoshukeji.github.io/Updata.html')
else:
    print("ERROR:请输入有效数字！")
    time.sleep(5)
    exit()
