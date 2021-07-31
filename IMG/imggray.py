import sys
import cv2

if len(sys.argv)<2:
    print('表示したいファイル名を指定してください。')
    sys.exit() #ファイルが指定されていないので強制終了

file = sys.argv[1]

try:
    img = cv2.imread(file)

    if img is None:
        raise ValueError('ファイルが見つかりません。')

    
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    
    cv2.imshow(file, img_gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except ValueError as e:
    print(e)
except:
    import traceback
    traceback.print_exc()
