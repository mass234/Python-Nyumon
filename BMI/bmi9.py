#BMIチェックに必要な名前、体重、身長を１つの塊（リスト）にする
bmi_elements = ['',0.0,0.0]

#肥満度の判別をタプルにする
bmi_checks = (
    (0, 18.5, '栄養不足に注意しましょう'),
    (18.5, 25, '今の状態を維持しましょう'),
    (25, 99, '食事改善や運動を心がけましょう')
    )


#名前を入力
bmi_elements[0] = input('名前を入力してください:')
#身長、体重を入力
bmi_elements[1] = input('体重(kg)を入力してください:')
bmi_elements[2] = input('身長(m)を入力してください:')

#入力された内容を表示
print('入力された内容を確認のため表示}')
print(f'名前:{bmi_elements[0]}')
print(f'体重と身長:{bmi_elements[1:]}')
print('--------')

#入力された名前を使ってメッセージを作成
message = bmi_elements[0] + 'さんのBMIは、'

#入力された体重と身長は文字列なので計算できるよう「型」を浮動小数点に変換
my_weight = float(bmi_elements[1])
my_height = float(bmi_elements[2])

#BMI=体重[kg」÷（身長「ｍ」×身長「ｍ」）
my_bmi = my_weight / (my_height * my_height)
print(f'{message}{my_bmi}です。')

#BMI値によって肥満度を分類する
if my_bmi < bmi_checks[0][1] :
    print(bmi_checks[0][2])
elif my_bmi >= bmi_checks[1][0] and my_bmi < bmi_checks[1][1]:
    print(bmi_checks[1][2])
else:
    print(bmi_checks[2][2])
    



