import pyautogui
import keyboard

pyautogui.PAUSE = 0.01

def clicker():
    is_run = False
    while True:
      try:
          if keyboard.is_pressed('F1') and not is_run:
              is_run = True
          if keyboard.is_pressed('F2') and is_run:
              is_run = False
          if is_run:
              x, y = pyautogui.position()
              pyautogui.click(x, y)
      except pyautogui.FailSafeException:
          is_run = False
      except KeyboardInterrupt:
          break


if __name__ == '__main__':
    print('Press F1 to start autoclick. Press F2 to stop it. Ctrl-C to quit')
    clicker()
