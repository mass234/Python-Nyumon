import sys
import cv2


if len(sys.argv)<3:
    print('検索対象画像ファイルとテンプレート画像ファイルの2つ指定してください。')
    sys.exit() #ファイルが指定されていないので強制終了

file = sys.argv[1] #渡された画像ファイル名の受け取り
file_templ = sys.argv[2]

try:


    img = cv2.imread(file) #画像ファイルを指定
    img_template = cv2.imread(file_templ)
    
    if (img is None) or (img_template is None): #画像が読み込めないときメッセージ表示
        raise ValueError('ファイルが見つかりません。')
        
        
    result_match = cv2.matchTemplate(img, img_template, cv2.TM_CCOEFF_NORMED)

    cv2.imshow('Template Matching', result_match)
    cv2.waitKey(0)
    
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result_match)
    top_left = max_loc
    bottom_right = (top_left[0] + img_template.shape[1], top_left[1] + img_template.shape[0])
    cv2.rectangle(img, top_left, bottom_right, (0, 0, 255), 2)
    
    
    cv2.imshow('Photo', img)
    cv2.waitKey(0)
    cv2.detroyAllWindows()
    
    
except ValueError as e: #エラー対策
    print(e)
except:
    import traceback
    traceback.print_exc()




