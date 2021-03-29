end = 1

import json

with open('spells.json') as f:
  spellData= json.load(f)

def initBattle():

    myHP = 100
    enHP = 100
    move1 = 0
    move2 = 1
    myactiveSkills = []

    while(myHP > 0 or enHP > 0):
        print("\nYour Health: " + str(myHP))
        print("Enemy's Health: " + str(enHP))
        
        print("\n Pick a skill by typing the corresponding command: \n " + spellData[move1]['name'] + ": 1 \n " + spellData[move2]['name']+": 2 \n")
        while True:
            n = input("command: ")
            if myactiveSkills.includes(n-1):
                print("That skill is already in use! try again")
            else:
                print("You used" + spellData[n]['name'])
                myactiveSkills.append(n-1)
                break
        enHP -= spellData[n]["damage"]
        

while(end):
    command = input("Input a command: ")

    if command.startswith('info'):

        args = command.split()[1].lower()
        for key in spellData:
            
            if args == key['name'].lower().replace(" ", ""):
                print("\n "+key['name']+": "+ key['desc'])
                break

    if command.startswith("fight"):

      initBattle()

    if command.startswith("exit"):
      end = 0
            

        

