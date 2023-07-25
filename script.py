file = open("input.txt")

# data = file.readlines()
# print(data)

lines = []

while True:
    line = file.readline()
    line = line.replace("\n", "")
    
    if not line:
        break
        
    lines.append(line)

print(lines)
