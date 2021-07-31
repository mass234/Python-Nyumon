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
    
    RESIZE_WIDTH = 800
    img_height = img.shape[0]
    img_width = img.shape[1]
    if img_width > RESIZE_WIDTH:
        img_resize = cv2.resize(img, (RESIZE_WIDTH, int(RESIZE_WIDTH / img_width * img_height)))
    else:
        img_resize = img
    
    img_gray = cv2.cvtColor(img_resize, cv2.COLOR_RGB2GRAY)
    
    
    #CASCADE_FILE = 'haarcascade_frontalface_alt.xml' 
    CASCADE_FILE = 'haarcascade_eye.xml'
    haar_cascade = cv2.CascadeClassifier(CASCADE_FILE)
    
    detection = haar_cascade.detectMultiScale(img_resize, scaleFactor=1.1, minNeighbors=2, minSize=(30, 30))
    
    if len(detection) > 0: #lenという関数で検出結果が何件あったのかを調べている。０以上ならば顔が見つかったので、赤枠を描く。
        for rect in detection:
            cv2.rectangle(img_resize, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), (0, 0, 255), thickness=2)
            
    else: #顔が見つからないとき、no match foundと表示する。
        cv2.putText(img_resize, 'no match found', (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 0, 255), 2)
    
    
    
    cv2.imshow(file, img_resize)
    cv2.waitKey(0)
    cv2.detroyAllWindows()
    
    
except ValueError as e: #エラー対策
    print(e)
except:
    import traceback
    traceback.print_exc()




