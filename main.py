Heroes = {
    "AAA" : "Starlord",
    "AAB" : "Drax",
    "ABA" : "Black Panther",
    "ABB" : "Doctor Strange",
    "BAA" : "Winter Soldier",
    "BAB" : "Rocket Raccoon",
    "BBA" : "Captain America",
    "BBB" : "Iron Man",
    "CAA" : "Groot",
    "CAB" : "Hulk",
    "CBA" : "Spiderman",
    "CBB" : "Mantis",
    "DAA" : "Thanos",
    "DAB" : "Thor",
    "DBA" : "Hawkeye",
    "DBB" : "Black Widow"
}

name = input("hello what is your name")
answer = input ("hi "+ name + " ready to play y or n")

if answer.upper() == "Y" :
  question1 = input("what color do you prefer? (Choose a or b) \na Blue \nb red")
if answer.upper() == "Y" :
  question2 = input ("who do you think is stronger A.thor or A.hulk \nA \nB" ) 
  if answer.upper() == "Y" :
    question3 = input ("who is your faviroit Spiderman A.tom B.andrew \nA \nB" )
    if wait.upper()  == "Y": 
      print 