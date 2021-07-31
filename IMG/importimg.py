import sys
import cv2

try:
    img = cv2.imread('girl01.jpg') #画像ファイルを指定
    
    if img is None:
        raise ValueError('ファイルが見つかりません。')
    
    cv2.imshow('Photo', img)
    cv2.waitKey(0)
    cv2.detroyAllWindows()
    
    
    
except ValueError as e:
    print(e)
except:
    import traceback
    traceback.print_exc()




