import os
import sys

sys.tracebacklimit = 5

def add(array, item):
    array.append(item)
    return array

def remove(array, index):
    array.pop(index)
    return array

def find(array, item):
    return array.index(item)

# Files and directories
def writeFile(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def readFile(filename):
    with open(filename, 'r') as file:
        return file.read()

def appendFile(filename, content):
    with open(filename, 'a') as file:
        file.write(content)

try:
    if os.path.isfile(sys.argv[1]) and os.path.splitext(sys.argv[1])[-1].lower() == ".alpha":
        pass
    else:
        if not os.path.isfile(sys.argv[1]):
            print("Error: File is not found.")
        elif os.path.splitext(sys.argv[1])[-1].lower() != ".alpha":
            print("Error: File is not an Alpha file.")
        sys.exit()
except IndexError:
    print("Error: No .alpha file given.")
    sys.exit()

with open(sys.argv[1], "r") as f:

    code = f.readlines()
    totalcode = ""
    loopcount = 0

    for line in code:
        if line.startswith("//"):
            continue
        else:

            line = line.strip()

            if any(var in line for var in [":=", ":str=", ":int=", ":dec=", ":bool=", ":array=", ":dict="]):
                
                if ":str=" in line:
                    totalcode += "\t" * loopcount + line[:line.index(":str=")] + " = str(" + line[line.index(":str=")+5:] + ") \n"
                elif ":int=" in line:
                    totalcode += "\t" * loopcount + line[:line.index(":int=")] + " = int(" + line[line.index(":int=")+5:] + ") \n"
                elif ":dec=" in line:
                    totalcode += "\t" * loopcount + line[:line.index(":dec=")] + " = float(" + line[line.index(":dec=")+5:] + ") \n"
                elif ":bool=" in line:
                    totalcode += "\t" * loopcount + line[:line.index(":bool=")] + " = bool(" + line[line.index(":bool=")+6:] + ") \n"
                elif ":array=" in line:
                    totalcode += "\t" * loopcount + line[:line.index(":array=")] + " = list(" + line[line.index(":array=")+7:] + ") \n"
                elif ":dict=" in line:
                    totalcode += "\t" * loopcount + line[:line.index(":dict=")] + " = dict(" + line[line.index(":dict=")+6:] + ") \n"
                else:    
                    totalcode += "\t" * loopcount + line[0:line.index(":=")] + " = " + line[line.index(":=")+2:].strip() + "\n"

            elif line.startswith("log"):
                totalcode += "\t" * loopcount + "print(" + line[4:].strip() + ") \n"    

            elif line.startswith("tlog"):
                totalcode += "\t" * loopcount + "print(type(" + line[5:].strip() + ")) \n"

            # import module
            elif line.startswith("#import"):
                totalcode += "\t" * loopcount + "import " + line[7:] + "\n"

            # if statement
            elif line.startswith("if"):
                totalcode += "\t" * loopcount + "if " + line[3:].strip() + ":\n"
                loopcount += 1

            elif line.startswith("for"):
                totalcode += "\t" * loopcount + "for " + line[4:].strip() + ":\n"
                loopcount += 1

            elif line.startswith("iterate <- "):
                # repeat x amount of times
                totalcode += "\t" * loopcount + "for i in range(" + line[11:].strip() + "):\n"
                loopcount += 1

            elif line.startswith("while"):
                totalcode += "\t" * loopcount + "while " + line[5:].strip() + ":\n"
                loopcount += 1

            elif line.startswith("else if"):
                loopcount -= 1
                totalcode += "\t" * loopcount + "elif " + line[7:].strip() + ":\n"
                loopcount += 1

            elif line.startswith("else"):
                loopcount -= 1
                totalcode += "\t" * loopcount + "else:\n"
                loopcount += 1

            elif line.startswith("endclass"):
                loopcount -= 1

            elif line.startswith("endfunc <-"):
                # this is a return statement
                totalcode += "\t" * loopcount + "return " + line[11:].strip() + "\n"
                loopcount -= 1

            elif line.startswith("end"):
                loopcount -= 1

            # function creation
            elif line.startswith("func"):
                totalcode += "\t" * loopcount + "def " + line[5:].strip() + ":\n"
                loopcount += 1

            # class creation      

            elif line.startswith("class"):
                if "<-" in line:
                    totalcode += "class " + line[6:line.index("<-")] + "(" + line[line.index("<-")+3:] + "):\n"
                    loopcount += 1
                totalcode += "class " + line[6:].strip() + ":\n"
                loopcount += 1

            else:
                totalcode += "\t" * loopcount + line.strip() + "\n"

totalcode = totalcode.replace("userInput", "input")
totalcode = totalcode.replace(":exit:", "break")

totalcode = totalcode.replace("private::", "__")

totalcode = totalcode.replace("??", "self")

#print(totalcode)
#print("-" * 25)

try:
    #print(totalcode)
    exec(totalcode)
except Exception as ex:
    print(f"Error: {str(ex).capitalize()}.")
