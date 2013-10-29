from wnck import Window

from screenManager import ScreenManager
from piWindow import PIWindow
if __name__ == '__main__':
    manager = ScreenManager()
    window = PIWindow(manager.get_active_window())
    print window.set_position(0,0)
    #print manager.get_screen_size()
    #window.set_geometry(5, 15, 1900, 24, 500, 500)

