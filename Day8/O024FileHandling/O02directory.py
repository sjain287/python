from pathlib import Path

path = Path()
print(path)
path = Path("test")
print(path)
print(path.exists())

path = Path("Shalu")
# path.mkdir()
# path.rmdir()
# path.rename("Jain")

for p in path.iterdir():  # return generator
    print(p)

paths = [p for p in path.iterdir()]  # can't use patterns
print(paths)
print("_" * 50)
path = Path()
# iterdir,glob,rglob
files = [p for p in path.glob("**/*.*")]
print(files)
print("_" * 50)
files = [p for p in path.rglob("**/*.*")]
print(files)
