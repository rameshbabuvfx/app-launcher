import os
import sys
import subprocess

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import icons


class ApplauncherUI(QWidget):
    def __init__(self):
        super(ApplauncherUI, self).__init__()
        self.hlayout = QHBoxLayout()
        self.app_source_path = r"C:\Program Files"
        self.dcc_apps = ("Nuke", "Blender", "Natron", "Maya", "Fusion", "Houdini", "Mocha", "Silhouette")
        self.get_apps_list()

    def get_apps_list(self):
        all_apps_list = os.listdir(self.app_source_path)
        print(all_apps_list)
        for app_name in all_apps_list:
            for dcc_name in self.dcc_apps:
                if app_name.startswith(dcc_name):
                    self.create_app_buttons(app_name, dcc_name)

    def create_app_buttons(self, button_name, icon_name):
        self.app_button = QPushButton(button_name)
        self.app_button.setMinimumSize(QSize(100, 100))
        self.app_button.setIcon(QIcon("./icons/{}.png".format(icon_name)))
        self.hlayout.addWidget(self.app_button)
        self.setLayout(self.hlayout)
        self.app_button.clicked.connect(lambda: self.launch_application(button_name))

    @staticmethod
    def launch_application(app_launch_name):
        if app_launch_name == "Nuke11.1v3":
            subprocess.Popen(r"C:\Program Files\Nuke11.1v3\Nuke11.1.exe")
        elif app_launch_name == "Natron":
            subprocess.Popen(r"C:\Program Files\Natron\bin\Natron.exe")
        elif app_launch_name == "Nuke13.0v3":
            subprocess.Popen(r"C:\Program Files\Nuke11.1v3\Nuke11.1.exe")
        elif app_launch_name == "Blender Foundation":
            subprocess.Popen(r"C:\Program Files\Blender Foundation\Blender 2.93\blender.exe")


if __name__ == '__main__':
    app = QApplication()
    launcher = ApplauncherUI()
    launcher.show()
    sys.exit(app.exec_())
