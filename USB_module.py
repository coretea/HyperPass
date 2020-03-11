import subprocess

"""
#get disk index
batcmd= "wmic diskdrive where \"Model=\'USB2.0 Flash Disk USB Device\'\" get index"
result = subprocess.check_output(batcmd, shell=True)
result_str = str(result)
disk_index = result_str[15]


#write the script to Diskpart
f = open("usb_part.txt", "w")
f.write("list disk\nselect Disk "+disk_index+"\nclean\ncreate partition primary size=500\nformat quick fs=fat32 label=\"HyperPassEncrypt\"\nassign letter=J\nactive\ncreate partition primary\nformat fs=ntfs quick label=\"HyperPassStorage\"\nassign letter=K\nlist vol\nexit")
f.close()

diskpart_script= "diskpart \s usb_part.txt"
result = subprocess.check_output(batcmd, shell=True)

"""
import os

def isPluggedIn(driveLetter):
    if os.system("cd " +driveLetter +":") == 0: return True
    else: return False

def main():
    if not (isPluggedIn("R") and isPluggedIn("S")):
        exit()
    else:
        print("Connected")

if __name__ == "__main__":
    main()
