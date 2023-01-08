import json
from enum import Enum

class food(Enum):
    ONION = 1
    POTATO = 2

class shopping_entry():
    def __init__(self, type, num) -> None:
        self.type = type
        self.num = num

    def __repr__(self) -> str:
        return f"shopping_entry({self.type}, {self.num})"

class house:
    def __init__(self, pos, type, value) -> None:
        self.pos = pos
        self.type = type
        self.value = value

    def __repr__(self) -> str:
        return f"house({self.pos}, {self.type}, {self.value})"

class interpreter:
    def __init__(self, code):
        self.code = code
        self.map = []

    def find_char(self, pos, char) -> list:
        for y, i in enumerate(self.map):
            for x, j in enumerate(i):
                if (x in range(pos[1] - 1, pos[1] + 1)):
                    if (y in range(pos[0] - 1, pos[0] + 1)):
                        if j == char:
                            return [y, x]

        return None
    
    def run(self):
        cd = self.code.split("***")

        # save shopping list
        slistraw = json.loads(cd[0]) # loads raw shopping list
        slist = [] # shopping list

        for i, l in enumerate(slistraw):
            slist.append([])
            for e in slistraw[l]:
                if e == "onion" or e == "o":
                    slist[i].append(shopping_entry(food.ONION, slistraw[l][e]))
                elif e == "potato" or e == "p":
                    slist[i].append(shopping_entry(food.POTATO, slistraw[l][e]))
        
        # save self.map
        buf = []
        for c in cd[1]:
            if c == "\n":
                self.map.append(buf)
                buf = []
                continue
            buf.append(c)

        # find the car
        carPos = []
        carInv = [] # car inventory
        carDir = 0 # car direction

        for y, i in enumerate(self.map):
            for x, j in enumerate(i):
                if j == "=":
                    carPos = [y, x]
                    break

        # print(carPos[1])

        # actually running the code
        
        eof = False
        houses = []
        currentList = 0

        while not eof:
            if self.map[carPos[0]][carPos[1]] == "l":
                # check if shop is in vicinity
                storage_chars = ["$", "#", "+", "-", "@"]
                c2store = ""
                c2sloc = [] # and the award for worst variable name of the year goes to...

                for c in storage_chars:
                    if self.find_char(carPos, c):
                        c2store = c
                        c2sloc = self.find_char(carPos, c)

                if c2store == "@":
                    for i in slist:
                        carInv.append(i)
                
                    slist.remove(slist[0])

                elif c2store == "$" or c2store == "#" or c2store == "+" or c2store == "-":
                    for h in houses:
                        if h.pos == c2sloc:
                            carInv.append([shopping_entry(h.type, h.value)])
                            houses.remove(h)
                            break
            elif self.map[carPos[0]][carPos[1]] == "e":
                storage_chars = ["%", "$", "#", "+", "-"]
                c2store = ""
                c2sloc = [] # and the award for worst variable name of the year goes to...

                for c in storage_chars:
                    if self.find_char(carPos, c):
                        c2store = c
                        c2sloc = self.find_char(carPos, c)

                if c2store == "":
                    print("No house to empty into you moron")
                    break

                if c2store == "%":
                    if carInv[0][0].type == food.ONION:
                        print(chr(carInv[0][0].num), end="")
                    elif carInv[0][0].type == food.POTATO:
                        print(carInv[0][0].num, end="")

                    if len(slist) == 0:
                        eof = True

                    carInv.remove(carInv[0])

                if c2store == "$":
                    if carInv[0][0].type == food.POTATO:
                        print("This is an onion house. Dont throw those potatoes at me!")
                        break
                    
                    houses.append(house(c2sloc, food.ONION, carInv[0][0].num))
                    carInv = []

                elif c2store == "#":
                    if carInv[0][0].type == food.ONION:
                        print("This is a potato house. Dont throw those onions at me!")
                        break

                    houses.append(house(c2sloc, food.POTATO, carInv[0][0].num))
                    carInv = []

                elif c2store == "+":
                    if carInv[0][0].type == food.ONION:
                        print("This is a potato house. Dont throw those onions at me!")
                        break
                    houses.append(house(c2sloc, food.POTATO, carInv[0][0].num + carInv[1][0].num))
                    carInv = []

                elif c2store == "-":
                    if carInv[0][0].type == food.ONION:
                        print("This is a potato house. Dont throw those onions at me!")
                        break
                    houses.append(house(c2sloc, food.POTATO, carInv[0][0].num - carInv[1][0].num))
                    carInv = []

            elif self.map[carPos[0]][carPos[1]] == ".":
                eof = True

            elif self.map[carPos[0]][carPos[1]] in ["0", "1", "2", "3"]:
                allZero = True
                for i in carInv:
                    for e in i:
                        if e.num != 0:
                            allZero = False
                            break

                if allZero:
                    carDir = int(self.map[carPos[0]][carPos[1]])

            elif self.map[carPos[0]][carPos[1]] == "c": # clear inventory
                carInv = []

            elif self.map[carPos[0]][carPos[1]] == "d": # duplicate shopping list
                slist.append(slist[0])

            match self.map[carPos[0]][carPos[1]]:
                case ">":
                    carDir = 0
                case "v":
                    carDir = 1
                case "<":
                    carDir = 2
                case "^":
                    carDir = 3

            match carDir:
                case 0:
                    carPos[1] += 1
                case 1:
                    carPos[0] += 1
                case 2:
                    carPos[1] -= 1
                case 3:
                    carPos[0] -= 1
            # try:
            #     print(self.map[houses[0].pos[1]][houses[0].pos[0]])
            # except:
            #     pass
            #print(carInv)
