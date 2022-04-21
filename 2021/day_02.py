'''
Here we take all the commands and his respective the resulting values (depth, aim) and
in the end we show the simple depth for PART I and the depth considering the aim for PART II.
PART I ANSWER: 2117664
PART II ANSWER: 2073416724
'''

with open("day_02_input.txt") as commands:
    list_of_commands = commands.read().splitlines()

dict_of_commands = {"forward": 0, "up": 0, "down":0, "depth": 0, "aim": 0}    

for item in  list_of_commands:
    word = item.split()[0]
    value = int(item.split()[1])
    dict_of_commands[word] = dict_of_commands[word] + value
    if word == "forward":
        dict_of_commands["depth"] = dict_of_commands["depth"] + dict_of_commands["aim"]*value
    elif word == "down":
        dict_of_commands["aim"] = dict_of_commands["aim"] + value
    else:
        dict_of_commands["aim"] = dict_of_commands["aim"] - value

print(dict_of_commands)
print(f"PART I: {dict_of_commands['forward'] * (dict_of_commands['down'] - dict_of_commands['up'])}")
print(f"PART II: {dict_of_commands['depth'] * dict_of_commands['forward']}")
