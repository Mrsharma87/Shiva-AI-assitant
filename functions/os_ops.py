import os
import subprocess as sp

paths = {
    'notepad': "C:\\Windows\\System32\\notepad.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe",
}

def open_notepad():
    os.startfile(paths['notepad'])

def open_cmd():
    os.system('start cmd')

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def open_calculator():
    sp.Popen(paths['calculator'])

def open_file_explorer():
    os.startfile("C:\\Windows\\explorer.exe")

def open_edge():
    os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

def open_chrome():
    os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

def open_word():
    os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")

def open_excel():
    os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")

def open_powerpoint():
    os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")

def open_vscode():
    os.startfile("C:\\Users\\sanuj\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

def open_windows_media_player():
    os.startfile("C:\\Program Files\\Windows Media Player\\wmplayer.exe")

def open_control_panel():
    os.startfile("C:\\Windows\\System32\\control.exe")

