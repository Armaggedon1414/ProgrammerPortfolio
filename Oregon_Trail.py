#Jadiah Jensen
import time
import datetime
import sys
import random
from time import sleep

#variables
STARTDATE = datetime.datetime(1848, 3, 1)
currentDate = STARTDATE
health = 100
oxenHealth = 100
totalMiles = 2000
milesTraveled = 0
rations = "FULL"
healthCondition = "GOOD"
weather = "COLD"
mainMenu = ["\n\t1. PLAY GAME", "\n\t2. QUIT"]
professionDetails = ["\n\t1. Banker    $1600", "\n\t2. Carpenter  $800", "\n\t3. Farmer     $400"]
professions = ["Banker", "Carpenter", "Farmer"]
wagonLeader = []
Family = []
money = 0
Oxen = 0
Food = 0
Clothes = 0
Ammunition = 0
axles = 0
tongues = 0
wheels = 0
supplies = [money, Oxen, Food, Clothes, Ammunition, axles, tongues, wheels]
speed = 2
rationMod = 2

#Logo and Title
def logoScreen():
  logo = """
  ___  _____  _  _  ____  __  __  ___  ____  _____  _  _
 / __)(  _  )( \( )( ___)(  )(  )/ __)(_  _)(  _  )( \( )
( (__  )(_)(  )  (  )__)  )(__)( \__ \ _)(_  )(_)(  )  (
 \___)(_____)(_)\_)(__)  (______)(___/(____)(_____)(_)\_)
              ___    __    __  __  ____  ___
             / __)  /__\  (  \/  )( ___)/ __)
            ( (_-. /(__)\  )    (  )__) \__ \\
             \___/(__)(__)(_/\/\_)(____)(___/
                          Presnts
 """
  print(logo)
  creators = "Created by: Jadiah"
  copyright = "\nCopyright 2020"
  print(creators)
  print(copyright)

def startScreen():
    title = """
 _____  ____  ____  ___  _____  _  _    ____  ____    __    ____  __
(  _  )(  _ \( ___)/ __)(  _  )( \( )  (_  _)(  _ \  /__\  (_  _)(  )
 )(_)(  )   / )__)( (_-. )(_)(  )  (     )(   )   / /(__)\  _)(_  )(__
(_____)(_)\_)(____)\___/(_____)(_)\_)   (__) (_)\_)(__)(__)(____)(____)
                        ... another one?

    """
    print(title)

#Main Menu function
def menu():
    print("""\n\n\t\t(_.=={ MAIN MENU }==._)""")
    print("\n\tWhat would you like to do?")
    for i in range(0, len(mainMenu)):
        print(mainMenu[i] + "?")
    while True:
        choiceMain = input("\n")
        if choiceMain == "1":
            break
        elif choiceMain == "2":
            quit()
        else:
            print("\nPlease enter which number you'd like to do")

#Choosing your profession
def profession():
    global money
    print("""\n\n\t\t(_.=={ Character Selection }==._)""")
    print("\nWhat profession would you like to be?")
    print("\n\tNote: The more money you start with, the fewer points you earn")
    for i in range(0, len(professionDetails)):
        print(professionDetails[i])
    while True:
        chooseProf = input("\n")
        print(str.format("\n\tYou have chosen to be a {}", professions[int(chooseProf) - 1]))
        if chooseProf == "1":
            print("\nYou have $1600")
            wagonLeader.append("Banker")
            money += 1600
            break
        elif chooseProf == "2":
            print("\nYou have $800")
            wagonLeader.append("Carpenter")
            money += 800
            break
        elif chooseProf == "3":
            print("\nYou have $400")
            wagonLeader.append("Farmer")
            money += 400
            break
        else:
            print("\nThat is not a given option")
            continue

