from pathlib import Path

p = Path('chocolate.txt')
p.write_text('Hello! I Like chocolate.')
print(p.read_text())
