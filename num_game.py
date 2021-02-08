import random as r
import time as t

def players():
  total_play = int(input('how many players are there? '))
  play = []
  i=0
  while i < total_play:
    play.append(input('enter player name: '))
    i+=1
  start = int(input('what is the max number?'))
  n = 0
  game = True
  while game: 
    if n == total_play:
      n = 0
    player_turn = play[n]
    start = r.randint(0,start)
    josh_game(start, player_turn)
    if start == 0:
      game = False
    n += 1

def josh_game(start, player_turn):
  #num1 = r.randint(0,start)
  print(player_turn, 's number:   \t' ,start, sep='')
  if(start == 0):
    print(player_turn ,'LOST and hit 0!')
    game = False
  else:
    t.sleep(3)
    
players()