#Picking your Family
def wholeFamily():
    print("\nWhat is the name of your Wagon Leader?")
    while True:
        playerName = input("\n")
        playerName = playerName.upper()
        if len(playerName) >= 2:
            wagonLeader.append(playerName)
            break
        else:
            print("\nName must be bigger than two characters")
            continue
    print("\nHow many other family members...?")
    print("\nNote: No more than nine. Enter an number")
    while True:
        familyLength = input("\n")
        if familyLength in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
            familyLength = int(familyLength)
            if familyLength >= 1 and familyLength <= 9:
                members = ["wife", "first child", "second child", "third child", "fourth child", "fifth child", "sixth child", "seventh child", "eighth child"]
            for i in range(1, familyLength + 1):
                print(str.format("\nWhat is the name of your {}?", members[i-1]))
                famMem = input("\n")
                famMem = famMem.upper()
                while True:
                    if len(famMem) >= 2:
                        Family.append(famMem)
                        break
                    else:
                        print("\nName must be bigger than two characters")
                        break
        else:
            print("\n\tEnter an accepted number please")
            continue
        break

#Shopping function
def shopping():
    global money, Food, Oxen, Ammunition, Clothes, axles, tongues, wheels, inventory
    shopItems = ["Oxen", "Food", "Ammunition", "Clothes", "Wagon Parts", "Check Out"]
    partsCost = [0.00, 0.00, 0.00]
    bill = 0
    amntSpent = [0.00, 0.00, 0.00, 0.00, 0.00, bill]
    print("\nBefor leaving Independence, you should buy supplies")
    print(str.format("\n\tYou have {} in cash to make this trip", money))
    print("\nRemember you can buy supplies along the way at certain points, \nso you may want to save some money")
    print("\n\nPress Enter to Continue")
    input("\n")
    print("\nWhy hello ta yeh! C'mon in! I've got a lot o' good things fer yeh!\n 'Ere they are! My humble, magnificent shop...\
    \nWell, go on then! What're yeh wantin'?\n\n")
    while True:
        amntSpent[len(amntSpent)-1] = bill
        print("""\n\n\t\t(_.=={ Welcome to MacLeod's General Store }==._)""")
        for i in range(1, len(shopItems)):
            print(str.format("{}.      {:20}      ${:.2f}", i, shopItems[i-1], amntSpent[i-1]))
        print(str.format("Total Bill so far:      ${:.2f}", bill))
        print(str.format("Total funds available:  ${:.2f}", money - bill))
        print("You can check out at any time by saying 'Check Out'")
        choice = input("What Item would you like to buy? \n")
        choice = choice.upper()
        if choice == "1":
            Oxen = 0
            amntSpent[0] = 0.00
            print("""
            Unless yeh're plannin' on pullin' everythin'
            yerself, yeh'll be wantin' oxen an'
            there're two oxen in a yoke;
            I's recommenin' at least three yokes
            an' I charge $40 a yoke""")
            answer = input("\nHow many Yokes do yeh want?\n")
            cost = int(answer) * 40
            Oxen = int(answer) * 2
            bill += cost
            amntSpent[0] = cost

        elif choice == "2":
            Food = 0
            amntSpent[1] = 0.00
            print("""
            Yeh're goin' up fer a loooong trek:
            I'd be recommendin' at the very least
            1300 pounds. I charge $1.00 per
            10 pounds""")
            answer2 = input("\nHow many pounds yeh want? \n")
            cost2 = int(answer2) * 0.10
            Food = int(answer2)
            bill += cost2
            amntSpent[1] = cost2

        elif choice == "3":
            Ammunition = 0
            amntSpent[2] = 0.00
            print("""
            Yeh'll be travelin' through dangerous territory, mark my words;
            I'd suggest yeh purchase plenty o' ammo fer them thieves.
            Comes in cases o' 100 rounds, an' each costs $7.00""")
            answer3 = input("\nHow many cases do yeh want, lad? \n")
            cost3 = int(answer3) * 7
            Ammunition = int(answer3) * 100
            bill += cost3
            amntSpent[2] = cost3

        elif choice == "4":
            Clothes = 0
            amntSpent[3] = 0.00
            print("""
            Yeh'll be needin' clothin' fer yer journey;
            I'll sell ya a shirt, trousers, and shoes in a set
            fer $4.50 each. I'd recommend a few per person, if yer
            not wantin' ter be naked halfway through yer voyage""")
            answer4 = input("\nHow many sets of clothing are yeh wantin'?\n")
            cost4 = int(answer4) * 4.50
            Clothes = int(answer4)
            bill += cost4
            amntSpent[3] = cost

        elif choice == "5":
            Parts = 0
            amntSpent[4] = 0.00
            print("""
            O'course your wagon'll fall apart! It's inevitable!
            So you might be wantin' ter buy some parts fer yer trip, an' I'm
            the gen'leman who'll sell 'em ter ya for dirt cheap!""")

            print("""An if yer wantin' ter go back ter go back an' look at the other things, yeh only need to say so!...
            Let's see 'ere... we's got wheels o' course, an' also axles, an' methinks we has a few tongues lyin'
            'round 'ere somewhere. Only $12, measley dollars for an axle, yer stealin' from me at $14 a tongue, and it's a
            deal-breaker at $15
            a wheel!""")

            while True:
                print("""\n\n\t\t(_.=={ Welcome to MacLeod's Wagon Part Emporium }==._)""")
                wagonParts = ["Axles", "Tongues", "Wheels"]
                for i in range (1, len(wagonParts) + 1):
                    print(str.format("{}.      {:20}      ${:.2f}", i, wagonParts[i-1], partsCost[i-1]))
                print(str.format("Total Bill so far:      ${:.2f}", bill))
                print(str.format("Total funds available:  ${:.2f}", money-bill))
                part = input("Pardon, but what'll it be?\n")
                if part == "1":
                    axles = 0
                    partsCost[0] = 0.00
                    print("\nYeh're wantin' the axles then? Well, that's $12 an axle")
                    numAxles = input("\nAn' how many are yeh needin'?\n")
                    axleCost = int(numAxles) * 12
                    axles = int(numAxles)
                    bill += axleCost
                    partsCost[0] = axleCost

                elif part == "2":
                    tongues = 0
                    partsCost[1] = 0.00
                    print("\nTongues it is! $14 each")
                    numTongues = input("\nHow many?\n")
                    tongueCost = int(numTongues) * 14
                    tongues = int(numTongues)
                    bill += tongueCost
                    partsCost[1] = tongueCost

                elif part == "3":
                    wheels = 0
                    partsCost[2] = 0.00
                    print("\nWheels, eh? Good choice. Only $15 each")
                    numWheels = input("\nHow many, sir?\n")
                    wheelCost = int(numWheels) * 15
                    wheels = int(numWheels)
                    bill += wheelCost
                    partsCost[2] = wheelCost

                else:
                    partsTotal = partsCost[0] + partsCost[1] + partsCost[2]
                    amntSpent[4] = partsTotal
                    print("\nHuh? Did mine old ears catch that right? Yeh're wantin' to go back to the main\
                    \npart o' my shop? Let's go then!")
                    break

        elif choice in "CHECK OUT":
            print("Well, can't say I'm happy ter see yeh go, lad. Have a good trip! Maybe I'll see yeh on the way!\
            \nI'll be needin' payment please? Righ' this way")
            if bill > money:
                print("I'm sorry ter say, yeh've spent too much! Yeh're gonna have ter go through again")
                continue
            if bill <= money:
                print("Okay, if yeh're confident with yer purchases, then yeh're good ter go! Adios! *I learned that\
                \nfrom a Spanish man. Passed through not too long ago, haha!*")
                money -= bill
                return Oxen, Food, Clothes
            

