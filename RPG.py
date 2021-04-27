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
    enSP = 100
    myStun = 0
    enStun = 0
    enspells = 0
    my_absorbed = 0
    en_absorbed = 0
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

    enClass1 = random.randint(0, 3)
    enClass2 = random.randint(0, 3)
    while enClass2 == enClass1:
        enClass2 = random.randint(0, 3)
    while len(enspellOptions) < 3:
        enspells = random.randint(0, len(spellOptions))
        while enspells in enspellOptions:
            enspells = random.randint(0, len(spellOptions))
        enspellOptions.append(enspells)
            

    
    n = 0
    while(myHP > 0 and enHP > 0):
        if myStun == 0:
            print("\n Your Health: " + str(myHP))
            print(" Your skill points: " + str(mySP))
            print("\n Enemy's Health: " + str(enHP))
            print(" Enemy's Skill Points: " + str(enSP))
        else:
            print("You are stunned")

        if turn >= 1:
            time.sleep(2)
            print("\n---------------------------------------------------")
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

        
        while myStun == 0:
            n = int(input(" command: "))
            if (n-1) in myactiveSkills:
                print("That skill is already in use! try again")
            elif 3 < n < 7 and classes[class1 - 1][n - 4]["SP_cost"] > mySP:
                print("You do not have enough skill points! try again")
            elif 6 < n < 10 and classes[class2 - 1][n - 7]["SP_cost"] > mySP:
                print("You do not have enough skill points! try again")
            else:
                if n < 4:
                    print("\nYou used " + spellData[spellOptions[n - 1]]['name'])
                    activeSkillsInfo.append({"spellID": spellData[spellOptions[n - 1]], "turnsLeft": int(spellData[spellOptions[n - 1]]["duration"])})
                elif 3 < n < 7:
                    cost = classes[class2-1][n-4]["SP_cost"]
                    print("\nYou used " + classes[class1-1][n-4]['name'])
                    mySP -= cost
                    activeSkillsInfo.append({"spellID": classes[class1 - 1][n - 4], "turnsLeft": int(classes[class1 - 1][n - 4]["duration"])})
                elif 6 < n < 10:
                    cost = classes[class2 - 1][n - 7]["SP_cost"]
                    print("\nYou used " + classes[class2 - 1][n - 7]['name'])
                    mySP -= cost
                    activeSkillsInfo.append({"spellID": classes[class2 - 1][n - 7], "turnsLeft": int(classes[class2 - 1][n - 7]["duration"])})
                myactiveSkills.append(n-1)
                break
        if myStun == 0:
            for i in activeSkillsInfo:
                if i["spellID"]['dmg'] > 0:
                    for n in myDebuff:
                        if n["enemy_dmg_deal_reduc"] > 0:
                            less_dmg += n["enemy_dmg_deal_reduc"]
                    for n in enBuff:
                        try:
                            if n["self_dmg_taken_reduc"] > 0:
                                less_dmg += n["self_dmg_deal_reduc"]
                        except:
                            pass
                    if less_dmg > 100:
                        less_dmg == 100
                    less_dmg -= 100
                    dmg = abs(less_dmg / 100) * i["spellID"]['dmg']
                    for n in enBuff:
                        try:
                            if n["reflect_dmgperc"] > 0:
                                reflected_dmg = myRound((n["reflect_dmgperc"] / 100) * dmg)
                                dmg -= reflected_dmg
                                myHP -= reflected_dmg
                                print("Enemy reflected " + str(reflected_dmg) + " damage")
                                time.sleep(2)
                        except:
                            pass
                    for n in enBuff:
                        try:
                            if n["absorbed_dmgperc"] > 0:
                                absorbed_dmg = myRound((n["absorbed_dmgperc"] / 100) * dmg)
                                dmg -= absorbed_dmg
                                print("Enemy absorbed " + str(absorbed_dmg) + " damage")
                                time.sleep(2)
                                en_absorbed = absorbed_dmg
                        except:
                            pass
                    if my_absorbed > 0:
                        dmg += my_absorbed
                    enHP -= dmg
                    print(i["spellID"]['name'] + " dealt " + str(dmg) + " damage")
                    time.sleep(2)
                    less_dmg = 0
                if i["spellID"]['dmgperc'] > 0:
                    for n in myDebuff:
                        if n["enemy_dmg_deal_reduc"] > 0:
                            less_dmg += n["enemy_dmg_deal_reduc"]
                    for n in enBuff:
                        if n["self_dmg_taken_reduc"] > 0:
                            less_dmg += n["self_dmg_taken_reduc"]
                    if less_dmg > 100:
                        less_dmg == 100
                    less_dmg -= 100
                    dmg = abs(less_dmg / 100) * myRound(i["spellID"]['dmgperc'] / 100 * enHP)
                    for n in enBuff:
                        if n["reflect_dmgperc"] > 0:
                            reflected_dmg = myRound((n["reflect_dmgperc"]/100)*dmg)
                            dmg -= reflected_dmg
                            myHP -= reflected_dmg
                            print("Enemy reflected " + str(reflected_dmg) + " damage")
                            time.sleep(2)
                    for n in enBuff:
                        if n["absorbed_dmgperc"] > 0:
                            absorbed_dmg = myRound((n["absorbed_dmgperc"]/100)*dmg)
                            dmg -= absorbed_dmg
                            print("Enemy absorbed " + str(absorbed_dmg) + " damage")
                            time.sleep(2)
                            en_absorbed = absorbed_dmg
                    if my_absorbed > 0:
                        dmg += my_absorbed
                    enHP -= dmg
                    print(i["spellID"]['name'] + " dealt " + str(dmg) + " damage")
                    time.sleep(2)
                    less_dmg = 0
                if i["spellID"]['heal'] > 0:
                    HP = myHP
                    myHP += i["spellID"]['heal']
                    if myHP > max_myHP:
                        print(str(i["spellID"]['name']) + " healed " + str(
                            i["spellID"]['heal'] - max_myHP - HP) + " health points")
                        time.sleep(2)
                        myHP = max_myHP
                    else:
                        print(str(i["spellID"]['name']) + " healed " + str(i["spellID"]['heal']) + " health points")
                        time.sleep(2)
                if i["spellID"]['healPerc'] > 0:
                    HP = myHP
                    heal = myRound(i["spellID"]['healPerc'] / 100 * max_myHP)
                    myHP += heal
                    if myHP > max_myHP:
                        print(str(i["spellID"]['name']) + " healed " + str(heal - max_myHP - HP) + " health points")
                        time.sleep(2)
                        myHP = max_myHP
                    else:
                        print(str(i["spellID"]['name']) + " healed " + str(heal) + " health points")
                        time.sleep(2)
                if i["spellID"]["self_dmg_taken_reduc"] > 0:
                    myBuff.append({"self_dmg_taken_reduc": i["spellID"]["self_dmg_taken_reduc"]})
                if i['spellID']["enemy_dmg_deal_reduc"] > 0:
                    enDebuff.append({"enemy_dmg_deal_reduc": i['spellID']["enemy_dmg_deal_reduc"]})
                if i["spellID"]["stunTime"] > 0:
                    enStun = i["spellID"]["stunTime"]
                if i["spellID"]["HP_stealperc"] > 0:
                    HP = myHP
                    steal_hp = myRound((i["spellID"]["HP_stealperc"] / 100) * enHP)
                    enHP -= steal_hp
                    myHP += steal_hp
                    if myHP > max_myHP:
                        print(str(i["spellID"]['name']) + " stole " + str(steal_hp - max_myHP - HP) + " health points")
                        time.sleep(2)
                        myHP = max_myHP
                    else:
                        print(str(i["spellID"]['name']) + " stole " + str(steal_hp) + " health points")
                        time.sleep(2)
                if i["spellID"]["reflect_dmgperc"] > 0:
                    myBuff.append({"reflect_dmgperc": i["spellID"]["reflect_dmgperc"]})
                if i["spellID"]["absorbed_dmgperc"] > 0:
                    myBuff.append({"absorbed_dmgperc": i["spellID"]["absorbed_dmgperc"]})
                if i["spellID"]["Remove_debuff"] > 0:
                    myDebuff.clear()
                if i["spellID"]["SP_stealperc"] > 0:
                    steal_sp = myRound((i["spellID"]["SP_stealperc"]/100)*enSP)
                    mySP += steal_sp
                    enSP -= steal_sp
                    print(i['spellID']['name'] + " stole " + str(steal_sp) + " skill points")
                    time.sleep(2)

        if enStun == 0:
            print("\n Your Health: " + str(myHP))
            print(" Your skill points: " + str(mySP))
            print("\n Enemy's Health: " + str(enHP))
            print(" Enemy's Skill Points: " + str(enSP))
        else:
            print("Enemy is stunned")

        time.sleep(2)


        turn += 1

        for i in activeSkillsInfo:
            if i['turnsLeft'] == 1:

                del myactiveSkills[activeSkillsInfo.index(i)]
                activeSkillsInfo.remove(i)

            else:
                i['turnsLeft'] -= 1
        if enStun == 0:
            n = random.randint(1, 9)
            while (n - 1) in enactiveSkills:
                n = random.randint(1, 9)
            while 3 < n < 7 and classes[enClass1 - 1][n - 4]["SP_cost"] > enSP:
                n = random.randint(1, 9)
                while 6 < n < 10 and classes[enClass2 - 1][n - 7]["SP_cost"] > enSP:
                    n = random.randint(1, 9)
            while 6 < n < 10 and classes[enClass2 - 1][n - 7]["SP_cost"] > enSP:
                n = random.randint(1, 9)
                while 3 < n < 7 and classes[enClass1 - 1][n - 4]["SP_cost"] > enSP:
                    n = random.randint(1, 9)
            if n < 4:
                print("\nOpponent used " + spellData[spellOptions[n - 1]]['name'])
                enactiveSkillsInfo.append({"spellID": spellData[spellOptions[n - 1]],
                                           "turnsLeft": int(spellData[spellOptions[n - 1]]["duration"])})
            elif 3 < n < 7:
                cost = classes[enClass1 - 1][n - 4]["SP_cost"]
                print("\nOpponent used " + classes[class1 - 1][n - 4]['name'])
                enSP -= cost
                enactiveSkillsInfo.append({"spellID": classes[class1 - 1][n - 4],
                                           "turnsLeft": int(classes[class1 - 1][n - 4]["duration"])})
            elif 6 < n < 10:
                cost = classes[enClass2 - 1][n - 7]["SP_cost"]
                print("\nOpponent used " + classes[class2 - 1][n - 7]['name'])
                enSP -= cost
                enactiveSkillsInfo.append({"spellID": classes[class2 - 1][n - 7],
                                           "turnsLeft": int(classes[class2 - 1][n - 7]["duration"])})
            enactiveSkills.append(n - 1)

            for i in enactiveSkillsInfo:
                if i["spellID"]['dmg'] > 0:
                    for n in enDebuff:
                        if n["enemy_dmg_deal_reduc"] > 0:
                            less_dmg += n["enemy_dmg_deal_reduc"]
                    for n in myBuff:
                        try:
                            if n["self_dmg_taken_reduc"] > 0:
                                less_dmg += n["enemy_dmg_deal_reduc"]
                        except:
                            pass
                    if less_dmg > 100:
                        less_dmg == 100
                    less_dmg -= 100
                    dmg = abs(less_dmg / 100) * i["spellID"]['dmg']
                    for n in myBuff:
                        if n["reflect_dmgperc"] > 0:
                            reflected_dmg = myRound((n["reflect_dmgperc"]/100)*dmg)
                            dmg -= reflected_dmg
                            enHP -= reflected_dmg
                            print("You reflected " + str(reflected_dmg) + " damage")
                            time.sleep(2)
                    for n in myBuff:
                        if n["absorbed_dmgperc"] > 0:
                            absorbed_dmg = myRound((n["absorbed_dmgperc"]/100)*dmg)
                            dmg -= absorbed_dmg
                            print("You absorbed " + str(absorbed_dmg) + " damage")
                            time.sleep(2)
                            my_absorbed = absorbed_dmg
                    if en_absorbed > 0:
                        dmg += en_absorbed
                    myHP -= dmg
                    print(i["spellID"]['name'] + " dealt " + str(dmg) + " damage")
                    time.sleep(2)
                    less_dmg = 0
                if i["spellID"]['dmgperc'] > 0:
                    for n in enDebuff:
                        if n["enemy_dmg_deal_reduc"] > 0:
                            less_dmg += n["enemy_dmg_deal_reduc"]
                    for n in myBuff:
                        try:
                            if n["self_dmg_taken_reduc"] > 0:
                                less_dmg += n["enemy_dmg_deal_reduc"]
                        except:
                            pass
                    if less_dmg > 100:
                        less_dmg == 100
                    less_dmg -= 100
                    dmg = abs(less_dmg / 100) * myRound(i["spellID"]['dmgperc'] / 100 * enHP)
                    for n in myBuff:
                        if n["reflect_dmgperc"] > 0:
                            reflected_dmg = myRound((n["reflect_dmgperc"]/100)*dmg)
                            dmg -= reflected_dmg
                            enHP -= reflected_dmg
                            print("You reflected " + str(reflected_dmg) + " damage")
                            time.sleep(2)
                    for n in myBuff:
                        if n["absorbed_dmgperc"] > 0:
                            absorbed_dmg = myRound((n["absorbed_dmgperc"]/100)*dmg)
                            dmg -= absorbed_dmg
                            print("You absorbed " + str(absorbed_dmg) + " damage")
                            time.sleep(2)
                            my_absorbed = absorbed_dmg
                    if en_absorbed > 0:
                        dmg += en_absorbed
                    myHP -= dmg
                    print(i["spellID"]['name'] + " dealt " + str(dmg) + " damage")
                    time.sleep(2)
                    less_dmg = 0
                if i["spellID"]['heal'] > 0:
                    HP = enHP
                    enHP += i["spellID"]['heal']
                    if enHP > max_enHP:
                        print(str(i["spellID"]['name']) + " healed " + str(
                            i["spellID"]['heal'] - max_enHP - HP) + " health points")
                        time.sleep(2)
                        enHP = max_enHP
                    else:
                        print(str(i["spellID"]['name']) + " healed " + str(i["spellID"]['heal']) + " health points")
                        time.sleep(2)
                if i["spellID"]['healPerc'] > 0:
                    HP = enHP
                    heal = myRound(i["spellID"]['healPerc'] / 100 * max_enHP)
                    enHP += heal
                    if enHP > max_enHP:
                        print(str(i["spellID"]['name']) + " healed " + str(heal - max_myHP - HP) + " health points")
                        time.sleep(2)
                        enHP = max_enHP
                    else:
                        print(str(i["spellID"]['name']) + " healed " + str(heal) + " health points")
                        time.sleep(2)
                if i["spellID"]["self_dmg_taken_reduc"] > 0:
                    enBuff.append({"self_dmg_taken_reduc": i["spellID"]["self_dmg_taken_reduc"]})
                if i['spellID']["enemy_dmg_deal_reduc"] > 0:
                    myDebuff.append({"enemy_dmg_deal_reduc": i['spellID']["enemy_dmg_deal_reduc"]})
                if i["spellID"]["stunTime"] > 0:
                    myStun = i["spellID"]["stunTime"]
                if i["spellID"]["HP_stealperc"] > 0:
                    HP = enHP
                    steal_hp = myRound((i["spellID"]["HP_stealperc"] / 100) * enHP)
                    myHP -= steal_hp
                    enHP += steal_hp
                    if enHP > max_enHP:
                        print(str(i["spellID"]['name']) + " stole " + str(steal_hp - max_myHP - HP) + " health points")
                        time.sleep(2)
                        enHP = max_enHP
                    else:
                        print(str(i["spellID"]['name']) + " stole " + str(steal_hp) + " health points")
                        time.sleep(2)
                if i["spellID"]["reflect_dmgperc"] > 0:
                    enBuff.append({"reflect_dmgperc": i["spellID"]["reflect_dmgperc"]})
                if i["spellID"]["absorbed_dmgperc"] > 0:
                    enBuff.append({"absorbed_dmgperc": i["spellID"]["absorbed_dmgperc"]})
                if i["spellID"]["Remove_debuff"] > 0:
                    enDebuff.clear()
                if i["spellID"]["SP_stealperc"] > 0:
                    steal_sp = myRound((i["spellID"]["SP_stealperc"]/100)*enSP)
                    enSP += steal_sp
                    mySP -= steal_sp
                    print(i['spellID']['name'] + " stole " + str(steal_sp) + " skill points")
                    time.sleep(2)

        if myStun > 0:
            myStun -= 1
        if enStun > 0:
            enStun -= 1

    for i in enactiveSkillsInfo:
        if i['turnsLeft'] == 1:

            del enactiveSkills[enactiveSkillsInfo.index(i)]
            enactiveSkillsInfo.remove(i)

        else:
            i['turnsLeft'] -= 1

while(end):
    command = input("Input a command: ")

    if command.startswith('basicspellinfo'):

     
        for key in spellData:
                print("\n "+key['name']+": "+ key['desc'])
                

    if command.startswith("fight"):

      initBattle()

    if command.startswith("classspellinfo"):
        classes = [guard, tank, mage, medic]
        print("\n Guard Class spells:")
        for key in guard:
                print(key['name'] + ": " + key['desc'])
        print("\n Tank Class spells:")
        for key in tank:
                print(key['name'] + ": " + key['desc'])
        print("\n Mage Class spells:")
        for key in mage:
                print(key['name'] + ": " + key['desc'])
        print("\n Medic Class spells:")
        for key in medic:
                print(key['name'] + ": " + key['desc'])
        
        
    

    if command.startswith("exit"):
      end = 0
            

        

