end = 1

import json

with open('main_character_moves.json') as f:
  spellData = json.load(f)
with open('armour.json') as f:
    armour = json.load(f)
with open('potions.json') as f:
    potions = json.load(f)
with open('guard_moves.json') as f:
    guard = json.load(f)
with open('tank_moves.json') as f:
    tank = json.load(f)
with open('mage_moves.json') as f:
    mage = json.load(f)
with open('medic_moves.json') as f:
    medic = json.load(f)

def initBattle():
    weapons = ["Sword", "Shield", "Staff", "Wand"]
    print("\n The buying phase has started \n choose 2 weapons seperated by a space")
    print(" " + weapons[0] + ": 1")
    print(" " + weapons[1] + ": 2")
    print(" " + weapons[2] + ": 3")
    print(" " + weapons[3] + ": 4")
    class1, class2 = input(" weapons: ").split(" ")
    classes = [guard, tank, mage, medic]
    class1 = int(class1)
    class2 = int(class2)

    myHP = 100
    enHP = 100
    mySP = 100
    enMP = 100
    myBP = 0
    enBP = 0
    myactiveSkills = []
    activeSkillsInfo = []
    spellOptions = []
    for i in range(1,4):
        texting = ""
        if i == 1:
            texting = "first"
        elif i == 2:
            texting  = "second"
        else:
            texting = "third"
        while True:
            print("Pick your "+texting+ " basic spell by typing the correesponding command:")
            count = 1
            for b in spellData:
                
                print(" "+ str(b['name'])+" : "+str(count))
                count += 1
            a = int(input())
          
            if a-1 not in spellOptions:
                break
            else:
                print("you already have selected this skill! Select another one ")
            
        spellOptions.append(a-1)
            

    
    n = 0
    while(myHP > 0 and enHP > 0):
        print("\n Your Health: " + str(myHP))
        print(" Enemy's Health: " + str(enHP))
        
        print("\n Pick a skill by typing the corresponding command:")
        print(" " + spellData[spellOptions[0]]['name'] + ": 1")
        print(" " + spellData[spellOptions[1]]['name'] + ": 2")
        print(" " + spellData[spellOptions[2]]['name'] + ": 3")
        print(" " + classes[class1-1][0]['name'] + ": 4")
        print(" " + classes[class1-1][1]['name'] + ": 5")
        print(" " + classes[class1-1][2]['name'] + ": 6")
        print(" " + classes[class2-1][0]['name'] + ": 7")
        print(" " + classes[class2-1][1]['name'] + ": 8")
        print(" " + classes[class2-1][2]['name'] + ": 9")

        
        while True:
            n = int(input(" command: "))
            if (n-1) in myactiveSkills:
                print("That skill is already in use! try again")
            else:
                print("You used " + spellData[spellOptions[n-1]]['name'])
                myactiveSkills.append(n-1)
                activeSkillsInfo.append({"spellID": spellOptions[n-1], "turnsLeft": int(spellData[spellOptions[n-1]]["duration"])})
                break
            
        enHP -= int(spellData[spellOptions[n-1]]["dmg"])

        print(myactiveSkills)
        print(activeSkillsInfo)
        for i in activeSkillsInfo:
            if i['turnsLeft'] == 1:
                
                del myactiveSkills[activeSkillsInfo.index(i)]
                activeSkillsInfo.remove(i)
                
            else:
                i['turnsLeft'] -= 1

        

while(end):
    command = input("Input a command: ")

    if command.startswith('spellinfo'):

        args = command.split()[1].lower()
        for key in spellData:
            
            if args == key['name'].lower().replace(" ", ""):
                print("\n "+key['name']+": "+ key['desc'])
                break

    if command.startswith("fight"):

      initBattle()

    

    if command.startswith("exit"):
      end = 0
            

        

