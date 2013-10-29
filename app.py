from wnck import Window

from screenManager import ScreenManager

if __name__ == '__main__':
	manager = ScreenManager()
	window = manager.get_active_window()
	print window.get_geometry()
	print manager.get_screen_size() 
	#print window.set_geometry(5, 15, 65, 24, 500, 500)

