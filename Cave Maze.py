def direc(room): #changes rooms
  a=input("Where do you want to go? Enter a direction.\n")
  a = a.lower()
  if (a=='east' or a=='e'):
    if (room==1 or room==2 or room==4 or room==5 or room==7 or room==10 or room==11): 
      print ("Going east.")
      room+=1
      return(room)
    else:
      print("You can't go there.")
      room=direc(room)
      return(room)
  elif (a=='west' or a=='w'):
    if (room==2 or room==3 or room==5 or room==6 or room==8 or room==11 or room==12): 
      print ("Going west.")
      room-=1
      return(room)
    else:
      print("You can't go there.")
      room=direc(room)
      return(room)
  elif (a=='south' or a=='s'):
    if (room==2): 
      print ("Going south.")
      room=4
      return(room)
    elif (room==3):
      print ("Going south.")
      room=6
      return(room)      
    elif (room==4):
      print ("Going south.")
      room=7
      return(room)
    elif (room==5):
      print ("Going south.")
      room=8
      return(room)
    elif (room==7):
      print ("Going south.")
      room=10
      return(room)
    elif (room==8):
      print ("Going south.")
      room=12
      return(room)
    else:
      print("You can't go there.")
      room=direc(room)
      return(room)
  elif (a=='north' or a=='n'):
    if (room==4): 
      print ("Going north.")
      room=2
      return(room)
    elif (room==6):
      print ("Going north.")
      room=3
      return(room)      
    elif (room==7):
      print ("Going north.")
      room=4
      return(room)
    elif (room==8):
      print ("Going north.")
      room=5
      return(room)
    elif (room==10):
      print ("Going north.")
      room=7
      return(room)
    elif (room==12):
      print ("Going north.")
      room=8
      return(room)
    else:
      print("You can't go there.")
      room=direc(room)
      return(room)
  else:
    print("What? If you don't start making sense soon...")
    room=direc(room)
    return(room)

def credits(): #it prints who made the game, frankly unnecessary
  print("This game was made by Shweta Patki, PES1UG19CS477")
      
def bossfight(): #dude the function is named bossfight
  php=30
  shp=30
  turn=0
  print("There is someone inside!")
  print("They raise a large stick with a rock stuck to the end. It starts to glow with an octarine light.")
  while(php!=0 and shp!=0):
    print("Your HP:", php, "\nShweta's HP:", shp)
    turn+=1 #I only attack on even turns, but count starts from 1
    print("What do you want to do?")
    a=input("1. Dodge\n2. Fight\n3. Run\n")
    if(turn%2==1): 
      if a=='1':
        print("You dodge, but nothing is attacking you.")
      elif a=='2':
        print("You attack, punching the person's face.")
        shp=shp-10
      elif a=='3':
        print("The door is barred! You cannot run.")
      else:
        print("You stand there, paralysed with fear.")
    elif(turn%2==0):
      if a=='1':
        print("You dodge! A fireball rushes past your face, barely missing you.\nThe person lets out a scream of rage, and the stick starts glowing again.")
      elif a=='2':
        print("Before you can attack, a fireball hits you in the face! You sputter and slap it away.")
        php=php-10
      else:
        print("Before you can do anything, a fireball hits you in the face! You sputter and slap it away.")
        php=php-10
  if php==0:
    print("You're dead, bucko. Wait up-- here, I'll get you a new body...\nA door suddenly opens in front of you. A light shines out of it. You walk in. Obviously.")
    return('lost')
  elif shp==0:
    print("The person sighs and sits down. 'Okay, that's all I have in me,' they say. 'What do you want? Do you want this? Just take it.'\n ITEM RECIEVED: KEY")
    return('won')


def tkinv(inv): #takes inventory
  if len(inv)==0:
    print("Your pockets are empty right now.")
  else:
    print("Your pockets contain :",inv)

a=input("Press 0 to exist.\n") #this one makes sure i can quit if needed, to check if the whole thing is compiling, might delete later 
if (a!="0"): #joke lines
  print("That wasn't a typo. You will not exist now.")
  exit()
