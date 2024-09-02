import customtkinter
import PIL
import keyboard
import pygame
import webbrowser
from PIL import Image
from pymem import *
from pymem.process import *
from pymem.ptypes import RemotePointer
from subprocess import Popen
from threading import Thread

# The game were hacking
mem = Pymem("RelicCOH")
# The dll we write to
module = module_from_name(mem.process_handle, "WW2Mod.dll").lpBaseOfDll
# static pointer offsets
Money_offsets = [0x0, 0X10, 0X24, 0X18, 0X264]
gas_offsets = [0x0, 0x10, 0x30, 0x18, 0x268]
ammo_offsets = [0x0, 0x26C]
cap_offsets = [0x0, 0x4E8]


# Are threads
def multi_run_money():
    new_thread = Thread(target=money_hack, daemon=True)
    new_thread.start()


def multi_run_gas():
    new_thread = Thread(target=gas_hack, daemon=True)
    new_thread.start()


def multi_run_pop():
    new_thread = Thread(target=cap_hack, daemon=True)
    new_thread.start()


def multi_run_ammo():
    new_thread = Thread(target=ammo_hack, daemon=True)
    new_thread.start()


# Are functions
def getpointeraddress(base, offsets):
    remote_pointer = RemotePointer(mem.process_handle, base)
    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(mem.process_handle, remote_pointer.value + offset)
        else:
            return remote_pointer.value + offset


def money_hack():
    addr = getpointeraddress(module + 0x0061E810, Money_offsets)
    while 1:
        try:
            mem.write_int(addr, 0x47960000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            break


def gas_hack():
    addr = getpointeraddress(module + 0x0061E810, gas_offsets)
    while 1:
        try:
            mem.write_int(addr, 0x47960000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            break


def ammo_hack():
    addr = getpointeraddress(module + 0x0061E810, ammo_offsets)
    while 1:
        try:
            mem.write_int(addr, 0x47960000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            break


def cap_hack():
    addr = getpointeraddress(module + 0x0061E810, cap_offsets)
    while 1:
        try:
            mem.write_int(addr, 0x1)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            break


def open_msn():
    webbrowser.open_new("C:/Microsoft/Windows")


def open_calc():
    Popen("calc.exe")


def open_paint():
    Popen("mspaint.exe")


# ----- Menu music-----
pygame.init()
pygame.mixer_music.load("music/mod.mp3")
pygame.mixer_music.play(1)


# Menu gui/overlay


class App(customtkinter.CTk):
    width = 350
    height = 380

    def __init__(self):
        super().__init__()
        s = self
        s.title("Fragging Terminal")
        s.geometry(f"{s.width}x{s.height}")
        s.attributes("-topmost", 1)
        s.resizable(False, False)
        # Menu background
        image = PIL.Image.open("back/back.jpg")
        background_image = customtkinter.CTkImage(image, size=(350, 380))

        # Create a bg label
        bg_lbl = customtkinter.CTkLabel(s, text="", image=background_image)
        bg_lbl.place(x=0, y=0)
        # Menu buttons
        s.button = customtkinter.CTkButton(s, text="Money", fg_color="black", bg_color="black", text_color="red",
                                           hover_color="gray", command=multi_run_money)
        s.button.grid(row=0, column=0, padx=20, pady=10)

        s.button = customtkinter.CTkButton(s, text="Gas", fg_color="black", bg_color="black", text_color="red",
                                           hover_color="gray", command=multi_run_gas)
        s.button.grid(row=1, column=0, padx=20, pady=10)

        s.button = customtkinter.CTkButton(s, text="Ammo", fg_color="black", bg_color="black", text_color="red",
                                           hover_color="gray", command=multi_run_ammo)
        s.button.grid(row=2, column=0, padx=20, pady=10)

        s.button = customtkinter.CTkButton(s, text="Population Cap", fg_color="black", bg_color="black",
                                           text_color="red",
                                           hover_color="gray", command=multi_run_pop)
        s.button.grid(row=3, column=0, padx=20, pady=10)

        s.button = customtkinter.CTkButton(s, text="Exit", fg_color="black", bg_color="black", text_color="red",
                                           hover_color="gray", command=s.destroy)
        s.button.grid(row=4, column=0, padx=20, pady=10)

        s.button = customtkinter.CTkButton(s, text="MSN", fg_color="black", text_color="red",
                                           bg_color="black",
                                           hover_color="gray", command=open_msn)
        s.button.grid(row=4, column=2, padx=20, pady=10)

        s.button = customtkinter.CTkButton(s, text="Calculator", fg_color="black", text_color="red",
                                           bg_color="black",
                                           hover_color="gray", command=open_calc)
        s.button.grid(row=0, column=2, padx=20, pady=10)

        s.button = customtkinter.CTkButton(s, text="MS Paint", fg_color="black", text_color="red",
                                           bg_color="black",
                                           hover_color="gray", command=open_paint)
        s.button.grid(row=1, column=2, padx=20, pady=10)


# End loop


if __name__ == "__main__":
    app = App()
    app.mainloop()
