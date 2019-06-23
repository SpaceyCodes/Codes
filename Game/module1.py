import random
import time
               #Variables

infin = 1
x = 0
distleft = 30
#Stats
health = random.randrange(70,95,1)
food = random.randrange(70,95,1)
water = random.randrange(70,95,1)
energy = random.randrange(70,95,1)
timing = 96



               #Inventory
#Water
clean_water_bottle = random.randrange(3,5,1)
dirty_water_bottle = 0
empty_water_bottle = 2
#Food
mre = 1
canned_beans = random.randrange(1,2,1)
cooked_meat = 0
raw_meat = 0
#Health
medkit = 1
bandages = random.randrange(1,2,1)
#Energy
energy_bar = random.randrange(1,2,1)
                                                                                                            #Need to do the travel system(done)
                                                                                                            #Need to do the time system(done)
                                                                                                            #Need to do the weather system/building system(maybe)
                                                                                                            #Need to do the hunting system(done)
                                                                                                            #Need to do the scavanging system
                                                                                                            #Need to do the timeing for all the code
                                                                                                            #Might want to add different locations at differnet distances



               #Functions
def inventory():
    print ("Your Inventory:")
    print ("Clean Water Bottle:",clean_water_bottle)
    print ("Dirty Water Bottle:",dirty_water_bottle)
    print ("Empty Water Bottle:",empty_water_bottle)
    print ("MRE:",mre)
    print ("Canned Beans:",canned_beans)
    print ("Cooked Meat:",cooked_meat)
    print ("Raw Meat:",raw_meat)
    print ("Medkit:",medkit)
    print ("Bandages:",bandages)
    print ("Energy Bars:",energy_bar)

def stats():
    print ("Your stats:")
    print ("Health:",health)
    print ("Food:",food)
    print ("Water:",water)
    print ("Energy:",energy)

def ask1():
    print ("")
    print ("(Options)    (Eat)         (Drink)    (Use) ")
    print ("(Hunt)       (Scavange)    (Cook)     (Sleep)    (Walk)")
    print ("_________________________")

def askoptions():
    print ("")
    print ("(Stats)    (Inventory)    (Distance Left)    (Time)")
    print ("_________________________")

def askeat():
    print ("")
    print ("(MRE)    (Canned Beans)    (Energy Bar)    (Cooked Meat)    (Raw Meat)")
    print ("_________________________")

def askdrink():
    print ("")
    print ("(Clean Water Bottle)    (Dirty Water Bottle)")
    print ("_________________________")

def askuse():
    print ("")
    print ("(Medkit)    (Bandage)")
    print ("_________________________")

def askhunt():
    print ("")
    print ("(Hunt For 1hr)    (Hunt For 2hr)")
    print ("_________________________")

def askcook():
    print ("")
    print ("(Cook Meat)    (Cook Water)")
    print ("________________________")

def asksleep():
    print ("")
    print ("(Sleep For 2hr)    (Sleep For 4hr)")
    print ("________________________")

def askwalk():
    print ("")
    print ("(Walk for 4km)    (Walk for 8km)")                    #2km/hr
    print ("________________________")

def askscavange():
    print ("")
    print ("(2km Radius)    (4km Radius)    (Collect Water)")                    #2km/hr
    print ("________________________")

def startgame1():
    print ("(Type <start> to start the game)    (Type <rule> to look at the rules)")

def startgame2():
    print("_________________________")
    print ("You are stuck in a forest.")
    time.sleep(1)
    print ("If you don't find a way out......you will die.")
    time.sleep(1)
    enter = str(input("Press enter to start."))
    stats()
    print ("_________________________")
    print ("Lets start the game.")

            #Game
print ("--------------------------------LOST------------------------------------")
startgame1()
while x == 0:
    starter = str(input(""))
    if starter == "rule":
        print ("Rules: To exit press enter.")
        back = str(input(""))
        startgame1()

    elif starter == "start":
        startgame2()
        infin = 0
        x += 1
    else :
        print ("Invalid.")



while infin == 0:
    if health >= 101:
        health = 100
    if water >= 101:
        water = 100
    if food >= 101:
        food = 100
    if energy >= 101:
        energy = 100
#------------------------------------------
#Timing Start
    timeday = timing // 24
    timehr = timing - (timeday*24) 