else:
  print("    _//         _/       _//         _//_////////         _//       _//      _/       _/////// _//_////////")
  print(" _//   _//     _/ //      _//       _// _//               _/ _//   _///     _/ //            _//  _//      ")
  print("_//           _/  _//      _//     _//  _//               _// _// _ _//    _/  _//          _//   _//      ")
  print("_//          _//   _//      _//   _//   _//////           _//  _//  _//   _//   _//       _//     _//////  ")
  print("_//         _////// _//      _// _//    _//               _//   _/  _//  _////// _//     _//      _//      ")
  print(" _//   _// _//       _//      _////     _//               _//       _// _//       _//  _//        _//      ")
  print("   _////  _//         _//      _//      _////////         _//       _//_//         _//_///////////_////////")
  print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Created in 2019 by your local cryptids ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")

print("Welcome to the world. You are a person. You have one body, two eyes, two hands, two feet, and two noses.")
print("You stand on a cliffside. To the east is a cave. To the west is a steep drop. The roads to the north and south are blocked by rockslides.")
print("Where do you want to go?")   
a=input("You can choose directions by typing north, south, east or west. If you're feeling lazy, just type the first letter.\n")
a.lower() #this entire if tree takes you into the cave whatever you do, it's meant to be like a tutorial
if (a=='e' or a=='east'):
  print("Good choice. Nice to see you have the spirit of adventure in you.")
elif (a=='west' or a=='north' or a=='south' or a=='w' or a=='n' or a=='s'):
  print("As if you have a choice. You haven't earned those yet. You're going east.")
else: 
  print("That wasn't too hard of an instruction, was it? Because you insist on being difficult, into the cave you go.")

r=1
inventory=[]
red=0
blue=0
green=0
print("As soon as you walk in, a sudden landslide completely blocks the entrance! Good thing you're inside now.")
print("Of course, now you have no choice but to go forth in search of an exit.")
while (r==1): #entry room code
  print("What do you want to do? Type a number.")
  act=input("1. Look around \n2. Go somewhere else\n3. Take inventory\n")
  if act=='1':
    print("You stand in an empty room. There is a single door to the east. The cave entrance lies to the north.")
  elif act=='2':
    r=direc(r)
  elif act=='3':
    print("Your pockets are empty right now.")
  else:
    print("I want to be here just as much as you do, buddy. Enter a number from the list.")
        
