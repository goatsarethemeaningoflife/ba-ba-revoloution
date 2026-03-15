text = input()
str =[]
def parse(x):
    if x == "u":
        return "ud"
    elif x == "d":
        return "du"
    elif x == "l":
        return "lr"
    elif x == "r":
        return "rl"
    else:
         return "no"
def parseplus(x):
    if x == "u" or x == "d" or x == "l" or x == "r":
        return parse(x)
    elif x == "q":
        return "ulrd"
    elif x == "e":
        return "urld"
    elif x == "z":
        return "dlru"
    elif x == "c":
        return "drlu"
new_string = "".join(map(parseplus, text))
with open("out.txt", "w") as f:
    f.write(f"=t tile:5/3&arrow:u:rot-45:5/4 tile:green&arrow:u:lime tile:1/2&arrow:u:rot45:1/3\ntile:gold&arrow:l:yellow tile&baba:[!/{new_string}] tile:4/3&arrow:blue\ntile:brown&arrow:d:rot45:orange tile:maroon&arrow:d:red tile:3/0&arrow:d:rot-45:purple\n")
print(f"=t tile:5/3&arrow:u:rot-45:5/4 tile:green&arrow:u:lime tile:1/2&arrow:u:rot45:1/3\ntile:gold&arrow:l:yellow tile&baba:[!/{new_string}] tile:4/3&arrow:blue\ntile:brown&arrow:d:rot45:orange tile:maroon&arrow:d:red tile:3/0&arrow:d:rot-45:purple\n")
#q is up left, e is up right, z is down left, c is down right