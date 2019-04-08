import shutil
from pathlib import Path
from time import ctime


# --------------------------------------------1
path = Path("test/test1/cat.txt")
print(path.exists())
print(path.absolute())

# --------------------------------------------2
# path = Path("test/test1/lion.txt")
# print(path.exists())
# path.unlink()  # deletes the file

# --------------------------------------------3
path = Path("test/test1/cat.txt")
print(path.stat())
print('_' * 50)
print(path.stat().st_ctime)
print(ctime(path.stat().st_ctime))  # convert time
# --------------------------------------------4
path = Path("test/test1/cat.txt")
print(path.read_bytes())
print(path.read_text())

# --------------------------------------------5
path = Path("test/test1/cat.txt")
path.write_text('RCB: We will win')  # overwrites
# --------never reliable on this------------------------------------6
source = Path("test/test1/cat.txt")
target = Path("test/test1/cat1.txt")
target.write_text(source.read_text())
# --------------import shutil--------------------7
source = Path("test/test1/cat.txt")
target = Path("test/test1/cat1.txt")
shutil.copy(source, target)
