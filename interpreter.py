import json

class interpreter:
    def __init__(self, code):
        self.code = code
        self.map = []

    def find_char(self, pos, char):
        for y in self.map:
            for x, j in enumerate(y):
                if x in range(pos[0] - 1, pos[0] + 1) and y in range(pos[1] - 1, pos[1] + 1):
                    if j == char:
                        return [x, y]
    
    def run(self):
        cd = self.code.split("***")
        
        # save self.map
        buf = []
        for c in cd[2]:
            if c == "\n":
                self.map.append(buf)
                buf = []
                continue
            buf.append(c)

        # save shopping list
        shopping_list = json.loads(cd[0])
        print(shopping_list)

        print(self.map)

        # find the car
        carPos = []

        for y, i in enumerate(self.map):
            print(i)
            for x, j in enumerate(i):
                if j == "=":
                    carPos = [x, y]
                    break

        # print(carPos[1])

        # actually running

        print(len(self.map[0]))

        
        eof = False

        while not eof:
            if self.map[carPos[1]][carPos[0]] == "l":
                print("load")
                print(self.find_char(carPos, "@"))
            elif self.map[carPos[1]][carPos[0]] == "e":
                print("empty")
            elif self.map[carPos[1]][carPos[0]] == ".":
                print("end")
                eof = True
            
            carPos[0] += 1