#This is to determine speed of travel
def pace():
    global speed
    print("""\n\n\t\t(_.=={ TRAVEL SPEED }==._)""")
    print("\nWhile traveling, you can go three different speeds; 1 mph(slow), 2 mph(normal), and 4 mph(fast)")
    print(str.format("Your current speed is {} mph", speed))
    print("Going a faster speed, increases the distance covered per day, but uses rations more quickly, and slower depletes\
    \nyour stock more slowly")
    speedChoice = input("How fast would you like to go for now? ")
    while True:
        if speedChoice in ("1", "2", "4"):
            speedChoice = int(speedChoice)
            speed = speedChoice
            break
        else:
            print("\nEnter a speed of 1, 2, or 4")
            continue

#Checks supplies
def checkSupplies():
    global inventory
    print("""\n\n\t\t(_.=={ CHECK SUPPLIES }==._)""")
    print(str.format("""You have...
    ${}
    {} Oxen
    {} Pounds of Food
    {} Sets of Clothing
    {} Rounds of Ammunition
    {} Axles
    {} Tongues
    {} Wheels """, money, Oxen, Food, Clothes, Ammunition, axles, tongues, wheels))

#Determines you ration level
def rationFunct():
    global Food
    global rations
    global rationMod
    if (Food/(2 * len(Family))) >= (totalMiles/20):
        rations =  "FULL"
        rationMod = 2
    elif (Food/len(Family)) >= (totalMiles/20):
        rations =  "HALF"
        rationMod = 1
    else:
        rations = "LOW"
        rationMod = 0.5
    return rations

