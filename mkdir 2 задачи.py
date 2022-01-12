import os

def mkdir(*directories):
    dir_ = os.path.join(*directories)
    if not os.path.isdir(dir_):
        os.makedirs(dir_)



# решение с модулем pathlib
from pathlib import Path
def mkdir_(directories):
    outpath = Path(directories)
    if not outpath.is_dir():
        outpath.mkdir(parents=True)
        print(outpath.is_dir())
