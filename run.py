import tkinter as tk
from tkinter import X, ttk, font
from PIL.ImageOps import expand
import cv2
import numpy as np
import pyautogui
from time import sleep

startYN = False
home_prompt = ''

def fish_bite_detected(shot, template):
    result = cv2.matchTemplate(template, shot, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(result)
    return max_val > 0.8  # 阈值可以根据实际情况调整

def get_fish(root):
    if not startYN:
        return

    # 读取鱼上钩的模板图像
    template = cv2.imread('./target_en.png')

    # 截取屏幕特定区域的截图，该区域应包含鱼上钩的提示
    shot = pyautogui.screenshot(region=(940, 540, 960, 540))
    shot = cv2.cvtColor(np.array(shot), cv2.COLOR_RGB2BGR)

    # 检测鱼是否上钩
    if fish_bite_detected(shot, template):
        print('鱼上钩了！进行点击')
        pyautogui.click(button='right')
        sleep(4)  # 等待一段时间再进行下一次检测
        pyautogui.click(button='right')
    else:
        print('等待鱼上钩...')

    # 使用root.after来定期调用get_fish
    root.after(500, get_fish, root)  # 500毫秒（0.5秒）后再次调用get_fish

def start_fishing(root, sbutton, ebutton):
    sbutton.configure(state='disabled', text='已开始...', cursor='circle')
    ebutton.configure(state='normal', cursor='hand2')
    global startYN
    startYN = True
    get_fish(root)  # 启动get_fish

def end_fishing(sbutton, ebutton):
    global startYN
    startYN = False
    sbutton.configure(state='normal', text='开始', cursor='hand2')
    ebutton.configure(state='disabled', text='结束', cursor='circle')

def home_page(frame, root):
    home_label = ttk.Label(frame, text='MC自动钓鱼工具', font=('Arial', 18), anchor='center')
    home_label.pack(pady=5)

    # 设置按钮的宽度和高度
    button_width = 146  # 按钮的宽度（以字符数为单位）
    button_height = 80  # 按钮的高度（以行数为单位）

    button_frame = ttk.Frame(frame, height=button_height)
    button_frame.pack(side='top', fill='x', padx=21, pady=15)  # 设置button_frame与上下左右墙壁的距离为20

    start_button = ttk.Button(button_frame, text='开始', command=lambda: start_fishing(root=root, sbutton=start_button, ebutton=end_button), cursor='hand2')
    start_button.place(x=0, y=0, width=button_width, height=button_height)

    end_button = ttk.Button(button_frame, text='结束', command=lambda: end_fishing(start_button, end_button), state='disabled', cursor='circle')
    end_button.place(x=button_width + 21, y=0, width=button_width, height=button_height)

    home_prompt = '点击"开始"按钮开始自动钓鱼'
    prompt_frame = ttk.Frame(frame, height=120)
    prompt_frame.pack(side='top', fill='both', padx=21, pady=8)
    prompt_label = tk.Label(prompt_frame, text=home_prompt, font=('Arial', 11), anchor='center', fg='#999999')
    prompt_label.pack(side='left', padx=5)

if __name__ == "__main__":
    # 创建主窗口对象
    root = tk.Tk()
    # 加载主题文件
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "light")

    # 设置窗口标题
    root.title("Button Example")
    root.geometry("400x300")
    root.resizable(width=False, height=False)

    menu_bar = tk.Frame(root, width=45, bg='#f0f0f0')
    menu_bar.pack(side='left', fill='y')

    mainFrame = tk.Frame(root, bd=5).pack()

    homepage = home_page(mainFrame, root)

    root.mainloop()  # 主事循环