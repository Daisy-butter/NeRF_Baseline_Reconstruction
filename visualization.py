import os
import pandas as pd
import matplotlib.pyplot as plt

# 设置文件路径
csv_dir = 'RESULT_FIGURE/donggua/csv'
fig_dir = 'RESULT_FIGURE/donggua/figures'

# 创建保存图像的文件夹（如果不存在）
os.makedirs(fig_dir, exist_ok=True)

# 读取 CSV 文件
train_loss = pd.read_csv(os.path.join(csv_dir, 'train_loss.csv'))
# test_loss = pd.read_csv(os.path.join(csv_dir, 'test_loss.csv'))
train_psnr = pd.read_csv(os.path.join(csv_dir, 'train_PSNR.csv'))
# test_psnr = pd.read_csv(os.path.join(csv_dir, 'test_PSNR.csv'))

# 绘制 Loss 曲线
plt.figure(figsize=(8, 5))
plt.plot(train_loss['Step'], train_loss['Value'], label='Train Loss')
# plt.plot(test_loss['Step'], test_loss['Value'], label='Test Loss')
plt.xlabel('Iteration')
plt.ylabel('Loss')
plt.title('NeRF Training & Testing Loss (donggua)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, 'loss_curve.png'), dpi=300)
plt.close()

# 绘制 PSNR 曲线
plt.figure(figsize=(8, 5))
plt.plot(train_psnr['Step'], train_psnr['Value'], label='Train PSNR')
# plt.plot(test_psnr['Step'], test_psnr['Value'], label='Test PSNR')
plt.xlabel('Iteration')
plt.ylabel('PSNR')
plt.title('NeRF Training & Testing PSNR (donggua)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, 'psnr_curve.png'), dpi=300)
plt.close()

print("✅ Figures saved to:", fig_dir)
