#!/usr/bin/env python3
#   Bryan Cutkelvin
#   2020
#   "OReily - Python for DevOps book"
#     -this code is written in Python3 as excerpt of the text for educational
#      purposes; see Preface xviic page for more permissions and applicable user
#      information

from string import Template
import re

cc_list = 'Rostam Batmangli <rostam@vowk.com>'
if 'Rostam' in cc_list:
    print('true')

if re.search(r'Rostam', cc_list):
    print('true')
    open('test.txt', r)

map = dict()
type(map)
print(map)
map = {'k1': 'v1', 'k2': 'v2'}
print(map)

# see import for string template
greeting = Template("$hello Nark")

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

# Exceptions
print(f"\nPlaystation accessories include:")
ps_products = ["VR", "Vita", "PSP", "VR Aim", "Motion Controller", "Move Sharp Shooter"]
while True:
    try:
        ps_product = ps_products.pop()
        print(ps_product)
    except IndexError as e:
        print("ERROR! Removed/popped too many products!")
        print(f"\tMessage: {e}")
        break

# break statement
print("\nThe number of games I\"m NOT enjoying on PS5?:")
ps5_games_dislike_count = 0
while True:
    print(f"Dislike count? {ps5_games_dislike_count}")
    if ps5_games_dislike_count > 5:
        break  # condition fails, so leaves IMMEDIATELY, and evaluate var values
    ps5_games_dislike_count += 1

# continue statement:
print("\nThe following consoles do not have Cell Processors:")
for no_cell_cpu in range(1, 6, 1):
    if no_cell_cpu == 3:
        continue  # skip a step (3) in loop, then continues sequence
    print(f"Playstation {no_cell_cpu}")
print("\n")

# while loop:
num_consoles = 1
while num_consoles < 6:
    print(f"There is a Playstation {num_consoles} console")
    num_consoles += 1
print("\n")

# for loops:
for i in range(5):
    ps5_gen = i + 1
    print(f"Go Playstation {ps5_gen}!")
print("\n")

# if/elif/else:
rating = input("Enter a Rating for a PS5 game you want to play: ")
if rating == "E" or rating == "e":
    print("You should play Sackboy")
elif rating == "T" or rating == "t":
    print("You should play Godfall")
elif rating == "M" or rating == "m":
    print("You should play Devil May Cry: Definitive Edition")
else:
    print("Hmmm, you should try other games")

# Ranges:
print("\nPlaystation console model #s: ")
print(list(range(1, 6, 1)))  # (start, end (inclusive), iteration)

# Basic Math:
current_firmware = "20.02-02.30.00"
print("\nAs of today, the current firmware is: " + current_firmware)

# Variables:
ps5_console_name = "Playstation 5 "
disc_version = "Disk console"
digital_version = "Digital console"
ps5_disc_version = ps5_console_name + disc_version
ps5_digital_version = ps5_console_name + digital_version
print("\nThere are 2 PS5 console SKUs:")
print(ps5_disc_version)
print(ps5_digital_version)

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