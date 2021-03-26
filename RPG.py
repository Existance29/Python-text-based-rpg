end = 1

import json

with open('spells.json') as f:
  spellData= json.load(f)

while(end):
    command = input("Input a command: ")

    if command.startswith('info'):

        a = command.split()[1].lower()
        for key in spellData:
            
            if a == key['name'].lower().replace(" ", ""):
                print(key['name']+": "+ key['desc'])
                break
            

        

