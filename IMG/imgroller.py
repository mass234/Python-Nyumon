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

    
    img_height = img.shape[0] #画像の縦サイズ
    img_width = img.shape[1] #画像の横サイズ
    img_center = (int(img_width / 2), int(img_height / 2)) #中心点を計算
    
    img_rotate = cv2.getRotationMatrix2D(img_center, 20.0, 1.0)
    effect = cv2.warpAffine(img, img_rotate, (img_width, img_height))
    
    
    cv2.imshow(file, effect)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except ValueError as e:
    print(e)
except:
    import traceback
    traceback.print_exc()
