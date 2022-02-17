from platform import win32_edition
import os
import sys
import pathlib
from pathlib import Path
import subprocess

def get_platform():
    if sys.platform == 'linux':
        try:
            proc_version = open('/proc/version').read()
            if 'Microsoft' in proc_version:
                return 'wsl'
        except:
            pass

    return sys.platform

def open_file(path: Path):
    filename = str(path)
    platform = get_platform()

    # macos
    if platform == 'darwin':
        args = ['open', filename]
        subprocess.run(args)

    # windows
    elif platform in ['win32', 'win64']:
        os.startfile(filename.replace('/', '\\'))

    # windows WSL
    elif platform == 'wsl':
        subprocess.call('cmd.exe /C start'.split() + [filename])

    # linux
    else:
        args = ['xdg-open', filename]
        subprocess.call(args)

