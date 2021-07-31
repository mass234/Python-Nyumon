import sys
if len(sys.argv)<2:
    print('表示したい名前を指定してください。')
    sys.exit()

#BMIチェックに必要な名前、体重、身長を１つの塊（リスト）にする
kitchen_elements = [0.0,0.0]
kitchen_messages = ['身長(cm):','今のキッチンの高さ(cm):']

#2つの項目を入力
num = 0
for entry in kitchen_messages :
    kitchen_elements[num] = input(entry + 'を入力してください')
    num = num + 1

my_name = sys.argv[1]

print('-------')

try:

#それぞれの高さ情報を文字から浮動小数点に変換
human_height = float(kitchen_elements[0])
kitchen_height = float(kitchen_elements[1])

print(f'あなたの身長は{human_height}cmです。')
kitchen1 = human_height / 2+5

#計算結果の表示メッセージ
kitchen_message = my_name + 'さんの最適なキッチンの高さ（そのn)は'


#今のキッチンの高さと比較し目安と同じなら適合
#それ以外なら高い.低いと表示する
if kitchen1 == kitchen_height :
    print('最適な高さです')
elif kitchen1 > kitchen_height :
    print('目安よりも低いようです')
    print('腰痛に注意しましょう')
else:
    print('目安よりも高いようです')
    print('肩こりに注意しましょう')

kitchen2 = human_height - 60 -10

print('-------')


#今のキッチンの高さと比較し目安と同じなら適合
#それ以外なら高い.低いと表示する
if kitchen2 == kitchen_height :
    print('最適な高さです')
elif kitchen2 > kitchen_height :
    print('目安よりも低いようです')
    print('腰痛に注意しましょう')
else:
    print('目安よりも高いようです')
    print('肩こりに注意しましょう')


except ValueError as e:
    print('身長または今のキッチンの高さを見直してください。')
    print(e)
except:
    import traceback
    traceback.print_exc()


