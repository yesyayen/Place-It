from wnck import Window
import gtk
import time

class PIWindow:
    """Cotroller to abstract out window functions"""

    _gravity = 5
    _resizeMask = 15
    
    def __init__(self, window):
        self._window = window

    def set_position(self, xPos, yPos):
        (xCur, yCur, length, height) = self._window.get_geometry()
        self._window.set_geometry(PIWindow._gravity, PIWindow._resizeMask, xPos, yPos, length, height)

    def set_size(self, length, heigth):
        (xPos, yPos, curLength, curHeight) = self._window.get_geometry()
        self._window.set_geometry(PIWindow._gravity, PIWindow._resizeMask, xPos, yPos, length, height)

    def resize(self, xPos, yPos, length, height):
        self._window.set_geometry(PIWindow._gravity, PIWindow._resizeMask, xPos, yPos, length, height)