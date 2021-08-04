import random
score = 0 
arr = ["rock", "paper", "scissors"]
def gameThree():
  num = 0
  while num !=3:
    num = num + 1
    game()


def game():
  comp = randomPlay()
  print(comp)
  x = input("rock paper scissors shoot !!!!")
  if x == "rock":
    if comp == x:
      print("tie")
    if comp == "paper":
      print("you lost")
    if comp == "scissors":
      print("you won")
      score + 1
  if x == "paper":
    if comp == x:
      print("tie")
    if comp == "scissors":
      print("you lost")
    if comp == "rock":
      print("you won")
      score + 1
  if x == "scissors":
    if comp == x:
      print("tie")
    if comp == "rock":
      print("you lost")
    if comp == "paper":
      print("you won")
      score +1
  print(score)
 


def randomPlay():
  rand = random.randrange(0,3)
  # print(arr[rand])
  return arr[rand]


  

gameThree()

