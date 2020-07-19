import random
import sys

print("じゃんけんしようぜ！(グー＝0,チョキ＝1,パー＝2)")

a=input()

#例外処理
if(a!="0" and a!="1" and a!="2"):
    print("0か1か2を入れるんだよ!")
    sys.exit()

#手の調整
a= int(a)
b=random.randint(0,2)

#勝敗
if a==b:
    print("あいこ")
elif (a==0 and b==1)or(a==1 and b==2)or(a==2 and b==0):
    print("勝ち")
else:
    print("俺の勝ち！どうして負けたか明日までに考えといてください")
    