#------------------------------------------
#Endgame Start
    if health <= 0:
        print ("You died of blood lost!")
        break
    if food <= 0:
        print ("You died of hunger!")
        break
    if water <= 0:
        print ("You died of thirst!")
        break
    if energy <= 0:
        print ("You died of exhaustion!")
        break
    if timing <= 0:
        print ("You were left too long in the wild, and killed yourself.")
        break
    if distleft <= 0:
        print ("You escaped the forest and survived.")
        break
#Endgame End
#------------------------------------------
#Menu Start
    ask1()
    asking = str(input("What to do? "))
    if asking == "options":
        askoptions()
        
    elif asking == "eat":
        askeat()
        
    elif asking == "drink":
        askdrink()
        
    elif asking == "use":
        askuse()
        
    elif asking == "hunt":
        askhunt()

    elif asking == "scavange":
        askscavange()

    elif asking == "sleep":
        asksleep()

    elif asking == "cook":
        askcook()

    elif asking == "walk":
        askwalk()
        
    else :
        print ("Invalid.")
        print ("Press Enter Again.")
        print("_________________________")
    
#Menu End        
#-----------------------------------------        
#Options Start    
    ask = str(input("what to do? "))
    if ask == "stats":
        stats()
        print("_________________________")

    elif ask == "distance left":
        print ("Distance Left:",distleft,"km")
        print("_________________________")

    elif ask == "inventory":
        inventory()
        print("_________________________")

    elif ask == "time":
        print ("Time Left:")
        print ("Days:",timeday,"Hours:",timehr)
        print("_________________________")
#Option End
#-----------------------------------------
#Eat Start
    elif ask == "mre":
        if mre > 0: 
            food += 35
            mre -= 1
            print ("Food increased by 25.")
        else :
            print ("Not enough.")

    elif ask == "canned beans":
        if canned_beans > 0:
            food += 15
            canned_beans -= 1
            print ("Food increased by 15.")
        else :
            print ("Not enough.")

    elif ask == "raw meat":
        if raw_meat > 0:
            food += 10
            health -= 20
            print ("Food increased by 10.")
        else :
            print ("Not Enough.")

    elif ask == "cooked meat":
        if cooked_meat > 0:
            food += 20
            print ("Food increased by 25.")
        else :
            print ("Not enough.")

    elif ask == "energy bar":
        if energy_bar > 0:
            energy += 20
            energy_bar -= 1
            print ("Stamina increased by 20")
        else :
            print ("Not enough.")
    
#Eat End
#-----------------------------------------
#Drink Start
    elif ask == "clean water bottle":
        if clean_water_bottle > 0:
            water += 20
            clean_water_bottle -= 1
            empty_water_bottle += 1
            print ("Water increased by 15")
        else :
            print ("Not enough.")

    elif ask == "dirty water bottle":
        if dirty_water_bottle > 0:
            water += 10
            health -= 20
            dirty_water_bottle -= 1
            empty_water_bottle += 1
            print ("Water increased by 10.")
        else :
            print ("Not enough.")
#Drink End
#-----------------------------------------
#Use Start 
    elif ask == "medkit":
        if medkit > 0:
            health += 20
            medkit -= 1
            print ("Health increased by 20")
        else :
            print ("Not enough.")

    elif ask == "use bandage":
        if bandage > 0:
            health += 10
            bandage -= 1
            print ("Health increased by 10.")
        else :
            print ("Not enough.")
#Use End
#-----------------------------------------      
#Hunt Start
    elif ask == "hunt for 1hr":
        if random.randrange(1,100,1) < 5:
            health -= 20
            print ("You got hurt.")
        timing -= 1
        food -= random.randrange(8,17,1)
        water -= random.randrange(8,17,1)
        energy -= 10
        if random.randrange(1,100,1) < 85:
            raw_meat += random.randrange(1,2,1)
            print ("You got Raw Meat.")
        else :
            print ("You got nothing.")
        
    elif ask == "hunt for 2hr":
        if random.randrange(1,100,1) < 5:
            health -= 20
            print ("You got hurt.")
        timing -= 2
        food -= random.randrange(16,28,1)
        water -= random.randrange(16,28,1)
        energy -= 20
        if random.randrange(1,100,1) < 95:
            raw_meat += random.randrange(2,4,1)
            print ("You got Raw Meat.")
        else :
            print ("You got nothing.")
