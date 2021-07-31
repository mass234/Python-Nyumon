MY_HEIGHT = 1.8 #身長[m]
my_weight = 68 #体重[kg]
#名前を入力
my_name = input('名前を入力してください:') #入力内容を変数へ代入
message = my_name + 'さんのBMIは、'
message3 = 'メタボリックシンドロームであるか？'
#BMI=体重[kg]÷（身長[m]×身長[m])
my_bmi = my_weight / (MY_HEIGHT * MY_HEIGHT)
print(f'{message}{my_bmi}でした。')
print('---------')

#BMI値によって肥満度を分類する
if my_bmi < 18.5 :
    print('痩せてますね～')
elif my_bmi >= 18.5 and my_bmi < 25 :
    print('普通体重～')
elif my_bmi >= 25 and my_bmi < 30 :
    print('ぽっちゃり～')
elif my_bmi >= 30 and my_bmi < 35 :
    print('デブ～')
elif my_bmi >= 35 and my_bmi < 40 :
    print('豚～')
else:
    print('末期...')
    


