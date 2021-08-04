import os
import sys
import subprocess

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *


class ApplauncherUI(QWidget):
    def __init__(self):
        super(ApplauncherUI, self).__init__()
        self.hlayout = QHBoxLayout()
        self.app_source_path = r"C:\Program Files"
        self.all_apps_list = os.listdir(self.app_source_path)
        self.dcc_installed_apps = dict()
        self.dcc_apps_list = (
            "Nuke",
            "Blender",
            "Natron",
            "Maya",
            "Fusion",
            "Houdini",
            "Imagineer Systems Ltd",
            "Silhouette"
        )
        self.get_dcc_apps_list()
        self.setLayout(self.hlayout)

    def get_dcc_apps_list(self):
        for inst_app_name in self.all_apps_list:
            for dcc_app in self.dcc_apps_list:
                if inst_app_name.startswith(dcc_app):
                    self.create_app_buttons(app_name=inst_app_name, icon_name=dcc_app)

        self.get_maya_versions()
        self.get_houdini_versions()

    def get_maya_versions(self):
        for inst_app_name in self.all_apps_list:
            if inst_app_name == "Autodesk":
                maya_app_list = os.listdir(os.path.join(self.app_source_path, "Autodesk"))
                for maya_version in maya_app_list:
                    if maya_version.startswith("Maya"):
                        self.create_app_buttons(app_name=maya_version, icon_name="Maya")

    def get_houdini_versions(self):
        for inst_app_name in self.all_apps_list:
            if inst_app_name == "Side Effects Software":
                houdini_app_list = os.listdir(os.path.join(self.app_source_path, "Side Effects Software"))
                for houdini_version in houdini_app_list:
                    if houdini_version.startswith("Houdini"):
                        self.create_app_buttons(app_name=houdini_version, icon_name="Houdini")

    def create_app_buttons(self, app_name, icon_name):
        if app_name == "Imagineer Systems Ltd":
            app_name = icon_name = "Mocha"
        if app_name == "Blender Foundation":
            app_name = icon_name = "Blender"
        self.app_button = QPushButton(app_name)
        self.app_button.setMinimumSize(QSize(100, 100))
        self.app_button.setIcon(QIcon("./icons/{}.png".format(icon_name)))
        self.hlayout.addWidget(self.app_button)
        self.app_button.clicked.connect(lambda: self.launch_application(app_name))
        print(app_name)

    @staticmethod
    def launch_application(app_launch_name):
        cmd = None
        if app_launch_name.startswith("Nuke"):
            nuke_exe = app_launch_name.split("v")[0]
            cmd = fr"C:\Program Files\{app_launch_name}\{nuke_exe}.exe"
        elif app_launch_name == "Natron":
            cmd = r"C:\Program Files\Natron\bin\Natron.exe"
        elif app_launch_name.startswith("Maya"):
            cmd = fr"C:\Program Files\Autodesk\{app_launch_name}\bin\maya.exe"
        elif app_launch_name.startswith("Houdini"):
            cmd = fr"C:\Program Files\Side Effects Software\{app_launch_name}\bin\houdinifx.exe"
        elif app_launch_name == "Blender":
            cmd = fr"C:\Program Files\Blender Foundation\{app_launch_name}\blender.exe"
        subprocess.Popen(cmd)


if __name__ == '__main__':
    app = QApplication()
    launcher = ApplauncherUI()
    launcher.show()
    sys.exit(app.exec_())
