import cv2

try:
    img = cv2.imread('girl01.jpg') #画像ファイルを指定
    
    if img is None:
        raise ValueError('ファイルが見つかりません。')
        
    cv2.circle(img, (250,250), 200, (0, 200, 255), 3) #丸を描く
    cv2.rectangle(img, (400, 50), (500, 150), (0, 0, 200), 3, 4) #四角を描く
    
    cv2.imshow('Photo+Circle+Rectangle', img) #画像を表示させる
    cv2.waitKey(0) #スペースが入力されるまでポップアップ表示
    cv2.detroyAllWindows() #すべてのウィンドウを閉じる
    
except ValueError as e:
    print(e)
except:
    import traceback
    traceback.print_exc()




