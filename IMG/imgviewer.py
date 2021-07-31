import sys
import cv2


if len(sys.argv)<2:
    print('表示したいファイル名を指定してください。')
    sys.exit() #ファイルが指定されていないので強制終了

file = sys.argv[1] #渡された画像ファイル名の受け取り

try:


    img = cv2.imread(file) #画像ファイルを指定
    
    
    if img is None: #画像が読み込めないときメッセージ表示
        raise ValueError('ファイルが見つかりません。')
    
    
    cv2.imshow('Photo', img)
    cv2.waitKey(0)
    cv2.detroyAllWindows()
    
    
except ValueError as e: #エラー対策
    print(e)
except:
    import traceback
    traceback.print_exc()




