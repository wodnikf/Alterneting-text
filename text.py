import pyperclip
from pynput import keyboard
import time

def transform_text(text):
    new_text = ""
    for i, char in enumerate(text):
        if i % 2 == 0:
            new_text += char.lower()
        else:
            new_text += char.upper()
    return new_text

def on_activate():
    try:
        original_clipboard = pyperclip.paste()
        
        k = keyboard.Controller()
        k.press(keyboard.Key.cmd)
        k.press('c')
        k.release('c')
        k.release(keyboard.Key.cmd)
        
        time.sleep(0.2)
        
        selected_text = pyperclip.paste()
        
        if selected_text is None:
            print("Failed to copy text from clipboard.")
            return
        

        transformed_text = transform_text(selected_text)
        

        print("Transformed text:", transformed_text)
        
        pyperclip.copy(transformed_text)
        
        test = pyperclip.paste()
        print(test)
        
        k.press(keyboard.Key.cmd)
        k.press('v')
        k.release('v')
        k.release(keyboard.Key.cmd)
        
        time.sleep(0.2)

        pyperclip.copy(original_clipboard)
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('<ctrl>+m'),
    on_activate
)

def for_canonical(f):
    return lambda k: f(listener.canonical(k))

def main():
    global listener
    listener = keyboard.Listener(
        on_press=for_canonical(hotkey.press),
        on_release=for_canonical(hotkey.release)
    )
    listener.start()
    listener.join()

if __name__ == "__main__":
    main()
