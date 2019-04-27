import os

from Qt import QtCompat
from pyvfx.boilerplate import boilerplateUI


class myPlate(boilerplateUI.Boilerplate):
    def __init__(self, parent=None, win_title='defaultTitle', win_object='defaultObject'):
        super(myPlate, self).__init__(parent, win_title, win_object)

    def setupUi(self):
        main_window_file = os.path.join(os.path.dirname(__file__),
                                        'resources',
                                        'main_window.ui')
        self.main_widget = QtCompat.load_ui(main_window_file)
        self.setCentralWidget(self.main_widget)
        self.main_widget.pushButton.clicked.connect(self.say_hello)

    def say_hello(self):
        print('Hello world!')


if __name__ == "__main__":
    bpr = boilerplateUI.BoilerplateRunner(guiClass=myPlate,
                                          win_title='Myplate',
                                          win_object='myPlate')
    bpr.run_main()
