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
    
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    retValue, img_thresh = cv2.threshold(img_gray, 100, 200, cv2.THRESH_BINARY)
    
    
    cv2.imshow(file, img_thresh)
    cv2.waitKey(0)
    cv2.detroyAllWindows()
    
    
except ValueError as e: #エラー対策
    print(e)
except:
    import traceback
    traceback.print_exc()