#When you stop and rest
def stopAndRest():
    global Food
    global currentDate
    global speed
    restTime = int(input("\nHow many days are you stopping to rest?\n"))
    currentDate += datetime.timedelta(restTime)
    Food -= restTime * (len(Family) * rationMod)
    oxenHealth = 100
    speed = 0

#Shows all of your information
def displayData():
    global milesTraveled
    global totalMiles
    global health
    global oxenHealth
    global rations

    milesTraveled = 2000 - totalMiles
    print("""\n\n\t\t(_.=={ DATA }==._)""")
    print(str.format("""
    Total Miles Traveled : {}
    Remaining Miles to Travel : {}
    Health : {}
    Oxen Health : {}
    Rations : {}""", milesTraveled, totalMiles, healthCondition, oxenHealth, rations))

#For trying to trade on the trail
def trading():
    global money, Food, Oxen, Ammunition, axles, tongues, wheels, inventory
    tradeItems = ["Food", "Ammunition", "Wagon Parts", "Check Out"]
    bill = 0
    amntSpent = [0.00, 0.00, 0.00, bill]
    print("\nSeein' as how yeh've done this already, why don' we get right in it?\n\n")
    while True:
        amntSpent[len(amntSpent)-1] = bill
        print("""\n\n\t\t(_.=={ Welcome to MacLeod's Trading System }==._)""")
        for i in range(1, len(tradeItems)):
            print(str.format("{}.      {:20}      ${:.2f}", i, tradeItems[i-1], amntSpent[i-1]))
        print(str.format("Total Bill so far:      ${:.2f}", bill))
        print(str.format("Total funds available:  ${:.2f}", money - bill))
        print("You can check out at any time by saying 'Check Out'")
        choice = input("What Item would you like to buy? \n")
        choice = choice.upper()

        if choice == "1":
            Food = 0
            amntSpent[0] = 0.00
            print("""
            Yeh're still up fer a loooong trek:
            I charge $1.00 per
            10 pounds""")
            answer2 = input("\nHow many pounds yeh want? \n")
            cost2 = int(answer2) * 0.10
            Food = int(answer2)
            bill += cost2
            amntSpent[0] = cost2

        elif choice == "2":
            Ammunition = 0
            amntSpent[1] = 0.00
            print("""
            Yeh're travelin' through dangerous territory, mark my words;
            I'd suggest yeh purchase plenty o' ammo fer them thieves.
            Comes in cases o' 100 rounds, an' each costs $7.00""")
            answer3 = input("\nHow many cases do yeh want, lad? \n")
            cost3 = int(answer3) * 7
            Ammunition = int(answer3) * 100
            bill += cost3
            amntSpent[1] = cost3

        elif choice == "3":
            Parts = 0
            amntSpent[2] = 0.00
            wagonParts = ["axles", "tongues", "wheels"]
            bill = 0
            partsCost = [0.00, 0.00, 0.00, bill]
            
            print("""
            Has your wagon broken yet? Might as well get more parts!""")

            print("""An if yer wantin' ter go back ter see ever'thin' else, just say so...
            Let's see 'ere... we's got wheels o' course, an' also axles, an' methinks we has a few tongues lyin'
            'round 'ere somewhere. Only $12, measley dollars for an axle, yer stealin' from me at $14 a tongue, and it's a
            deal-breaker at $15
            a wheel!""")

            while True:
                partsCost[3] = bill
                print("""\n\n\t\t(_.=={ Welcome to MacLeod's Roadside Wagon Part Emporium }==._)""")
             
                for i in range (len(wagonParts)):
                    print(str.format("{}.      {:20}      ${:.2f}", i+1, wagonParts[i], partsCost[i]))
                print(str.format("Total Bill so far:      ${:.2f}", bill))
                print(str.format("Total funds available:  ${:.2f}", money-bill))
                part = input("Pardon, but what'll it be?\n")
                if part == "1":
                    axles = 0
                    partsCost[0] = 0.00
                    print("\nYeh're wantin' the axles then? Well, that's $12 an axle")
                    numAxles = input("\nAn' how many are yeh needin'?\n")
                    axleCost = int(numAxles) * 12
                    axles = int(numAxles)
                    bill += axleCost
                    partsCost[0] += axleCost

                elif part == "2":
                    tongues = 0
                    partsCost[1] = 0.00
                    print("\nTongues it is! $14 each")
                    numTongues = input("\nHow many?\n")
                    tongueCost = int(numTongues) * 14
                    tongues = int(numTongues)
                    bill += tongueCost
                    partsCost[1] += tongueCost

                elif part == "3":
                    wheels = 0
                    partsCost[2] = 0.00
                    print("\nWheels, eh? Good choice. Only $15 each")
                    numWheels = input("\nHow many, sir?\n")
                    wheelCost = int(numWheels) * 15
                    wheels = int(numWheels)
                    bill += wheelCost
                    partsCost[2] += wheelCost

                else:
                    amntSpent[2] = partsCost[0] + partsCost[1] + partsCost[2]
                    print("\nHuh? Did mine old ears catch that right? Yeh're wantin' to go back to the main\
                    \npart o' my shop? Let's go then!")
                    break

        elif choice in "CHECK OUT":
            print("Well, can't say I'm happy ter see yeh go, lad. Have a good trip! Maybe I'll see yeh on the way!\
            \nI'll be needin' payment please? Righ' this way")
            if bill > money:
                print("I'm sorry ter say, yeh've spent too much! Yeh're gonna have ter go through again")
                continue
            if bill <= money:
                print("Okay, if yeh're confident with yer purchases, then yeh're good ter go! Adios! *I learned that\
                \nfrom a Spanish man. Passed through not too long ago, haha!*")
                money -= bill
                return Oxen, Food, Clothes, inventory

