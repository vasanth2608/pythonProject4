file = open('test.txt')
print(file.readline())
print(file.read(5))
file.close()
with open('test.txt','r')as reader:
    content = reader.readline()
    reversed(content)
    with open('test.txt','w')as writer:
        for line in reversed(content):
            writer.wr ite(line)