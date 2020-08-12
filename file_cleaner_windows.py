import os
import time
print("""
Type 'emirkan' to start the clean operation.
""")

type = input("==>>  ")

if type == 'emirkan' or type == 'EMİRKAN':
    os.system("start %temp%")
    os.system("start Temp")
    os.system("start prefetch")

    print("Type 'ebby' to continue clean operation.")

    ebi = input("==>>  ")

    if ebi == "ebby" or ebi == "EBBY":
        print("Select system files , don't worry they're not win32 files :D")
        time.sleep(5)
        os.system("start Cleanmgr")

        print("Finish your job and feel fast :D Good Luck !")
    
    else:
        print("Type 'ebby' !!!")
else:
    print("Type 'emirkan' !!!")
