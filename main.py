import keyboard
import pyscreenshot as ImageGrab


def image_grab():
    im = ImageGrab.grab()
    im.save("user.png")

if __name__ == '__main__':
    image_grab()