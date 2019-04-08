from pathlib import Path
from zipfile import ZipFile
# ---------------simple zip-------------1
# zip = ZipFile("files.zip", "w")

# for path in Path("test/test1").rglob("*.*"):
#     zip.write(path)

# zip.close()
# ---------------implicit close of a file-------------2
# with ZipFile('files.zip', 'w') as zip:
#     for path in Path("test/test1").rglob("*.*"):
#         zip.write(path)
# # read info
# with ZipFile("files.zip") as zip:
#     print(zip.namelist())
#     info = zip.getinfo('test/test1/cat.txt')
#     print(info.file_size)
#     print(info.compress_size)

#
with ZipFile("files.zip") as zip:
    zip.extractall("test")
