import pynput
from pynput import mouse, keyboard

# Koordinatları almak için fare kontrolcüsü
mouse_controller = mouse.Controller()

def on_press(key):
    try:
        if key.char == 'k':  # 'k' tuşuna basıldığında
            position = mouse_controller.position
            print(f"Fare Koordinatları: {position}")
    except AttributeError:
        pass

def main():
    print("Fareyi bir yere götürün ve 'k' tuşuna basın.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
