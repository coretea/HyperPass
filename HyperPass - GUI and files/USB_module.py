import subprocess
from ctypes import windll, create_unicode_buffer, c_wchar_p, sizeof
from string import ascii_uppercase
import os

def get_win_drive_names():
    volumeNameBuffer = create_unicode_buffer(1024)
    fileSystemNameBuffer = create_unicode_buffer(1024)
    serial_number = None
    max_component_length = None
    file_system_flags = None
    drive_names = []
    #  Get the drive letters, then use the letters to get the drive names
    bitmask = (bin(windll.kernel32.GetLogicalDrives())[2:])[::-1]  # strip off leading 0b and reverse
    drive_letters = [ascii_uppercase[i] + ':/' for i, v in enumerate(bitmask) if v == '1']

    for d in drive_letters:
        rc = windll.kernel32.GetVolumeInformationW(c_wchar_p(d), volumeNameBuffer, sizeof(volumeNameBuffer),
                                                   serial_number, max_component_length, file_system_flags,
                                                   fileSystemNameBuffer, sizeof(fileSystemNameBuffer))
        if rc:
            drive_names.append(f'{volumeNameBuffer.value}({d[:2]})')  # disk_name(C:)
    return drive_names

def checkIfConnected():
    drives = get_win_drive_names()
    for i in range(0,len(drives)):
        if "HyperPassStorage" in drives[i]:
            print("Connected")
            return
    exit("Didn't find usb device")



