MY_HEIGHT = 1.8 #身長[m]
my_weight = 68 #体重[kg]
#message = 'あなたのBMIは、'
#message2 = 'です。'
message3 = 'メタボリックシンドロームであるか？'
#BMI=体重[kg]÷（身長[m]×身長[m])
my_bmi = my_weight / (MY_HEIGHT * MY_HEIGHT)
print(f'体重は{my_weight}kg、身長は{MY_HEIGHT}m、')
print(f'計算したBMI値は{my_bmi}でした。')
print('---------')
print(message3)
print(my_bmi > 25)
