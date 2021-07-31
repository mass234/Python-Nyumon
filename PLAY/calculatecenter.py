import cv2

try:
    img = cv2.imread('girl01.jpg') #画像ファイルを指定
    
    if img is None:
        raise ValueError('ファイルが見つかりません。')
        
    img_height = int(img.shape[0] / 2) #画像の縦1/2
    img_width = int(img.shape[1] / 2) #画像の横1/2
    
    
    cv2.circle(img, (img_width, img_height), 200, (0, 200, 255), 3) #丸を描く
    cv2.rectangle(img, (img_width - 50, img_height - 50), (img_width + 50, img_height + 50), (0, 0, 200), 3, 4) #-は左上、+は右下！（中心から）
    
    
    cv2.imshow('Photo+Circle+Rectangle Center', img) #画像を表示させる
    cv2.waitKey(0) #スペースが入力されるまでポップアップ表示
    cv2.detroyAllWindows() #すべてのウィンドウを閉じる
    
except ValueError as e:
    print(e)
except:
    import traceback
    traceback.print_exc()




