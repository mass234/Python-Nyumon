my_weight = 70 #体重70kg
my_height = 0 #身長0m
try:
    #身長が0以下の場合、わり算できない
    if my_height <= 0 :
        raise ValueError('身長が正しくありません。')
    #BMI=体重[kg]÷(身長[m]×身長[m])
    my_bmi = my_weight / (my_height * my_height)
    print(f'あなたのBMI値は{my_bmi}です。')
except ValueError as e:
    print('体重または身長を見直してください。')
    print(e)
except:
    import traceback
    traceback.print_exc()
