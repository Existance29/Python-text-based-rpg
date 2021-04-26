end = 1

import json
import time
import random

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

def myRound(n):
    a = str(n)
    b, c = a.split(".")
    if int(c[0]) >= 5:
        d = int(b) + 1
        return d
    else:
        return int(b)

def initBattle():
    weapons = ["Sword", "Shield", "Staff", "Wand"]
    print("\n The buying phase has started \n choose 2 weapons separated by a space")
    for i in range(0, 4):
        print(" " + weapons[i] + ": " + str(i+1))
    class1, class2 = input(" weapons: ").split(" ")
    classes = [guard, tank, mage, medic]
    class1 = int(class1)
    class2 = int(class2)

    myHP = 100
    enHP = 100
    max_myHP = 100
    max_enHP = 100
    mySP = 100
    enMP = 100
    myBP = 0
    enBP = 0
    enspells = 0
    myactiveSkills = []
    activeSkillsInfo = []
    spellOptions = []
    enspellOptions = []
    myBuff = []
    myDebuff = []
    enBuff = []
    enDebuff = []
    enactiveSkills = []
    enactiveSkillsInfo = []
    turn = 0
    less_dmg = 0
    for i in range(1, 4):
        texting = ""
        if i == 1:
            texting = "first"
        elif i == 2:
            texting  = "second"
        else:
            texting = "third"
        while True:
            print("Pick your " + texting + " basic spell by typing the corresponding command:")
            count = 1
            for b in spellData:
                
                print(" " + str(b['name']) + " : " + str(count))
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
        if turn >= 1:
            time.sleep(1)
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
                if n < 4:
                    print("You used " + spellData[spellOptions[n - 1]]['name'])
                    activeSkillsInfo.append({"spellID": spellData[spellOptions[n - 1]], "turnsLeft": int(spellData[spellOptions[n - 1]]["duration"])})
                elif 3 < n < 7:
                    print("You used " + classes[class1-1][n-4]['name'])
                    activeSkillsInfo.append({"spellID": classes[class1 - 1][n - 4], "turnsLeft": int(classes[class1 - 1][n - 4]["duration"])})
                elif 6 < n < 10:
                    print("You used " + classes[class2 - 1][n - 7]['name'])
                    activeSkillsInfo.append({"spellID": classes[class2 - 1][n - 7], "turnsLeft": int(classes[class2 - 1][n - 7]["duration"])})
                myactiveSkills.append(n-1)
                break

        for i in activeSkillsInfo:
            if i["spellID"]['dmg'] > 0:
                for n in enBuff:
                    if n["enemy_dmg_deal_reduc"] > 0:
                        less_dmg += n["enemy_dmg_deal_reduc"]
                    if less_dmg > 100:
                        less_dmg == 100
                less_dmg -= 100
                enHP -= abs(less_dmg/100)*i["spellID"]['dmg']
                print(i["spellID"]['name'] + " dealt " + str(abs(less_dmg/100)*i["spellID"]['dmg']) + " damage")
                less_dmg = 0
            if i["spellID"]['dmgperc'] > 0:
                for n in enBuff:
                    if n["enemy_dmg_deal_reduc"] > 0:
                        less_dmg += n["enemy_dmg_deal_reduc"]
                    if less_dmg > 100:
                        less_dmg == 100
                less_dmg -= 100
                dmg = abs(less_dmg/100)*myRound(i["spellID"]['dmgperc']/100*enHP)
                enHP -= dmg
                print(i["spellID"]['name'] + " dealt " + str(dmg) + " damage")
                less_dmg = 0
            if i["spellID"]['heal'] > 0:
                print(str(i["spellID"]['name']))
                HP = myHP
                myHP += i["spellID"]['heal']
                if myHP > max_myHP:
                    print(str(i["spellID"]['name']) + " healed " + str(i["spellID"]['heal'] - max_myHP - HP) + " health points")
                    myHP = max_myHP
                else:
                    print(str(i["spellID"]['name']) + " healed " + str(i["spellID"]['heal']) + " health points")
            if i["spellID"]['healPerc'] > 0:
                HP = myHP
                heal = myRound(i["spellID"]['healPerc']/100*max_myHP)
                myHP += heal
                if myHP > max_myHP:
                    print(str(i["spellID"]['name']) + " healed " + str(heal - max_myHP - HP) + " health points")
                    myHP = max_myHP
                else:
                    print(str(i["spellID"]['name']) + " healed " + str(heal) + " health points")
            if i["spellID"]["self_dmg_taken_reduc"] > 0:
                myBuff.append({"self_dmg_taken_reduc": i["spellID"]["self_dmg_taken_reduc"]})
            if i['spellID']["enemy_dmg_deal_reduc"] > 0:
                enDebuff.append({"enemy_dmg_deal_reduc": i['spellID']["enemy_dmg_deal_reduc"]})
            if i["spellID"]["stunTime"] > 0:
                enDebuff.append({"stunTime": i["spellID"]["stunTime"]})
            if i["spellID"]["HP_stealperc"] > 0:
                steal_hp = myRound((i["spellID"]["HP_stealperc"]/100)*enHP)
                enHP -= steal_hp
                myHP += steal_hp
                if myHP > max_myHP:
                    print(str(i["spellID"]['name']) + " stole " + str(steal_hp - max_myHP - HP) + " health points")
                    myHP = max_myHP
                else:
                    print(str(i["spellID"]['name']) + " stole " + str(steal_hp) + " health points")
            if i["spellID"]["reflect_dmgperc"]:
                myBuff.append({"reflect_dmgperc": i["spellID"]["reflect_dmgperc"]})
            if i["spellID"]["absorbed_dmgperc"]:
                myBuff.append({"absorbed_dmgperc": i["spellID"]["absorbed_dmgperc"]})

        turn += 1

        for i in activeSkillsInfo:
            if i['turnsLeft'] == 1:

                del myactiveSkills[activeSkillsInfo.index(i)]
                activeSkillsInfo.remove(i)

            else:
                i['turnsLeft'] -= 1

        enClass1 = classes[random.randint(0, 3)]
        enClass2 = classes[random.randint(0, 3)]
        while enClass2 == enClass1:
            enClass2 = classes[random.randint(0, 3)]
        while len(enspellOptions) < 3:
            enspells = random.randint((0, len(spellOptions)))
            while enspells in enspellOptions:
                enspells = random.randint((0, len(spellOptions)))
            enspellOptions.append(enspells)
        n = random.randint(1, 9)
        while (n - 1) in enactiveSkills:
            n = random.randint(1, 9)
        else:
            if n < 4:
                print("Opponent used " + spellData[spellOptions[n - 1]]['name'])
                enactiveSkillsInfo.append({"spellID": spellData[spellOptions[n - 1]], "turnsLeft": int(spellData[spellOptions[n - 1]]["duration"])})
            elif 3 < n < 7:
                print("Opponent used " + classes[class1 - 1][n - 4]['name'])
                enactiveSkillsInfo.append({"spellID": classes[class1 - 1][n - 4], "turnsLeft": int(classes[class1 - 1][n - 4]["duration"])})
            elif 6 < n < 10:
                print("Opponent used " + classes[class2 - 1][n - 7]['name'])
                enactiveSkillsInfo.append({"spellID": classes[class2 - 1][n - 7], "turnsLeft": int(classes[class2 - 1][n - 7]["duration"])})
            enactiveSkills.append(n - 1)
        for i in enactiveSkillsInfo:
            if i["spellID"]['dmg'] > 0:
                for n in myBuff:
                    if n["enemy_dmg_deal_reduc"] > 0:
                        less_dmg += n["enemy_dmg_deal_reduc"]
                    if less_dmg > 100:
                        less_dmg == 100
                less_dmg -= 100
                myHP -= abs(less_dmg/100)*i["spellID"]['dmg']
                print(i["spellID"]['name'] + " dealt " + str(abs(less_dmg/100)*i["spellID"]['dmg']) + " damage")
                less_dmg = 0
            if i["spellID"]['dmgperc'] > 0:
                for n in enBuff:
                    if n["enemy_dmg_deal_reduc"] > 0:
                        less_dmg += n["enemy_dmg_deal_reduc"]
                    if less_dmg > 100:
                        less_dmg == 100
                less_dmg -= 100
                dmg = abs(less_dmg/100)*myRound(i["spellID"]['dmgperc']/100*enHP)
                enHP -= dmg
                print(i["spellID"]['name'] + " dealt " + str(dmg) + " damage")
                less_dmg = 0
            if i["spellID"]['heal'] > 0:
                print(str(i["spellID"]['name']))
                HP = myHP
                myHP += i["spellID"]['heal']
                if myHP > max_myHP:
                    print(str(i["spellID"]['name']) + " healed " + str(i["spellID"]['heal'] - max_myHP - HP) + " health points")
                    myHP = max_myHP
                else:
                    print(str(i["spellID"]['name']) + " healed " + str(i["spellID"]['heal']) + " health points")
            if i["spellID"]['healPerc'] > 0:
                HP = myHP
                heal = myRound(i["spellID"]['healPerc']/100*max_myHP)
                myHP += heal
                if myHP > max_myHP:
                    print(str(i["spellID"]['name']) + " healed " + str(heal - max_myHP - HP) + " health points")
                    myHP = max_myHP
                else:
                    print(str(i["spellID"]['name']) + " healed " + str(heal) + " health points")
            if i["spellID"]["self_dmg_taken_reduc"] > 0:
                myBuff.append({"self_dmg_taken_reduc": i["spellID"]["self_dmg_taken_reduc"]})
            if i['spellID']["enemy_dmg_deal_reduc"] > 0:
                enDebuff.append({"enemy_dmg_deal_reduc": i['spellID']["enemy_dmg_deal_reduc"]})
            if i["spellID"]["stunTime"] > 0:
                enDebuff.append({"stunTime": i["spellID"]["stunTime"]})
            if i["spellID"]["HP_stealperc"] > 0:
                steal_hp = myRound((i["spellID"]["HP_stealperc"]/100)*enHP)
                enHP -= steal_hp
                myHP += steal_hp
                if myHP > max_myHP:
                    print(str(i["spellID"]['name']) + " stole " + str(steal_hp - max_myHP - HP) + " health points")
                    myHP = max_myHP
                else:
                    print(str(i["spellID"]['name']) + " stole " + str(steal_hp) + " health points")
            if i["spellID"]["reflect_dmgperc"]:
                myBuff.append({"reflect_dmgperc": i["spellID"]["reflect_dmgperc"]})
            if i["spellID"]["absorbed_dmgperc"]:
                myBuff.append({"absorbed_dmgperc": i["spellID"]["absorbed_dmgperc"]})






while(end):
    command = input("Input a command: ")

    if command.startswith('basicspellinfo'):

     
        for key in spellData:
                print("\n "+key['name']+": "+ key['desc'])
                

    if command.startswith("fight"):

      initBattle()

    if command.startswith("classspellinfo"):
        classes = [guard,tank,mage,medic]
        print("\n Guard Class spells:")
        for key in guard:
                print(key['name']+": "+ key['desc'])
        print("\n Tank Class spells:")
        for key in tank:
                print(key['name']+": "+ key['desc'])
        print("\n Mage Class spells:")
        for key in mage:
                print(key['name']+": "+ key['desc'])
        print("\n Medic Class spells:")
        for key in medic:
                print(key['name']+": "+ key['desc'])
        
        
    

    if command.startswith("exit"):
      end = 0
            

        

