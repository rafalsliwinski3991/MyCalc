#!C:\Users\rafal\Desktop\mycalc\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pyramid','console_scripts','prequest'
__requires__ = 'pyramid'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('pyramid', 'console_scripts', 'prequest')()
    )
