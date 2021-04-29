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

def initBattle():

    my_money = 1000
    en_money = 1000
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
    myturnsleft = []
    enturnsleft = []
    enbuffturnsleft = []
    endebuffturnsleft = []
    mybuffturnsleft = []
    mydebuffturnsleft = []
    myitems = []
    enitems = []
    turn = 0
    less_dmg = 0

    print("The buying phase has started\n")
    print("which armour would you like to purchase? (input 0 if you would not like any)\n")
    for i in range(0, 3):
        print(armour[i]["name"] + " (" + str(armour[i]["money_cost"]) + " coins) : " + str(i+1))
    print("You have " + str(my_money) + " coins\n")
    myarmour = int(input("armour: "))
    if myarmour in [1, 2, 3]:
        max_myHP += armour[myarmour - 1]["additional_health"]
        myHP = max_myHP
        myBuff.append({"self_dmg_taken_reduc": armour[myarmour - 1]["self_dmg_taken_reduc"]})
        mybuffturnsleft.append(0)
        my_money -= armour[myarmour - 1]["money_cost"]
    while True:
        print("Which items would you like to purchase?\n")
        for i in range(0, 3):
            print(potions[i]["name"] + " (" + str(potions[i]["money_cost"]) + " coins) : " + str(i + 1))
        print("You have " + str(my_money) + " coins\n")
        item = int(input("Item: "))
        if my_money >= potions[item]["money_cost"]:
            myitems.append()

    weapons = ["Sword", "Shield", "Staff", "Wand"]
    print("\n The buying phase has started \n choose 2 weapons separated by a space")

    for i in range(0, 4):
        print(" " + weapons[i] + ": " + str(i+1))
    while True:
        try:
            class1, class2 = input(" weapons: ").split(" ")
            classes = [guard, tank, mage, medic]
            class1 = int(class1)
            class2 = int(class2)
            if class1 < 5 and class1 > 0 and class2 < 5 and class2 > 0 and class2 != class1:
                break
        except:
            pass
        print(" incorrect format (are the weapons seperated by a space, valid numbers and are not equal?) ")


    for i in range(1, 4):
        texting = ""
        if i == 1:
            texting = "first"
        elif i == 2:
            texting = "second"
        else:
            texting = "third"
        while True:
            print("Pick your " + texting + " basic spell by typing the corresponding command:\n")
            count = 1
            for b in spellData:

                print(" " + str(b['name']) + " : " + str(count))
                count += 1
            a = int(input("\n" + texting + " skill: "))

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

        while myStun == 0:
            print("\n Pick a skill by typing the corresponding command:")
            print(" " + spellData[spellOptions[0]]['name'] + ": 1")
            print(" " + spellData[spellOptions[1]]['name'] + ": 2")
            print(" " + spellData[spellOptions[2]]['name'] + ": 3")
            print(" " + classes[class1 - 1][0]['name'] + ": 4")
            print(" " + classes[class1 - 1][1]['name'] + ": 5")
            print(" " + classes[class1 - 1][2]['name'] + ": 6")
            print(" " + classes[class2 - 1][0]['name'] + ": 7")
            print(" " + classes[class2 - 1][1]['name'] + ": 8")
            print(" " + classes[class2 - 1][2]['name'] + ": 9")
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
                    activeSkillsInfo.append({"spellID": spellData[spellOptions[n - 1]]})
                    myturnsleft.append(int(spellData[spellOptions[n - 1]]["duration"]))
                elif 3 < n < 7:
                    cost = classes[class2-1][n-4]["SP_cost"]
                    print("\nYou used " + classes[class1-1][n-4]['name'])
                    mySP -= cost
                    activeSkillsInfo.append({"spellID": classes[class1 - 1][n - 4]})
                    myturnsleft.append(int(classes[class1 - 1][n - 4]["duration"]))
                elif 6 < n < 10:
                    cost = classes[class2 - 1][n - 7]["SP_cost"]
                    print("\nYou used " + classes[class2 - 1][n - 7]['name'])
                    mySP -= cost
                    activeSkillsInfo.append({"spellID": classes[class2 - 1][n - 7]})
                    myturnsleft.append(int(classes[class2 - 1][n - 7]["duration"]))
                myactiveSkills.append(n-1)
                break
        if myStun == 0:
            for i in activeSkillsInfo:
                x = activeSkillsInfo.index(i)
                if i["spellID"]['dmg'] > 0:
                    for n in myDebuff:
                        try:
                            if n["enemy_dmg_deal_reduc"] > 0:
                                less_dmg += n["enemy_dmg_deal_reduc"]
                        except:
                            pass
                    for n in enBuff:
                        try:
                            if n["self_dmg_taken_reduc"] > 0:
                                less_dmg += n["self_dmg_deal_reduc"]
                        except:
                            pass
                    if less_dmg > 100:
                        less_dmg == 100
                    less_dmg -= 100
                    dmg = int(abs(less_dmg / 100) * i["spellID"]['dmg'])
                    for n in enBuff:
                        try:
                            if n["reflect_dmgperc"] > 0:
                                reflected_dmg = int((n["reflect_dmgperc"] / 100) * dmg)
                                dmg -= reflected_dmg
                                myHP -= reflected_dmg
                                print("Enemy reflected " + str(reflected_dmg) + " damage")
                                time.sleep(2)
                        except:
                            pass
                    for n in enBuff:
                        try:
                            if n["absorbed_dmgperc"] > 0:
                                absorbed_dmg = int((n["absorbed_dmgperc"] / 100) * dmg)
                                dmg -= absorbed_dmg
                                print("Enemy absorbed " + str(absorbed_dmg) + " damage")
                                time.sleep(2)
                                en_absorbed = absorbed_dmg
                        except:
                            pass
                    if my_absorbed > 0:
                        dmg += my_absorbed
                        my_absorbed = 0
                    enHP -= dmg
                    print(i["spellID"]['name'] + " dealt " + str(dmg) + " damage")
                    time.sleep(2)
                    less_dmg = 0
                if i["spellID"]['dmgperc'] > 0:
                    for n in myDebuff:
                        try:
                            if n["enemy_dmg_deal_reduc"] > 0:
                                less_dmg += n["enemy_dmg_deal_reduc"]
                        except:
                            pass
                    for n in enBuff:
                        try:
                            if n["self_dmg_taken_reduc"] > 0:
                                less_dmg += n["self_dmg_taken_reduc"]
                        except:
                            pass
                    if less_dmg > 100:
                        less_dmg == 100
                    less_dmg -= 100
                    dmg = int(abs(less_dmg / 100) * int(i["spellID"]['dmgperc'] / 100 * enHP))
                    for n in enBuff:
                        try:
                            if n["reflect_dmgperc"] > 0:
                                reflected_dmg = int((n["reflect_dmgperc"] / 100) * dmg)
                                dmg -= reflected_dmg
                                myHP -= reflected_dmg
                                print("Enemy reflected " + str(reflected_dmg) + " damage")
                                time.sleep(2)
                        except:
                            pass
                    for n in enBuff:
                        try:
                            if n["absorbed_dmgperc"] > 0:
                                absorbed_dmg = int((n["absorbed_dmgperc"] / 100) * dmg)
                                dmg -= absorbed_dmg
                                print("Enemy absorbed " + str(absorbed_dmg) + " damage")
                                time.sleep(2)
                                en_absorbed = absorbed_dmg
                        except:
                            pass
                    if my_absorbed > 0:
                        dmg += my_absorbed
                        my_absorbed = 0
                    enHP -= dmg
                    print(i["spellID"]['name'] + " dealt " + str(dmg) + " damage")
                    time.sleep(2)
                    less_dmg = 0
                if i["spellID"]['heal'] > 0:
                    HP = myHP
                    myHP += i["spellID"]['heal']
                    if myHP > max_myHP:
                        print(str(i["spellID"]['name']) + " healed " + str(max_myHP - HP) + " health points")
                        time.sleep(2)
                        myHP = max_myHP
                    else:
                        print(str(i["spellID"]['name']) + " healed " + str(i["spellID"]['heal']) + " health points")
                        time.sleep(2)
                if i["spellID"]['healPerc'] > 0:
                    HP = myHP
                    heal = int(i["spellID"]['healPerc'] / 100 * max_myHP)
                    myHP += heal
                    if myHP > max_myHP:
                        print(str(i["spellID"]['name']) + " healed " + str(max_myHP - HP) + " health points")
                        time.sleep(2)
                        myHP = max_myHP
                    else:
                        print(str(i["spellID"]['name']) + " healed " + str(heal) + " health points")
                        time.sleep(2)
                if i["spellID"]["self_dmg_taken_reduc"] > 0 and myturnsleft[x] == i["spellID"]["duration"]:
                    myBuff.append({"self_dmg_taken_reduc": i["spellID"]["self_dmg_taken_reduc"]})
                    mybuffturnsleft.append(i["spellID"]["duration"])
                if i['spellID']["enemy_dmg_deal_reduc"] > 0 and myturnsleft[x] == i["spellID"]["duration"]:
                    enDebuff.append({"enemy_dmg_deal_reduc": i['spellID']["enemy_dmg_deal_reduc"]})
                    endebuffturnsleft.append(i["spellID"]["duration"])
                if i["spellID"]["stunTime"] > 0:
                    enStun = i["spellID"]["stunTime"]
                if i["spellID"]["HP_stealperc"] > 0:
                    HP = myHP
                    steal_hp = int((i["spellID"]["HP_stealperc"] / 100) * enHP)
                    enHP -= steal_hp
                    myHP += steal_hp
                    if myHP > max_myHP:
                        print(str(i["spellID"]['name']) + " stole " + str(steal_hp) + " health points")
                        time.sleep(2)
                        myHP = max_myHP
                    else:
                        print(str(i["spellID"]['name']) + " stole " + str(steal_hp) + " health points")
                        time.sleep(2)
                if i["spellID"]["reflect_dmgperc"] > 0 and myturnsleft[x] == i["spellID"]["duration"]:
                    myBuff.append({"reflect_dmgperc": i["spellID"]["reflect_dmgperc"]})
                    mybuffturnsleft.append(i["spellID"]["duration"])
                if i["spellID"]["absorbed_dmgperc"] > 0 and myturnsleft[x] == i["spellID"]["duration"]:
                    myBuff.append({"absorbed_dmgperc": i["spellID"]["absorbed_dmgperc"]})
                    mybuffturnsleft.append(i["spellID"]["duration"])
                if i["spellID"]["Remove_debuff"] > 0:
                    myDebuff.clear()
                if i["spellID"]["SP_stealperc"] > 0:
                    steal_sp = int((i["spellID"]["SP_stealperc"]/100)*enSP)
                    mySP += steal_sp
                    enSP -= steal_sp
                    print(i['spellID']['name'] + " stole " + str(steal_sp) + " skill points")
                    time.sleep(2)
        if myStun > 0:
            myStun -= 1

        if enStun == 0:
            print("\n Your Health: " + str(myHP))
            print(" Your skill points: " + str(mySP))
            print("\n Enemy's Health: " + str(enHP))
            print(" Enemy's Skill Points: " + str(enSP))
        else:
            print("Enemy is stunned")

        time.sleep(2)


        turn += 1
        enindex = 0
        enbuffindex = 0
        endebuffindex = 0

        for i in range(0, len(enbuffturnsleft)):
            if enbuffturnsleft[i - enbuffindex] == 1:
                del enBuff[i - enbuffindex]
                del enbuffturnsleft[i - enbuffindex]
                enbuffindex += 1
            else:
                enbuffturnsleft[i - enbuffindex] -= 1

        for i in range(0, len(endebuffturnsleft)):
            if endebuffturnsleft[i - endebuffindex] == 1:
                del enDebuff[i - endebuffindex]
                del endebuffturnsleft[i - endebuffindex]
                endebuffindex += 1
            else:
                endebuffturnsleft[i - endebuffindex] -= 1



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
                enactiveSkillsInfo.append({"spellID": spellData[spellOptions[n - 1]]})
                enturnsleft.append(int(spellData[spellOptions[n - 1]]["duration"]))
            elif 3 < n < 7:
                cost = classes[enClass1 - 1][n - 4]["SP_cost"]
                print("\nOpponent used " + classes[class1 - 1][n - 4]['name'])
                enSP -= cost
                enactiveSkillsInfo.append({"spellID": classes[class1 - 1][n - 4]})
                enturnsleft.append(int(classes[class1 - 1][n - 4]["duration"]))
            elif 6 < n < 10:
                cost = classes[enClass2 - 1][n - 7]["SP_cost"]
                print("\nOpponent used " + classes[class2 - 1][n - 7]['name'])
                enSP -= cost
                enactiveSkillsInfo.append({"spellID": classes[class2 - 1][n - 7]})
                enturnsleft.append(int(classes[class2 - 1][n - 7]["duration"]))
            enactiveSkills.append(n - 1)

            for i in enactiveSkillsInfo:
                x = enactiveSkillsInfo.index(i)
                if i["spellID"]['dmg'] > 0:
                    for n in enDebuff:
                        if n["enemy_dmg_deal_reduc"] > 0:
                            less_dmg += n["enemy_dmg_deal_reduc"]
                    for n in myBuff:
                        try:
                            if int(n["self_dmg_taken_reduc"]) > 0:
                                less_dmg += int(n["self_dmg_taken_reduc"])
                        except:
                            pass
                    if less_dmg > 100:
                        less_dmg == 100
                    less_dmg -= 100
                    dmg = int(abs(less_dmg / 100) * i["spellID"]['dmg'])
                    for n in myBuff:
                        try:
                            if n["reflect_dmgperc"] > 0:
                                reflected_dmg = int((n["reflect_dmgperc"] / 100) * dmg)
                                dmg -= reflected_dmg
                                enHP -= reflected_dmg
                                print("You reflected " + str(reflected_dmg) + " damage")
                                time.sleep(2)
                        except:
                            pass
                    for n in myBuff:
                        try:
                            if n["absorbed_dmgperc"] > 0:
                                absorbed_dmg = int((n["absorbed_dmgperc"] / 100) * dmg)
                                dmg -= absorbed_dmg
                                print("You absorbed " + str(absorbed_dmg) + " damage")
                                time.sleep(2)
                                my_absorbed = absorbed_dmg
                        except:
                            pass
                    if en_absorbed > 0:
                        dmg += en_absorbed
                        en_absorbed = 0
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
                                less_dmg += n["self_dmg_deal_reduc"]
                        except:
                            pass
                    if less_dmg > 100:
                        less_dmg == 100
                    less_dmg -= 100
                    dmg = int(abs(less_dmg / 100) * int(i["spellID"]['dmgperc'] / 100 * enHP))
                    for n in myBuff:
                        try:
                            if n["reflect_dmgperc"] > 0:
                                reflected_dmg = int((n["reflect_dmgperc"] / 100) * dmg)
                                dmg -= reflected_dmg
                                enHP -= reflected_dmg
                                print("You reflected " + str(reflected_dmg) + " damage")
                                time.sleep(2)
                        except:
                            pass
                    for n in myBuff:
                        try:
                            if n["absorbed_dmgperc"] > 0:
                                absorbed_dmg = int((n["absorbed_dmgperc"] / 100) * dmg)
                                dmg -= absorbed_dmg
                                print("You absorbed " + str(absorbed_dmg) + " damage")
                                time.sleep(2)
                                my_absorbed = absorbed_dmg
                        except:
                            pass
                    if en_absorbed > 0:
                        dmg += en_absorbed
                        en_absorbed = 0
                    myHP -= dmg
                    print(i["spellID"]['name'] + " dealt " + str(dmg) + " damage")
                    time.sleep(2)
                    less_dmg = 0
                if i["spellID"]['heal'] > 0:
                    HP = enHP
                    enHP += i["spellID"]['heal']
                    if enHP > max_enHP:
                        print(str(i["spellID"]['name']) + " healed " + str(max_enHP - HP) + " health points")
                        time.sleep(2)
                        enHP = max_enHP
                    else:
                        print(str(i["spellID"]['name']) + " healed " + str(i["spellID"]['heal']) + " health points")
                        time.sleep(2)
                if i["spellID"]['healPerc'] > 0:
                    HP = enHP
                    heal = int(i["spellID"]['healPerc'] / 100 * max_enHP)
                    enHP += heal
                    if enHP > max_enHP:
                        print(str(i["spellID"]['name']) + " healed " + str(max_myHP - HP) + " health points")
                        time.sleep(2)
                        enHP = max_enHP
                    else:
                        print(str(i["spellID"]['name']) + " healed " + str(heal) + " health points")
                        time.sleep(2)
                if i["spellID"]["self_dmg_taken_reduc"] > 0 and enturnsleft[x] == i["spellID"]["duration"]:
                    enBuff.append({"self_dmg_taken_reduc": i["spellID"]["self_dmg_taken_reduc"]})
                    enbuffturnsleft.append(i["spellID"]["duration"])
                if i['spellID']["enemy_dmg_deal_reduc"] > 0 and enturnsleft[x] == i["spellID"]["duration"]:
                    myDebuff.append({"enemy_dmg_deal_reduc": i['spellID']["enemy_dmg_deal_reduc"]})
                    mydebuffturnsleft.append(i["spellID"]["duration"])
                if i["spellID"]["stunTime"] > 0:
                    myStun = i["spellID"]["stunTime"]
                if i["spellID"]["HP_stealperc"] > 0:
                    HP = enHP
                    steal_hp = int((i["spellID"]["HP_stealperc"] / 100) * enHP)
                    myHP -= steal_hp
                    enHP += steal_hp
                    if enHP > max_enHP:
                        print(str(i["spellID"]['name']) + " stole " + str(steal_hp) + " health points")
                        time.sleep(2)
                        enHP = max_enHP
                    else:
                        print(str(i["spellID"]['name']) + " stole " + str(steal_hp) + " health points")
                        time.sleep(2)
                if i["spellID"]["reflect_dmgperc"] > 0 and enturnsleft[x] == i["spellID"]["duration"]:
                    enBuff.append({"reflect_dmgperc": i["spellID"]["reflect_dmgperc"]})
                    enbuffturnsleft.append(i["spellID"]["duration"])
                if i["spellID"]["absorbed_dmgperc"] > 0 and enturnsleft[x] == i["spellID"]["duration"]:
                    enBuff.append({"absorbed_dmgperc": i["spellID"]["absorbed_dmgperc"]})
                    enbuffturnsleft.append(i["spellID"]["duration"])
                if i["spellID"]["Remove_debuff"] > 0:
                    enDebuff.clear()
                if i["spellID"]["SP_stealperc"] > 0:
                    steal_sp = int((i["spellID"]["SP_stealperc"]/100)*enSP)
                    enSP += steal_sp
                    mySP -= steal_sp
                    print(i['spellID']['name'] + " stole " + str(steal_sp) + " skill points")
                    time.sleep(2)

        if enStun > 0:
            enStun -= 1

        myindex = 0
        mybuffindex = 0
        mydebuffindex = 0

        for i in range(0, len(enturnsleft)):
            if enturnsleft[i - enindex] == 1:

                del enactiveSkills[i - enindex]
                del enactiveSkillsInfo[i - enindex]
                del enturnsleft[i - enindex]
                enindex += 1

            else:
                enturnsleft[i - enindex] -= 1

        for i in range(0, len(myturnsleft)):
            if myturnsleft[i - myindex] == 1:

                del myactiveSkills[i - myindex]
                del activeSkillsInfo[i - myindex]
                del myturnsleft[i - myindex]
                myindex += 1

            else:
                myturnsleft[i - myindex] -= 1

        for i in range(0, len(mybuffturnsleft)):
            if mybuffturnsleft[i - mybuffindex] == 1:
                del myBuff[i - mybuffindex]
                del mybuffturnsleft[i - mybuffindex]
                mybuffindex += 1
            else:
                mybuffturnsleft[i - mybuffindex] -= 1

        for i in range(0, len(mydebuffturnsleft)):
            if mydebuffturnsleft[i - mydebuffindex] == 1:
                del myDebuff[i - mydebuffindex]
                del mydebuffturnsleft[i - mydebuffindex]
                mydebuffindex += 1
            else:
                mydebuffturnsleft[i - mydebuffindex] -= 1



while(end):
    command = input("Input a command: ")

    if command.startswith('basicspellinfo'):


        for key in spellData:
                print("\n "+key['name']+": "+ key['desc'])


    if command.startswith("fight"):

      initBattle()
    if command.startswith("help"):

      print("\n ===commands=== \n basicspellinfo: shows all basic spells and their information \n classspellinfo: shows all classes' spells and their information \n fight: initiate a fight with a AI")
    if command.startswith("classspellinfo"):
        classes = [guard, tank, mage, medic]
        print("\n ===Guard Class spells===\n weapon: sword")
        for key in guard:
                print(" "+key['name'] + ": " + key['desc'])
        print("\n ===Tank Class spells===\n weapon: shield")
        for key in tank:
                print(" "+key['name'] + ": " + key['desc'])
        print("\n ===Mage Class spells===\n weapon: staff")
        for key in mage:
                print(" "+key['name'] + ": " + key['desc'])
        print("\n ===Medic Class spells===\n weapon: wand")
        for key in medic:
                print(" "+key['name'] + ": " + key['desc'])




    if command.startswith("exit"):
      end = 0




