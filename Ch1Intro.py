#!/usr/bin/env python3
#   Bryan Cutkelvin
#   2020
#   "OReily - Python for DevOps book"
#     -this code is written in Python3 as excerpt of the text for educational
#      purposes; see Preface xviic page for more permissions and applicable user
#      information

import re
from string import Template

# Print statements:
print("\nHello MrBCut!")
# positional argument
print("Playstation member", "since:\t", end=" ")
print("2000")
# separator
print("Owned PlayStation's:\t")
print("2 ", "3 ", "4 ", "5", sep=",")
# in one invocation:
print("Playstation", "member", "since:\t", sep=" ", end="     ")
print("2000")
print("Owned", "PlayStation's:", "2 ", "3 ", "4 ", "5", sep=", ", end="!")

# Variables:
ps5_console_name = "Playstation 5 "
disc_version = "Disk console"
digital_version = "Digital console"
ps5_disc_version = ps5_console_name + disc_version
ps5_digital_version = ps5_console_name + digital_version
print("\n\nThere are 2 PS5 console SKUs:")
print(ps5_disc_version)
print(ps5_digital_version)

# Basic Math:
current_firmware = "20.02-02.30.00"
print("\nAs of today, the current firmware is: " + current_firmware)

# Ranges:
print("\nPlaystation console model #s: ")
print(list(range(1, 6, 1)))  # (start, end (exclusive), iteration)

# if/elif/else:
rating = input("\nEnter a Rating for a PS5 game you want to play: ")
if rating == "E" or rating == "e":
    print("You should play Sackboy")
elif rating == "T" or rating == "t":
    print("You should play Godfall")
elif rating == "M" or rating == "m":
    print("You should play Devil May Cry: Definitive Edition")
else:
    print("Hmmm, you should try other games")

# for loops:
print("\n")
for i in range(5):
    ps5_gen = i + 1
    print(f"Go Playstation {ps5_gen}!")

# while loop:
print("\n")
num_consoles = 1
while num_consoles < 6:
    print(f"There is a Playstation {num_consoles} console")
    num_consoles += 1
print("\n")

# break statement
print("The number of games I\"m NOT enjoying on PS5?:")
ps5_games_dislike_count = 0
while True:
    print(f"Dislike count? {ps5_games_dislike_count}")
    if ps5_games_dislike_count > 2:
        break  # condition fails, so leaves IMMEDIATELY, and evaluate var values
    ps5_games_dislike_count += 1
print("\n")

# continue statement:
print("The following consoles do not have Cell Processors:")
for no_cell_cpu in range(1, 6, 1):
    if no_cell_cpu == 3:
        continue  # skip a step (3) in loop, then continues sequence
    print(f"Playstation {no_cell_cpu}")

# Exceptions
print(f"\nPlaystation accessories include:")
ps_products = ["VR", "VR Aim", "Motion Controller", "Move Sharp Shooter"]
while True:
    try:
        ps_product = ps_products.pop()
        print(ps_product)
    except IndexError as e:
        print("ERROR! Removed/popped too many products!")
        print(f"\tMessage: {e}")
        break


# Objects
class Gamer:
    # variables
    memberYearLength = 2

    # methods
    @staticmethod
    def displaymembershipactivation():
        print("User has signed up for 1 year")


# instantiate Gamer class
userPsn = Gamer()
print(f"User is signed up for: {userPsn.memberYearLength} years")
userPsn.displaymembershipactivation()

