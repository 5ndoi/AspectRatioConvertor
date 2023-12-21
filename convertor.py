# python make_widescreen.py file_path

# 1440x1080 - 4:3 >>> 1920x1080 - 16:9

import cv2
import numpy as np

# ファイルのパスの入力
print("ファイルのパスを入力してください")
rfname = input()

# 画像の読み込み
img = cv2.imread(rfname, cv2.IMREAD_UNCHANGED)

# 元画像の高さ，幅
h = img.shape[0] # 1080
w = img.shape[1] # 1440

# 生成画像
img_new = np.zeros((1080,1920,4))

# 生成画像の幅
new_w = img_new.shape[1] # 1920

# 増やした幅の色付け
# 左右別々
for x in range(new_w):
    for y in range(h):
        if x < 245:
            img_new[y,x,:] = img[y,1,:]
        elif x > 1675:
            img_new[y,x,:] = img[y,1438,:]


 # 画像のはめ込み
for x in range(w):
    for y in range(h):
        img_new[y,x+240,:] = img[y,x,:]

# 出力ファイル名の生成
basename = rfname[0:rfname.rfind(".")]
wfname = basename + "_wide" + ".png"

#画像データ書き込み
cv2.imwrite(wfname, img_new)
print('保存完了 >>> ', wfname)
