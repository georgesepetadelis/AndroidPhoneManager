import os 
import sys


def main():
    os.system("color 9")
    cmd = input("(APM) >> ")
    if(cmd == "open screen"):
        print("make sure when you have enable debuging n your android phone and you have it connected to this pc!")
        input("press any key when your phone is connected to this pc...\n")
        os.system("scrcpy-noconsole.exe")
        input()
        return main()
    if (cmd == "open port"):
        port = input("please enter a port number: ")
        os.system("adb tcpip " + port)
        print("the port " + port + "have be opened successfully!") 
        return main()
    if (cmd == "devices"):
        os.system("adb devices")
        return main()
    if(cmd == "connect w"):
        ip = input("please enter the local ip of your andorid phone: ")
        port = input("please enter the port when you want to connect: ")
        os.system("adb connect " + ip + ":" + port)
        print("now your phone is connected via adb on this pc (you can remove the usb cable if you want)")
        return main()
    if(cmd == "restart"):
        os.system("adb reboot")
        return main()
    if(cmd == "fastboot"):
        os.system("adb reboot-bootloader")
        return mian()
    if (cmd == "exit"):
        os.system("exit")
    else:
        print("command not found")
        return main()


print("-- Welcome to AndroidPhoneManager -- (by george sepetadelis)\n")
main()
