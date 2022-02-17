import sys
import pathlib
from pathlib import Path
import subprocess

def open_file(path: Path):
    platform = sys.platform
    if platform == 'linux':
        args = ["xdg-open", str(path)]
        proc = subprocess.run(args)
    else:
        raise NotImplementedError
