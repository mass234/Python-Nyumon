#BMIチェックに必要な名前、体重、身長を１つの塊（リスト）にする
bmi_elements = ['',0.0,0.0]
bmi_messages = ['名前','体重(kg):','身長「ｍ」:']

#3つの項目を入力
num = 0
for entry in bmi_messages :
    bmi_elements[num] = input(entry + 'を入力してください')
    num = num + 1

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
    



