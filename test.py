# path=str("C:/Users/AHMED/Documents/مواد الابتدائية.txt")
# text=str("yiubyhgugh")
# with open(path,"w") as f :
#     f.write(text)
# print("uig")

f = open("D:/pythonproject/textEditor/demofile2.txt", "a")
f.write("\n biuyyhuyghughntent!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())