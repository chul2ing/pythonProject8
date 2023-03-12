file = open("point20.txt", "r")
text = file.read()
data = text.split()
data = [eval(i) for i in data]
print(data)

result = []
for i in range(1, len(data), 2):
    result.append([data[i], data[i +1]])
print(result)