with open("./file.txt", "w") as file:
    file.write('hello world \n')

with open("./file.txt", "r") as file:
    content = file.read()
    print(content)
