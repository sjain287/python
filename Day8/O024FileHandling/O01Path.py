from pathlib import Path

print(Path(r'E:\shalu\Python'))
print(Path())

print(Path("radhika"))  # searches for folder named Radhika
print(Path()/Path("Srujana"))
print(Path()/"Srujana"/"Santoshi.zip")
print(Path.home())
print('_' * 30)
path = Path("test/abc.py")
print(path.exists())
print(path.is_file())
print(path.is_dir())
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
print(path.absolute())
print(path.with_suffix('.txt'))
print(path.with_name('Shalu.txt'))
