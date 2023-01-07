import interpreter
import sys

filestr = ""

with open(sys.argv[1], "r") as f:
    filestr = f.read()

interpreter = interpreter.interpreter(filestr)

interpreter.run()