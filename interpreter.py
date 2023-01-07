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
                if x in range(pos[0] - 1, pos[0] + 1) and y in range(pos[1] - 1, pos[1] + 1):
                    if j == char:
                        return [x, y]

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

        for y, i in enumerate(self.map):
            for x, j in enumerate(i):
                if j == "=":
                    carPos = [x, y]
                    break

        # print(carPos[1])

        # actually running the code
        
        eof = False
        houses = []
        currentList = 0

        while not eof:
            if self.map[carPos[1]][carPos[0]] == "l":
                # check if shop is in vicinity
                carInv = []
                shop_pos = self.find_char(carPos, "@")
                if shop_pos == None:
                    print("You fucking idiot. What were you thinking? What the hell were you thinking? You are attempting to load items from your shopping list, but there is no store within one character of your car! You dumbass.")
                    break

                carInv.append(slist[0])
                slist.remove(slist[0])
            elif self.map[carPos[1]][carPos[0]] == "e":
                storage_chars = ["%", "$", "#"]
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

                    carInv = []

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

            elif self.map[carPos[1]][carPos[0]] == ".":
                eof = True
            
            print(houses)
            carPos[0] += 1