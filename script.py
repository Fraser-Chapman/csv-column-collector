file = open("input.txt")

lines = []

while True:
    line = file.readline()
    line = line.replace("\n", "")
    
    if not line:
        break
        
    lines.append(line)

print(lines)
