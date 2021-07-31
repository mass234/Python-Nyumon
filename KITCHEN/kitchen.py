#あなたの身長は？（単位ｃｍ）
HEIGHT = 180
print(f'あなたの身長は{HEIGHT}cmです。')
print('------')

#計算結果の表示メッセージ
kitchen_message = '最適なキッチンの高さ(そのn)は'

#キッチンの高さの目安計算（その１）
#キッチンの高さ=身長[cm]÷２+５）
kitchen1 = HEIGHT / 2+5
message = kitchen_message.replace('そのn', 'その1')
print(f'{message}{kitchen1}cmです。')
print('--------')

#キッチンの高さの目安計算（その２）
#キッチンの高さ=肘高ｃｍ-１０ｃｍ
#肘高はおおよそ「身長[cm]-60cm」と言われています。
kitchen2 = HEIGHT - 60 - 10
message = kitchen_message.replace('そのn','その2')
print(f'{message}{kitchen2}cmです。')
print('--------')

