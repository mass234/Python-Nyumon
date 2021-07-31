import cv2

try:
    img = cv2.imread('girl01.jpg') #画像ファイルを指定
    
    if img is None:
        raise ValueError('ファイルが見つかりません。')
    
    cv2.putText(img, 'When do you drink a smoothie?', (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1.1, (0,0,255), 2) #画像の上に文字を入力 #色はなぜかBGRの順番になってる
    
    cv2.imshow('Photo+Text', img)
    cv2.waitKey(0)
    cv2.detroyAllWindows()
except ValueError as e:
    print(e)
except:
    import traceback
    traceback.print_exc()




