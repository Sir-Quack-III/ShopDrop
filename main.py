import interpreter
import sys

def split(str):
    return str.split("***")

# def main():
filestr = ""

with open(sys.argv[1], "r") as f:
    filestr = f.read()

interpreter = interpreter.interpreter(filestr)

interpreter.run()

print(split(filestr))

# if __name__ == "__main__":
#     main()