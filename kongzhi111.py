import tkinter as tk
import platform
from HeadCtrlKit import HeadCtrl
import time
# 创建主窗口
root = tk.Tk()
root.title("滑块控制")

def set_value(value):
  # 将值转换为浮点数并保留一位小数
   float_value = round(float(value), 1)
   print(f"当前值设置为: {float_value}")  # 这里可以替换为实际的控制逻辑
   value_label.config(text=f"当前值: {float_value}")

# 创建滑条
slider = tk.Scale(root, from_=0, to=1, resolution=0.01, orient='horizontal', command=set_value)
slider.set(0.5)  # 初始值为0.5
slider.pack(pady=20)

# 当前值标签
value_label = tk.Label(root, text="当前值: 0.5")
value_label.pack()

os_type = platform.system()

if os_type == "Linux":
   port_head = '/dev/ttyACM1'
elif os_type == "Darwin":
   port_head = ""
elif os_type == "Windows":
   port_head = 'COM4'
else:
   print("Unsupported OS, Please check your PC system")

ctrl = HeadCtrl(port_head)
ctrl.head_bai = set_value
# 退出处理
def on_closing():
   root.destroy()
   

root.protocol("WM_DELETE_WINDOW", on_closing)

# 运行主循环
root.mainloop()
""