while((red==0 or blue==0 or green==0) and (r!=6 or r!=8)):  #this one loops until all the items have been given to the respective people
#there are 13 rooms in total, room 9 is for bossfight and 13 is the stairs to the next floor, 6 is above 9 and 8 is next to it
  if r==1:
    print("What do you want to do? Type a number.")
    act=input("1. Look around \n2. Go somewhere else\n3. Take inventory\n")
    if act=='1':
      print("You stand in an empty room. There is a single door to the east. The cave entrance lies to the north.")
    elif act=='2':
      r=direc(r)
    elif act=='3':
      tkinv(inventory)
    else:
      print("I want to be here just as much as you do, buddy. Enter a number from the list.")
  elif r==2:
    print("What do you want to do? Type a number.")
    act=input("1. Look around \n2. Go somewhere else\n3. Take inventory\n")
    if act=='1':
      print("You stand in an empty room. There are three doors: one each to the east, west, and south.")
    elif act=='2':
      r=direc(r)
    elif act=='3':
      tkinv(inventory)
    else:
      print("I want to be here just as much as you do, buddy. Enter a number from the list.")
  elif r==3:
    print("What do you want to do? Type a number.")
    act=input("1. Look around \n2. Go somewhere else\n3. Take inventory\n4. Talk\n")
    if act=='1':
      print("There is a WALKING TREE in front of you. There are two doors: one to the west and one to the south.")
    elif act=='2':
      r=direc(r)
    elif act=='3':
      tkinv(inventory)
    elif act=='4':#green flag indicates if tree has recieved leaves
      if (green==0 and ('LEAVES' not in inventory)):
        print("The TREE says: 'Can you help me find my GREEN LEAVES?'")
      elif (green==1 and ('LEAVES' not in inventory)):
        print("The TREE says: 'Thank you!'")
      elif (green==0 and ('LEAVES' in inventory)):
        print("Do you want to give the GREEN LEAVES to the TREE?")
        x= input("1. Yes\n2. No\n")
        if x=='1':
          print("You give the LEAVES to the TREE. The TREE drops an apple on your head.")
          green=1
          inventory.remove("LEAVES")
        elif x=='2':
          print("What are you even going to do with the LEAVES? Fine, keep them if you want them so much.")
        else:
          print("I want to be here just as much as you do, buddy. Enter a number from the list.")
  elif r==4: 
    print("What do you want to do? Type a number.")
    act=input("1. Look around \n2. Go somewhere else\n3. Take inventory\n4. Talk\n")
    if act=='1':
      print("There is a TRANSPARENT OCTOPUS in front of you. There are three doors, one to the north, one to the east and one to the south.")
    elif act=='2':
      r=direc(r)
    elif act=='3':
      tkinv(inventory)
    elif act=='4':#blue flag tells if octopus has recieved ink
      if (blue==0 and ('INK' not in inventory)):
        print("The OCTOPUS says: 'Can you find me some INK?'")
      elif (blue==1 and ('INK' not in inventory)):
        print("The OCTOPUS says: 'Now I can make paintings!'")
      elif (blue==0 and ('INK' in inventory)):
        print("Do you want to give the BLUE INK to the OCTOPUS?")
        x= input("1. Yes\n2. No\n")
        if x=='1':
          print("You squeeze out the INK onto the OCTOPUS. The OCTOPUS waves its tentacles at you.")
          blue=1
          inventory.remove("INK")
        elif x=='2':
          print("What are you even going to do with the INK? Fine, keep it if you want it so much.")
    else:
      print("I want to be here just as much as you do, buddy. Enter a number from the list.")
  elif r==5:
    print("What do you want to do? Type a number.\nWow, this room smells weird...")
    act=input("1. Look around \n2. Go somewhere else\n3. Take inventory\n")
    if act=='1':
      if ('CRACKER' in inventory) or red==1:
        print("You stand in an empty room. There are three doors, one to the south, one to the east, and one to the west.")
      elif (('CRACKER' not in inventory) and (red==0)):
        print("There is a CRACKER on the floor. There are three doors, one to the south, one to the east, and one to the west.")
        x=input("Do you want to take the CRACKER?\n1. Yes\n2. No\n")
        if x=='1':
          print("You pick up the CRACKER and put it in your pocket. It is slightly damp.")
          inventory.append("CRACKER")
        elif x=='2':
          print("You do not pick up the CRACKER.")
        else:
          print("If you didn't want the CRACKER, you could just have said so.")
    elif act=='2':
      r=direc(r)
    elif act=='3':
      tkinv(inventory)
    else:
      print("I want to be here just as much as you do, buddy. Enter a number from the list.")
  elif r==6:
    print("What do you want to do? Type a number.")
    act=input("1. Look around \n2. Go somewhere else\n3. Take inventory\n")
    if act=='1':
      print("You stand in an empty room. There are two doors, one to the north and one to the west.")
    elif act=='2':
      r=direc(r)
    elif act=='3':
      tkinv(inventory)
    else:
      print("I want to be here just as much as you do, buddy. Enter a number from the list.")
  elif r==7:
    print("What do you want to do? Type a number.\nWow, this room smells weird.")
    act=input("1. Look around \n2. Go somewhere else\n3. Take inventory\n")
    if act=='1':
      if ('LEAVES' in inventory) or red==1:
        print("You stand in an empty room. There are three doors, one to the south, one to the east, and one to the north.")
      elif (('LEAVES' not in inventory) and (red==0)):
        print("There are some GREEN LEAVES on the floor. There are three doors, one to the south, one to the east, and one to the south.")
        x=input("Do you want to take the LEAVES?\n1. Yes\n2. No\n")
        if x=='1':
          print("You pick up the LEAVES and put them in your pocket. They crunch.")
          inventory.append("LEAVES")
        elif x=='2':
          print("You do not pick up the LEAVES.")
        else:
          print("If you didn't want the LEAVES, you could just have said so.")
    elif act=='2':
      r=direc(r)
    elif act=='3':
      tkinv(inventory)
    else:
      print("I want to be here just as much as you do, buddy. Enter a number from the list.")
  elif r==8:
    print("What do you want to do? Type a number.")
    act=input("1. Look around \n2. Go somewhere else\n3. Take inventory\n4. Talk\n")
    if act=='1':
      print("There is a RED PARROT in this room. There are three doors, one to the west, one to the north, and one to the south.")
    elif act=='2':
      r=direc(r)
    elif act=='3':
      tkinv(inventory)
    elif act=='4':#red flag indicates if parrot has recieved cracker
      if (red==0 and ('CRACKER' not in inventory)):
        print("The PARROT says: 'Polly wants a cracker!'")
      elif (red==1 and ('CRACKER' not in inventory)):
        print("The PARROT says: 'MmmmMMMMMmmmmm.'")
      elif (red==0 and ('CRACKER' in inventory)):
        print("Do you want to give the CRACKER to the PARROT?")
        x= input("1. Yes\n2. No\n")
        if x=='1':
          print("You give the CRACKER to the PARROT. The PARROT eats the CRACKER.")
          red=1
          inventory.remove("CRACKER")
        elif x=='2':
          print("What are you even going to do with the CRACKER? Fine, keep them if you want them so much.")
    else:
      print("I want to be here just as much as you do, buddy. Enter a number from the list.")
  elif r==10:
    print("What do you want to do? Type a number.")
    act=input("1. Look around \n2. Go somewhere else\n3. Take inventory\n")
    if act=='1':
      print("You stand in an empty room. There are two doors, one to the north and one to the east.")
    elif act=='2':
      r=direc(r)
    elif act=='3':
      tkinv(inventory)
    else:
      print("I want to be here just as much as you do, buddy. Enter a number from the list.")
  elif r==11:
    print("What do you want to do? Type a number.\nWow, this room smells weird...")
    act=input("1. Look around \n2. Go somewhere else\n3. Take inventory\n")
    if act=='1':
      if ('INK' in inventory) or red==1:
        print("You stand in an empty room. There are two doors, one to the east and one to the west.")
      elif (('INK' not in inventory) and (red==0)):
        print("There is some BLUE INK on the floor. There are two doors, one to the east and one to the west.")
        x=input("Do you want to take the INK?\n1. Yes\n2. No\n")
        if x=='1':
          print("You sop up the INK with your hat. Don't wear that.")
          inventory.append("INK")
        elif x=='2':
          print("You do not get the INK.")
        else:
          print("If you didn't want the INK, you could just have said so.")
    elif act=='2':
      r=direc(r)
    elif act=='3':
      tkinv(inventory)
    else:
      print("I want to be here just as much as you do, buddy. Enter a number from the list.")
  elif r==12:
    print("What do you want to do? Type a number.")
    act=input("1. Look around \n2. Go somewhere else\n3. Take inventory\n")
    if act=='1':
      print("You stand in an empty room. There are two doors, one to the north and one to the west.")
    elif act=='2':
      r=direc(r)
    elif act=='3':
      tkinv(inventory)
    else:
      print("I want to be here just as much as you do, buddy. Enter a number from the list.")
  if (red and blue and green and (r!=6 or r!=8)):
    print("A door creaks in the distance. The ground shakes underneath your feet.")

if (red and blue and green and (r==6 or r==8)):
  print("Suddenly, all the doors in the room shut!")
  if r==6:
    print("Another door suddenly opens to the south. A light shines out from it.")
    print("If you got this far, you know you don't have a choice here. You're going in. /n ")
  elif r==8:
    print("Another door suddenly opens to the east. A light shines out from it.")
    print("If you got this far, you know you don't have a choice here. You're going in.")
  result=bossfight()
  while result == 'lose':
    result = bossfight()

print("The person waves their hand, and the wall collapses behind them. 'Go on,' they say, 'get outta here.' You obey. Have you ever had any choice?")
a=input("There is a door in the next room. It's locked.")
print("You use the key. It's not locked. The sunlight falls on you.")
print("You take a step outside and immediately fall to your death becuase you stepped off the cliffside.")
print("THE END")

a=input("Thank you for joining in on this adventure. Press c for credits.") #well i wanted to use the credits somewhere
if a=='c':
  credits()
else:
  exit()
