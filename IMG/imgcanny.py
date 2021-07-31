import sys
import cv2

#キャニー（画像からエッジを抜き出す）（ソーベルの結果から、エッジであるところをさらに判断して表示する）


if len(sys.argv)<2:
    print('表示したいファイル名を指定してください。')
    sys.exit() #ファイルが指定されていないので強制終了

file = sys.argv[1] #渡された画像ファイル名の受け取り

try:


    img = cv2.imread(file) #画像ファイルを指定
    
    
    if img is None: #画像が読み込めないときメッセージ表示
        raise ValueError('ファイルが見つかりません。')
    
    edge = cv2.Canny (img, 10.0, 200.0)
    
    
    cv2.imshow(file, edge)
    cv2.waitKey(0)
    cv2.detroyAllWindows()
    
    
except ValueError as e: #エラー対策
    print(e)
except:
    import traceback
    traceback.print_exc()




