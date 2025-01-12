import cv2
import numpy as np
import pyautogui
from time import sleep


def fish_bite_detected(shot, template):
    """
    检测鱼是否上钩
    :param shot: 当前屏幕截图
    :param template: 鱼上钩的模板图像
    :return: 如果检测到鱼上钩，返回True；否则返回False
    """
    result = cv2.matchTemplate(template, shot, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(result)
    return max_val > 0.8  # 阈值可以根据实际情况调整

def auto_fish():
    """
    自动钓鱼程序
    """
    # 读取鱼上钩的模板图像
    template = cv2.imread('./target_en.png')

    while True:
        # 截取屏幕特定区域的截图，该区域应包含鱼上钩的提示
        shot = pyautogui.screenshot(region=(940, 540, 960, 540))
        shot = cv2.cvtColor(np.array(shot), cv2.COLOR_RGB2BGR)

        # 检测鱼是否上钩
        if fish_bite_detected(shot, template):
            print('鱼上钩了！进行点击')
            pyautogui.click(button='right')
            sleep(4) # 等待一段时间再进行下一次检测
            pyautogui.click(button='right')
        else:
            print('等待鱼上钩...')

        sleep(0.5)  # 每隔一段时间检测一次

if __name__ == '__main__':
    auto_fish()