#This is your entire turn and links all other necessary functions
def turn():
    global health
    global healthCondition
    global weather
    global currentDate
    global milesTraveled
    global Food
    global rations
    global oxenHealth
    global totalMiles
    global speed
    global Oxen
    global food


    while True:
        rationFunct()
        if speed == 0:
            speed = 2
        if health >= 80:
            healthCondition = "GOOD"
        elif health < 80 and health >= 50:
            healthCondition = "FAIR"
        else:
            healthCondition = "POOR"

        chanceDeadFam = random.randint(0, 100)
        if chanceDeadFam >= 90:
            deadperson = random.randint(0, len(Family)-1)
            print(str.format("\nYou have lost {} to one of the many dangers of the trail. My condolences", Family[deadperson]))
            Family.pop(deadperson)
            health = 100
        displayData()
        problem = random.randint(1, 100)
        if problem >= 1 and problem <= 10:
            lostTime = random.randint(1, 7)
            lostPerson = random.choice(Family)
            print(str.format("\n{}, seems to have wandered off! However, you found them after {} days", lostPerson, lostTime))
            Food -= (len(Family)) * rationMod * lostTime
            currentDate += datetime.timedelta(lostTime)
        elif problem > 10 and problem <= 30:
            print(str.format("\nAgh! A snake bite!"))
            health -= 50
            speed = 1
        elif problem > 30 and problem <= 50:
            sickTime = random.randint(1, 14)
            print(str.format("\nYou have gotten sick! You've been sick for {} days", sickTime))
            currentDate += datetime.timedelta(sickTime)
        elif problem > 50 and problem <= 55:
            print("\nOne of you oxen has died. While you've lost a valued member of your team,\
            \nyou've also harvested meat!")
            Food += random.randint(200, 300)
            Oxen -= 1
            oxenHealth = 100
        else:
            print("\nYou have had an uneventful day of travel")

        turnChoices = ["Continue on Trail", "Check Supplies", "Stop And Rest", "Attempt to Trade", "Change Pace", "Give Up"]
        while True:
            print("\nWhat would you like to do?")
            for i in range(1, len(turnChoices)):
                print(str.format("{}.      {}", i, turnChoices[i-1]))
            option = input("\n")
            if option == "1":
                print("You choose to continue on the trail. Another day passes...")
                totalMiles -= speed * 10
                currentDate += datetime.timedelta(1)
                if totalMiles <= 0 and len(Family) > 1:
                    print("You have made it to OREGON! Congratulations on surviving the Trail! Barely...")
                    quit()
                elif len(Family)<=0:
                    print("What remained of your family has perished. You have lost the will to live, and your mind begins to \nfade as you trudge endlessly through the brush")
                    quit()
                elif Food<=0:
                    print("You have run out of food. You and whatever remains of your family slowly become catatonic and \ninactive because of the lack of food and hydration. You have succumbed to the Trail")
                    quit()
                else:
                    break
            elif option == "2":
                checkSupplies()
                continue
            elif option == "3":
                stopAndRest()
                break
            elif option == "4":
                trade = random.randint(1, 100)
                if trade >= 1 and trade <= 20:
                    print("Huh? Is that yeh again? It is! Hullo Hullo Hullo! Would you like to trade?")
                    print(str.format("""
                    1.      Yes
                    2.      No"""))
                    tradeChoice = input("\n")
                    if tradeChoice == "1":
                        trading()
                    elif tradeChoice == "2":
                        print("\nOh... okay... well, catcha later, friend!")
                        continue
                    else:
                        print("\nWhat was that? Mine old ears ain' what they used ter be")
                elif trade >= 21 and trade >= 91:
                    print("\nThere doesn't seem to be anybody around to trade with right now")
                    continue
                else:
                    print("You have stumbled upon Indians, they are trying to raid your wagon and kill you!")
                    while True:
                        fight = input("""Do you fire back?\n
                        1. Yes
                        2. No""")
                        if fight == "1":
                            healthlost = random.randint(1, 100)
                            health -= healthlost
                            break
                        elif fight == "2":
                            print("You decide not to fight back. They steal everything from you \nand leave you to die in the desert.\n\
                            Yay")
                            main()
                        else:
                            print("Please input a number")
                            continue




def main():
    logoScreen()
    sleep(1)
    startScreen()
    sleep(1)
    menu()
    profession()
    wholeFamily()
    shopping()
    pace()
    turn()
main()
