"""
Unit 2
Code Your Own: Unit 2
[Your Title Here]
"""

#### ---- Introduction ---- ####
print("!!!!! WARNING !!!! WARNING" * 4)
print()
print("You are curently in a plane that is crashing down you must now decide what to do.")
print()
print("!!!!! WARNING !!!! WARNING" * 4)
print()

#### ---- Variables ---- ####
bad_ending = 0
good_ending = 0


#### ---- CHOICES ---- ####

## -- First choice -- ##
first_choice = input("Choose: \na) Save the pilot \nb) Go with everyone else to grab a parachute \nc) Stay in your seat and hope for the best \n")


    ## -- choice_1 ; answers B and C -- ##
if first_choice == "c":
    print()
    print("Because of your inaction, you've hit your head on the window, passed out, and finally died as the plane crashed")
    bad_ending += 1

elif first_choice == "b": 
    print("")
    print("On your way to the parachutes, you tripped, got trampled by the other passengers, and died")
    bad_ending += 1

    ## -- Nested choice A -- ##
elif first_choice == "a":
    print()
    print("🪂 --> 🌊 --> 🏝️")
    print("You couldn't save the pilot. However, in the cockpit you found the pilot's emergency bag, which happens to have a parachute. Using the parachute, you land in the ocean and swim to a nearby shore.")
    print("")
    question_a = input("You now need to get warm. \nChoose: \na) Take off your outer clothing (shirts, pants, ect.) and ring them out to dry. \nb) Keep your wet clothes on and look for firewood \n")
    if question_a == "b":
        print("")
        print("🏨 🌴 🍹")
        print("While you were walking and looking for firewood, you came across this beautiful resort. You were able to stay at the resort until another form of transportation took you home.")
        good_ending += 1
        
        
       ## -- Nested choice 1A -- ##     
    elif question_a == "a":
        print("")
        print("To pass the time, you look through the pilot's emergency bag and find alcohol.")
        question_1a = input("Choose: \na) Drink the alcohol \nb) Use it to try and make a fire ")
        if question_1a == "a":
            print("")
            print("🍾 --> 🥃")
            print("Due to the alcohol lowering your inhibitions, you went to sleep and died from the cold")
            bad_ending += 1
            
          ## -- Nested choice 2A -- ##  
        elif question_1a == "b":
            print("")
            print("🥶 --> 🔥 --> 😀 ") 
            print("You soon realize that the fire can be used not only for warmth, but also as a signal")
            question_2a = input("Choose: \na) Stay by the fire and hope it's enough of a signal \nb) Catch fire to a long branch and wave it around, hoping it draws more attention \n")
            if question_2a == "a":
                print("")
                print("People from a nearby resort saw your fire and rescued you")
                good_ending += 1
            elif question_2a == "b":
                print("")
                print("🔥 🌴" * 15)
                print("You were careless and as a result you set the forest on fire. In doing so, not only do you burn down the forest, but also the nearby resort")
                bad_ending += 1

#### ---- Outcomes ---- ####
print("")
if bad_ending > good_ending:
    print("💀" * 30)
    print("You achieved a bad ending! Play again to see a different outcome.")
    print("💀" * 30)

elif good_ending > bad_ending:
    print("😊✨😊" * 15)
    print("You achieved a good ending! Play again to see a different outcome.")
        