# Strings
# strip
playstation5_marketing_logo = "          Play Has No Limits™          "
print(playstation5_marketing_logo.strip())
print(playstation5_marketing_logo.rstrip())
print(playstation5_marketing_logo.lstrip())
# justify
print("\n")
playstation5_url = "www.playstation.com"
leftJustified_playstation5_url = playstation5_url.ljust(25, "*")
print(leftJustified_playstation5_url)
rightJustified_playstation5_url = playstation5_url.rjust(25, "*")
print(rightJustified_playstation5_url)
# split
playstation5_full_url = "https://www.playstation.com/en-us/ps5/"
print(playstation5_full_url.split('/'))
# join
print("\n")
playstation_lightguns = ['Move Sharp Shooter', 'PVR Aim Controller']
playstation_lightguns_list = " and ".join(playstation_lightguns)
print(f"Playstation lightguns are: {playstation_lightguns_list}")
# capitalization
print("\n")
playstation_logo = "play has No Limits"
print(playstation_logo.capitalize())
print(playstation_logo.upper())
print(playstation_logo.title())
print(playstation_logo.swapcase())
print(playstation_logo.lower())
# string content check
print("\n")
print(f"starts with 'play'?: {playstation_logo.startswith('play')}")
print(f"ends with 'Limits'?: {playstation_logo.endswith('Limits')}")
print(f"is alphanumeric?: {playstation_logo.isalnum()}")
print(f"is alpha?: {playstation_logo.isalpha()}")
print(f"is numeric?: {playstation_logo.isnumeric()}")
print(f"is title?: {playstation_logo.istitle()}")
print(f"is alpha?: {playstation_logo.islower()}")
print(f"is alpha?: {playstation_logo.isupper()}")
# format
print("\n")
print(f"logo: {playstation_logo}")
print(f"format with empty index on logo: " '{} Has No {}'.format("Playstation 5", "LIMITS!!!"))
print(f"format with numbered index on logo: " '{0} {1} No {2}'.format("Playstation 5", "is", "LIMIT!!!"))
playstation_brand_name = ""
playstation_console_name = ""
print(f'''format with insert value: {playstation_brand_name} is the brand.
{playstation_console_name} is the console.
{playstation_logo} is the logo.format(playstation_brand_name='Playstation',
                                      playstation_console_name='PS5',
                                     playstation_logo='PlayStation®5')''')
# Template method; see import for string template
psn_greeting = Template("Hello $Bryan")
print(psn_greeting.substitute(Bryan="MrBCut"))

# List
print(f"\nPlaystation console version #'s:")
console_list = list(range(6))  # 0 based index list
console_list.pop(0)  # removing first element
print(console_list)
playstation_controllers = ['DualShock', 'DualShock 2', 'DualShock 3', 'DualShock 4']
print(f"\nPlaystation controller versions: {playstation_controllers}")
playstation_controllers.append('DualSense')  # can also add like ... .insert(pos, 'value'), but less "efficient"
print(f"Adding Latest controller: {playstation_controllers}")
playstation_cameras = ['PS2 EyeToy', 'PS3 EyeMove']
supported_playstation_cameras = ['PS4 VR Motion Camera', 'PS5 HD Camera']
playstation_cameras.extend(supported_playstation_cameras)
print(f"List of PlayStation cameras: {playstation_cameras}")

# Sequences
currentGenConsole = 5
print(f"\nIs Playstation {currentGenConsole} current generation console?:")
print(currentGenConsole in [1, 2, 3, 4, 5])
# using index's on sequences are 0 based!
print(f"\nVerifying console name:")
consoleName = "PlayStation"
if consoleName[5] == 't':
    print(f"PASS: {consoleName[5]}")
if consoleName[-3] == 'i':
    print(f"PASS: {consoleName[-3]}")
if consoleName.index('y') == 3:
    print(f"PASS: {consoleName.index('y')}")
# slicing
print(consoleName[0:4])  # from front...
print(consoleName[4:])  # from rear...
# length
print(f"Console Length name: {len(consoleName)}")

# Dictionaries
# empty dictionary
empty_map = dict()
type(map)
print(map)
# dictionary functionality
ps5_games_map = {'rpg1': 'Sackboy',
                 'rpg2': 'AstroBot',
                 'action1': 'Godfall',
                 'action2': 'Devil May Cry 5'
                 }
ps4_games_map = {'rpg1': 'Cyberpunk 2077',
                 'shooter': 'Apex'
                 }
print(f"\nPS4 games: {ps4_games_map}")
print(f"PS5 games: {ps5_games_map}")
print(f"PS5 game currently playing: {ps5_games_map['action2']}")
ps4_games_map['shooter'] = "Apex Legends"
print(f"PS4 games: {ps4_games_map}")
print(f"So far best PS5 game: {ps5_games_map.get('action2', 'Devil May Cry 5')}")
print(f"PS3 game currently playing: {ps5_games_map.get('action3', 'Fallout 3')}")
del ps5_games_map['rpg2']
print(f"PS5 genres: {ps5_games_map.keys()}")
print(f"PS5 titles: {ps5_games_map.values()}")
# iterate through list for keys and values
print(f"\nthe PS5 games and genres are: ")
for key, value in ps5_games_map.items():
    print(f"{key}:{value}")


