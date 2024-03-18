import random

n = int(input('最小数を入力してください: '))
m = int(input('最大数を入力してください: '))

if(n>m):
  print('最小数は最大数以下にしてください')
else:
    ans = random.randint(n, m)
    user_ans = int(input("数値を入力してください: "))
    
    while ans != user_ans:
        if user_ans < ans:
          print('答えはもう少し大きい数です')
        else:
          print('答えはもう少し小さい数です')
        user_ans = int(input("もう1回入力してください: "))
    print("正解です!")