#Hunt End
#-----------------------------------------
#Scavange Start
    elif ask == "2km radius":
        timing -= 4
        if random.randrange(1,100,1) < 15:
            mre += random.randrange(1,2,1)
            print ("You found MRE.")
        if random.randrange(1,100,1) < 65:
            canned_beans += random.randrange(1,3,1)
            print ("You found Canned Beans.")
        if random.randrange(1,100,1) < 35:
            clean_water_bottle += random.randrange(1,3,1)
            print ("You found Clean Water Bottle.")
        if random.randrange(1,100,1) < 60:
            dirty_water_bottle += random.randrange(1,4,1)
            print ("You found Dirty Water Bottle.")
        if random.randrange(1,100,1) < 50:
            empty_water_bottle += random.randrange(1,3,1)
            print ("You found Empty Water Bottle.")
        if random.randrange(1,100,1) < 10:
            medkit += 1
            print ("You found Medkit.")
        if random.randrange(1,100,1) < 35:
            bandages += random.randrange(1,2,1)
            print ("You found Bandages.")
        if random.randrange(1,100,1) < 57:
            energy_bar += random.randrange(1,3,1)
            print ("You found Energy Bars.")
     
    elif ask == "4km radius":
        timing -= 8
        if random.randrange(1,100,1) < 15:
            mre += random.randrange(1,2,1)
            print ("You found MRE.")
        if random.randrange(1,100,1) < 65:
            canned_beans += random.randrange(1,3,1)
            print ("You found Canned Beans.")
        if random.randrange(1,100,1) < 35:
            clean_water_bottle += random.randrange(1,3,1)
            print ("You found Clean Water Bottle.")
        if random.randrange(1,100,1) < 60:
            dirty_water_bottle += random.randrange(1,4,1)
            print ("You found Dirty Water Bottle.")
        if random.randrange(1,100,1) < 50:
            empty_water_bottle += random.randrange(1,3,1)
            print ("You found Empty Water Bottle.")
        if random.randrange(1,100,1) < 10:
            medkit += 1
            print ("You found Medkit.")
        if random.randrange(1,100,1) < 35:
            bandages += random.randrange(1,2,1)
            print ("You found Bandages.")
        if random.randrange(1,100,1) < 57:
            energy_bar += random.randrange(1,3,1)
            print ("You found Energy Bars.")

    elif ask == "collect water":
        dirty_water_bottle += 1
        empty_water_bottle -= 1
        print ("You collected Dirty Water.")
#Scavange End
#-----------------------------------------
#Cooking Start
    elif ask == "cook meat":
        if raw_meat > 0:
            raw_meat -= 1
            cooked_meat =+ 1
            timing -= 1
            food -= random.randrange(3,14,1)
            water -= random.randrange(3,14,1)
            print ("You cooked 1 Meat.")
        else:
            Print("Not enough.")

    elif ask == "cook water":
        if dirty_water_bottle > 0:
            dirty_water_bottle -= 1
            clean_water_bottle += 1
            timing -= 1
            food -= random.randrange(3,14,1)
            water -= random.randrange(3,14,1)
            print ("You cleaned 1 Water Bottle.")
        else :
            print ("Not enough.")
#Cooking End
#-----------------------------------------
#Sleep Start
    elif ask == "sleep for 2hr":
        timing -= 2
        energy += random.randrange(15,25,1)
        print ("You slept.")

    elif ask == "sleep for 4hr":
        timing -= 4
        energy += random.randrange(35,52,1)
        print ("You slept.")
#Sleep End
#-----------------------------------------
#Walk Start
    elif ask == "walk for 4km":
        distleft -= 4
        timing -= 4
        water -= random.randrange(23,36,1)
        food -= random.randrange(23,36,1)
        energy -= random.randrange(23,36,1)
        print ("Distance Left:",distleft,"km")

    elif ask == "walk for 8km":
        distleft -= 8
        timing -= 4
        water -= random.randrange(46,72,1)
        food -= random.randrange(46,72,1)
        energy -= random.randrange(46,72,1)
        print ("Distance Left:",distleft,"km")
#Walk End
#-----------------------------------------
#DevComs Start
    elif ask == "kill":
        health -= 100

    elif ask == "walkall":
        distleft -= 10
#DevComs End
#-----------------------------------------
    elif ask == "":
        x=0
    else :
        print ("Invalid.")












