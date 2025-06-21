# # 生成images_8目录下的图片，尺寸为原图的1/8

# from PIL import Image
# import os

# src_dir = "data/nerf_llff_data/hotcrush/images"
# dst_dir = "data/nerf_llff_data/hotcrush/images_8"
# os.makedirs(dst_dir, exist_ok=True)

# for fname in sorted(os.listdir(src_dir)):
#     if fname.lower().endswith((".jpg", ".jpeg", ".png")):
#         img = Image.open(os.path.join(src_dir, fname))
#         w, h = img.size
#         img_resized = img.resize((w // 8, h // 8), Image.LANCZOS)
#         img_resized.save(os.path.join(dst_dir, fname))
#         print(f"Resized {fname} to {w // 8}x{h // 8}")


# 统一尺寸
from PIL import Image
import os
img = Image.open('./data/nerf_llff_data/hotcrush/images_8/1.jpg')  # 替换成你的路径
print(img.size)  # 输出为 (宽, 高)

input_dir = './data/nerf_llff_data/hotcrush/images_8'
target_size = (384, 512)  # 替换为上一步输出的尺寸

for fname in os.listdir(input_dir):
    if fname.endswith(('.png', '.jpg', '.jpeg')):
        path = os.path.join(input_dir, fname)
        img = Image.open(path).convert('RGB')
        img_resized = img.resize(target_size, Image.LANCZOS)
        img_resized.save(path)



# import os
# import numpy as np
# import imageio

# # 设置路径
# expname = 'donggua_1'
# log_dir = os.path.join('./logs', expname)
# npz_path = os.path.join(log_dir, 'renderonly_test_049999', 'rgbs.npy')
# video_path = os.path.join(log_dir, 'renderonly_test_049999', 'video.mp4')

# # 读取图片序列
# rgbs = np.load(npz_path)  # (N, H, W, 3)
# print(f"Loaded rgbs shape: {rgbs.shape}")

# # 转为 uint8
# def to8b(x): return (255*np.clip(x, 0, 1)).astype(np.uint8)
# frames = [to8b(im) for im in rgbs]

# # 写入视频
# imageio.mimsave(video_path, frames, fps=30)
# print(f"Saved video to {video_path}")



# import os
# folder = r"C:\Users\31521\project\cv\lab3\hotcrush"
# files = sorted([f for f in os.listdir(folder) if f.startswith("IMG_") and f.endswith(".jpg")])
# for i, filename in enumerate(files, 1):
#     os.rename(os.path.join(folder, filename), os.path.join(folder, f"{i}.jpg"))