# Functions
# positional arguments
def ps5DiscOrDigitalPreference(first, second):
    # no curly braces!
    print(f"first: {first}")
    print(f"second: {second}")


# NOTE! always 2 blank lines after a function definition
print(f"PS5 console preference: ")
ps5DiscOrDigitalPreference("disc", "digital")


# keyword arguments
def psSupportedConsoles(ps4=4, ps5=5):
    # default values assigned
    print(f"last gen console: {ps4}")
    print(f"current gen console: {ps5}")


print(f"\nPlayStation consoles on market are: ")
psSupportedConsoles(4, 5)
psSupportedConsoles(5)  # will pass argument of same value "twice"
psSupportedConsoles(ps5=3, ps4=2)  # you can change the argument order (and/or values)


# value returning functions
def displayPlaystationConsoleVersion():
    # returns 5
    return 5


print("\n")
print(f"The current Playstation Console version # is: ")
print(displayPlaystationConsoleVersion())


# passing functions to a list, then loop to call all functions
# 1st function:
def ps5NumberOfGames(gamesCount):
    return gamesCount + 1


# 2nd function
def ps4NumberOfGames(gamesCount):
    return gamesCount


# pass in functions to list, then loop
functions = [ps4NumberOfGames, ps5NumberOfGames]

for insideForLoopValue in functions:
    print(insideForLoopValue(4))

# RegEX
# Searching:
qa_roles = '''qa engineer,
 qa tester
 Qa analyst,
 senior qa analyst,
 test engineer,
 software development engineer in test, 
 development operations,
 QA lead'''
print("\n")
if 'qa engineer' in qa_roles:
    print(f"PASS - \"qa engineer\" found in qa_roles list")
if re.search(r'qa tester', qa_roles):
    print(f"PASS - \"qa tester\" found in 'qa_roles' list")
# Character sets
if re.search(r'[q, a]a engineer', qa_roles):  # character set matching
    print(f"PASS - there are \"qa titles\" in the 'qa roles' list")
if re.search(r'[Qq][Aa]+', qa_roles):  # matching one or more
    print(f"PASS - there are more than one titles starting with 'QA'")
email_input = input(f"\nenter an email address: ")
if re.search(r'[A-Za-z]+@[a-z]+\.[a-z]+', email_input):  # wildcard
    print(f"PASS - is a valid email address")
# Character classes
if re.search(r'\w+', email_input):  # \w+ -> a-zA-z0-9_, \d+ -> 0-9, + -> "multi chars"
    print(f"PASS - roles appear in this list")
if re.search(r'\w+@\w+\.\w+', email_input):  # refactor using Char. Classes
    print(f"PASS - using character classes: it is a valid email address")
# Groups
if re.search(r'(\w+)@(\w+)\.(\w+)', email_input):  # refactor using Char. Classes
    email_input_group = re.search(r'(\w+)@(\w+)\.(\w+)', email_input)
    print(f"PASS - using grouping: it is a valid email address ending with TLD: {email_input_group.group(3)}")
# Find All
qa_emails = '''qa.engineer@blah.com,
 qa.tester@blah.com,
 Qa.analyst@blah.com,
 senior.qa.analyst@blah.com,
 test.engineer@blah.com,
 software.development.engineer.in.test@blah.com, 
 development.operations@blah.com,
 QA.lead@blah.com'''
find_all_qa = re.findall(r"(\w+).(\w+)@(\w+)\.(\w+)", qa_emails)
display_first_part = [x[0] for x in find_all_qa]
print(f"displaying first part of titles: {display_first_part}")
display_first_part = [x[3] for x in find_all_qa]
print(f"displaying first part of titles: {display_first_part}")

# Substitution
psn_password = input(f"\nenter your PSN password: ")
print(re.sub("\w", "*", psn_password))
