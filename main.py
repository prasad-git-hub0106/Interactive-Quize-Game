# importing question and answer and levels data from question.py
from question import queAns,levels

money=0

for i in range(len(queAns)):
    que= queAns[i]
    print(f"Question for Rs.{levels[i]}")
    print(f"{i+1}.{que[0]}")
    print(f"1.{que[1]}          2.{que[2]} ")
    print(f"3.{que[3]}          4.{que[4]} ")
    reply = int(input("Enter your answer(1-4): "))
    if( reply == que[5]):
        print("Correct Answer!")
        if(i==4):
            money = 500
            print(f"You have Secured Rs.{money}!")
        elif(i==9):
            money = 5000
            print(f"You have Secured Rs.{money}!")
        elif(i==14):
            money = 10000
            print(f"You have Secured Rs.{money}!")
        print("-------------------------------------------------------------")
    else:
        print("Wrong Answer!")
        print("-------------------------------------------------------------")
        break
    
print(f"You have won Rs.{money}!")