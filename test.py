import pyautogui
import time
from PIL import ImageGrab
import numpy as np

pyautogui.FAILSAFE = True
count = 19547

def get_center_pixel_color():
    screen_width, screen_height = pyautogui.size()
    center_x = 488
    center_y = 760

    screenshot = ImageGrab.grab(bbox=(center_x, center_y, center_x + 1, center_y + 1))
    return screenshot.getpixel((0, 0))

def pixel_changed(old_color, new_color, threshold=5):

    return any(abs(old - new) > threshold for old, new in zip(old_color, new_color))

def perform_actions():
    global count
    try:
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(0.2)
        
        pyautogui.press('right')
        time.sleep(0.2)
        
        for _ in range(5):
            pyautogui.press('backspace')
            time.sleep(0.1)
            print(count)
        pyautogui.write(str(count))
        count += 1
        time.sleep(0.2)
        

        pyautogui.press('enter')

        time.sleep(5)
        

        screen_width, screen_height = pyautogui.size()
        pyautogui.click(screen_width/2, screen_height/2)
        

        time.sleep(2)
        
    except Exception as e:
        print(f"İşlem sırasında hata: {e}")

def main():
    print("Program başlatıldı. Çıkmak için Ctrl+C'ye basın.")
    print("Başlamak için 5 saniye bekleniyor...")
    time.sleep(5)
    print(f"Başlangıç count değeri: {count}")
    
    while True:
        try:

            initial_color = get_center_pixel_color()
            no_change_duration = 0
            check_interval = 0.5  
            
            print(f"Pixel rengi takip ediliyor... Başlangıç rengi: {initial_color}")
            
            while True:
                time.sleep(check_interval)
                current_color = get_center_pixel_color()
                
                if not pixel_changed(initial_color, current_color):
                    no_change_duration += check_interval
                    if no_change_duration >= 10.0: 
                        print("\nVideo durdu, işlemler başlatılıyor...")
                        perform_actions()
                        break
                else:
                    initial_color = current_color
                    no_change_duration = 0
                    
        except Exception as e:
            print(f"Hata oluştu: {e}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram kullanıcı tarafından sonlandırıldı.")
