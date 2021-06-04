#ROCK PAPER SCISSORS
#player1
#player2
c1=0
c2=0
n=int(input())
while(c1<n and c2<n):
  a=input()
  b=input()
  if((a=="paper" and b=="rock")or(a=="scissors" and b=="paper")or(a=="rock" and b=="scissors")):
    c1=c1+1
  elif((a=="rock" and b=="paper")or(a=="paper" and b=="scissors")or(a=="scissors" and b=="rock")):
    c2=c2+1
  else:
    c1=c1+0
    c2=c2+0
  print(c1,c2)
if(c1>c2):
  print("player1 won") 
else:
  print("player2 won")
