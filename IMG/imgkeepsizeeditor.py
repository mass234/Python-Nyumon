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

    RESIZE_WIDTH = 640 #リサイズしたい横サイズ(px)

    img_height = img.shape[0] #元画像の縦サイズ
    img_width = img.shape[1] #元画像の横サイズ

    effect = cv2.resize(img, (RESIZE_WIDTH, int(RESIZE_WIDTH / img_width * img_height)))

    cv2.imshow(file, effect)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except ValueError as e:
    print(e)
except:
    import traceback
    traceback.print_exc()
