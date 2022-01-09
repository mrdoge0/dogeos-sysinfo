#!/usr/bin/python3

from tkinter import *
import tkinter as tk
import platform
import cpuinfo
import socket
import psutil
import distro
import re
import os

bootMode = "UEFI" if os.path.exists("/sys/firmware/efi") else "Legacy"

cmd = "pacman -Q | wc -l"

desktopEvrionment = "Unknown"
windowManager = "Unknown"

desktopEvrionmentRaw = os.environ.get('DESKTOP_SESSION')
    
if desktopEvrionmentRaw.startswith("gnome"):
    windowManager = "Mutter"
    if desktopEvrionmentRaw.startswith("gnome-xorg"):
        desktopEvrionment = "GNOME (X11)"
    else:
        desktopEvrionment = "GNOME (Wayland)"
elif desktopEvrionmentRaw.startswith("ubuntu"):
    desktopEvrionment = "GNOME (Ubuntu)"
    windowManager = "Mutter"
elif desktopEvrionmentRaw.startswith("xfce"):
    desktopEvrionment = "XFCE4"
    windowManager = "Xfwm4"
elif desktopEvrionmentRaw.startswith("xubuntu"):
    desktopEvrionment = "XFCE4 (Xubuntu)"
    windowManager = "Xfwm4"
elif desktopEvrionmentRaw.startswith("kde"):
    desktopEvrionment = "KDE Plasma"
    windowManager = "Kwin"
elif desktopEvrionmentRaw.startswith("kubuntu"):
    desktopEvrionment = "KDE Plasma (Kubuntu)"
    windowManager = "Kwin"
elif desktopEvrionmentRaw.startswith("cinnamon"):
    desktopEvrionment = "Cinnamon"
    windowManager = "Mutter"
elif desktopEvrionmentRaw.startswith("lxde"):
    desktopEvrionment = "LXDE"
    windowManager = "Openbox"
elif desktopEvrionmentRaw.startswith("lxqt"):
    desktopEvrionment = "LXQT"
    windowManager = "Openbox"
elif desktopEvrionmentRaw.startswith("lubuntu"):
    desktopEvrionment = "LXQT/LXDE (Lubuntu)"
    windowManager = "Openbox"
elif desktopEvrionmentRaw.startswith("mate"):
    desktopEvrionment = "MATE"
    windowManager = "Metacity/Compiz"
else:
    desktopEvrionment = "Unknown"

window = tk.Tk()
window.title("System Information")
window.geometry("1000x700")
window.resizable(False, False)

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

Label(window, text = "System Information", width = 1000, height = "1", font=("Sans Serif", 15), anchor="w").pack(pady=0, side= TOP)

Label(window, text = "Operating System       : " + distro.name(pretty=True) + " (" + platform.machine() + ")", width = 1000, height = "1", anchor="w").pack(pady=0, side= TOP)
Label(window, text = platform.system() + " Kernel Version : " + platform.release(), width = 1000, height = "1", anchor="w").pack(pady=0, side= TOP)
# Label(window, text = "Installed Packages     : " + os.popen(cmd).read()[0], width = 1000, height = "1", anchor="w").pack(side= TOP)
Label(window, text = "Computer Name         : " + socket.gethostname(), width = 1000, height = "1", anchor="w").pack(pady=0, side= TOP)

Label(window, text = "CPU Name                  : " + cpuinfo.get_cpu_info()['brand_raw'], width = 1000, height = "1", anchor="w").pack(pady=0, side= TOP)
Label(window, text = "Total RAM                    : " + str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB", width = 1000, height = "1", anchor="w").pack(pady=0, side= TOP)
Label(window, text = "Boot Mode                   : " + bootMode, width = 1000, height = "1", anchor="w").pack(pady=0, side= TOP)
Label(window, text = "Screen Resolution     : " + str(screen_width) + "x" + str(screen_height), width = 1000, height = "1", anchor="w").pack(pady=0, side= TOP)
Label(window, text = "Desktop Evrionment  : " + desktopEvrionment, width = 1000, height = "1", anchor="w").pack(pady=0, side= TOP)
Label(window, text = "Window Manager       : " + windowManager, width = 1000, height = "1", anchor="w").pack(pady=0, side= TOP)

tk.mainloop()
