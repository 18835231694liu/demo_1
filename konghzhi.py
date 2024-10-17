import tkinter as tk
import platform
from HeadCtrlKit import HeadCtrl
class ServoControlApp:
    def __init__(self, master):
        self.master = master
        self.master.title("舵机控制")

        # 创建一个标签显示当前角度
    def set_value(value):
  # 将值转换为浮点数并保留一位小数
         float_value = round(float(value), 1)
         print(f"当前值设置为: {float_value}")  # 这里可以替换为实际的控制逻辑
         value_label.config(text=f"当前值: {float_value}")

# 创建滑条
         slider = tk.Scale(root, from_=0, to=1, resolution=0.01, orient='horizontal', command= self.update_angle)
         slider.set(0.5)
    def update_angle(self, value):
        # 更新标签显示当前角度
        self.angle_label.config(text=f"当前角度: {value}°")

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
        ctrl.right_blink = float(value)  #  0.51
        ctrl.send()


        # 在这里你可以添加代码来控制舵机
        # 比如：self.control_servo(int(value))

    def control_servo(self, angle):
        # 在这里添加控制舵机的代码cc
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = ServoControlApp(root)
    root.mainloop()

