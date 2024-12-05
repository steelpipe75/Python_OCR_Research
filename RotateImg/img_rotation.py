from PIL import Image
import numpy as np

# 画像読み込み
img = Image.open("./TestData/test.png")
w, h = img.size

# 回転角の指定
angle = 40
angle_rad = np.radians(angle)

# 回転後の画像サイズを計算
w_rot = int(np.round(h * abs(np.sin(angle_rad)) + w * abs(np.cos(angle_rad))))
h_rot = int(np.round(h * abs(np.cos(angle_rad)) + w * abs(np.sin(angle_rad))))

# 元画像の中心を軸に回転する
# PillowではImage.rotateで中心を基準に回転できる
# expand=Trueで回転後のサイズを自動調整
img_rot = img.rotate(angle, resample=Image.Resampling.BICUBIC, expand=True)

# 画像を保存
img_rot.save("test_rotate.png")
