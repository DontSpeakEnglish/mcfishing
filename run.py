import tkinter as tk
from tkinter import ttk, font

from PIL.ImageOps import expand


def home_page(frame):
    home_label = ttk.Label(frame, text='MC自动钓鱼工具', font=('Arial', 18), width=335, anchor='center').pack(pady=5)
    nframe = (ttk.Frame(frame, borderwidth=1, width=335, height=20, relief='solid'))
    nframe.pack(side='top', fill='x')
    null_frame = ttk.Frame(nframe, width=20).pack(side='left')
    start_button = ttk.Button(nframe, text='Start')
    start_button.pack(side='left', fill='y')
    null_frame = ttk.Frame(nframe, width=20).pack(side='left')
    end_button = ttk.Button(nframe, text='End')
    end_button.pack(side='left', fill='y')
    null_frame = ttk.Frame(nframe, width=20).pack(side='left')
    start_button = ttk.Button(nframe, text='Start')

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

    homepage = home_page(mainFrame)

    root.mainloop()