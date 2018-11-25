play_again = True
while play_again:

    print ("Welcome to 'The Wallmart difference adlib!'")

    #vARIABLEs FOR THE STORY
    verb1 = input("Give me a verb:")
    verb2 = input("Give me a verb ending in 'ing':")
    verb3 = input("Give me a third verb:")


    noun1 = input("Give me a plural noun:")
    noun2 = input("Give me a second plural noun:")
    noun3 = input("Give me a third plural noun:")
    noun4 = input("Give me a fourth plural noun:")
    noun5 = input("Give me a fifth plural noun:")

    number = input("Give me a number:")

    adj1 = input("Give me an adjective:")
    adj2 = input("Give me a second adjecive:")
    adj3 = input("Give me a third adjective:")
    adj4 = input("Give me a fourth adjective:")
    adj5 = input("Give me a fifth adjective:")


    #Template for the story 
    Story = ("Come " + (verb1) + " at WALMART, where you`ll receive " + (adj1) + " discounts on all of your favorite brand name " + (noun1) + ".Our " + (adj2) + " and " + (verb2) + " associates are there to " + (verb3) + " you " + (number) + " hours a day. Here you will find " + (adj3) +  " prices on the "+ (noun2) +" you need. "+ (noun3) +" for the moms, " + (noun4) + " for the kids and all the latest electronics for the family. So come on down to your "+ (adj4) +" "+ (adj5) + " WALMART where the " + (noun5) + " come first.	")   

    print(Story) 
#Loop for restarting the program

play_again_response = input("Play this program again")
if play_again_response == "y" or play_again_response == "Y":
  play_again = True
else:
  play_again = False
