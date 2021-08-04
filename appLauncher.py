import os
import sys
import subprocess

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *


class ApplauncherUI(QWidget):
    def __init__(self):
        super(ApplauncherUI, self).__init__()
        self.setWindowTitle("Smart Launch")
        # self.setStyleSheet("background-color: rgb(62, 61, 64)")
        self.vlayout = QVBoxLayout()
        self.app_source_path = r"C:\Program Files"
        self.all_apps_list = os.listdir(self.app_source_path)
        self.dcc_installed_apps = dict()
        self.dcc_apps_list = (
            "Nuke",
            "Natron",
            "Fusion",
        )
        self.get_dcc_apps_list()
        self.setLayout(self.vlayout)

    def get_dcc_apps_list(self):
        for inst_app_name in self.all_apps_list:
            for dcc_app in self.dcc_apps_list:
                if inst_app_name.startswith(dcc_app):
                    self.create_app_buttons(app_name=inst_app_name, icon_name=dcc_app)

        self.get_software_versions("Blender Foundation", "Blender")
        self.get_software_versions("Autodesk", "Maya")
        self.get_software_versions("Side Effects Software", "Houdini")
        self.get_software_versions("INRIA", "Natron")
        self.get_software_versions("SilhouetteFX", "Silhouette")
        self.get_software_versions("Imagineer Systems Ltd", "Mocha")

    def get_software_versions(self, company_name, software_name):
        for inst_app_name in self.all_apps_list:
            if inst_app_name == company_name:
                softwares_version_list = os.listdir(os.path.join(self.app_source_path, company_name))
                for software_version in softwares_version_list:
                    if software_version.startswith(software_name):
                        self.create_app_buttons(app_name=software_version, icon_name=software_name)

    def create_app_buttons(self, app_name, icon_name):
        if app_name == "Imagineer Systems Ltd":
            app_name = icon_name = "Mocha"
        self.app_button = QPushButton("   "+app_name)
        self.app_button.setFont(QFont("consolas", 10))
        self.app_button.setMinimumSize(QSize(280, 50))
        self.app_button.setIcon(QIcon("./icons/{}.png".format(icon_name)))
        self.app_button.setIconSize(QSize(100, 70))
        self.app_button.setStyleSheet("QPushButton { text-align: left; }")
        self.vlayout.addWidget(self.app_button)
        self.app_button.clicked.connect(lambda: self.launch_application(app_name))
        print(app_name)

    @staticmethod
    def launch_application(app_launch_name):
        cmd = None
        if app_launch_name.startswith("Nuke"):
            nuke_exe = app_launch_name.split("v")[0]
            cmd = fr"C:\Program Files\{app_launch_name}\{nuke_exe}.exe"
        elif app_launch_name.startswith("Natron"):
            cmd = fr"C:\Program Files\INRIA\{app_launch_name}\bin\Natron.exe"
        elif app_launch_name.startswith("Maya"):
            cmd = fr"C:\Program Files\Autodesk\{app_launch_name}\bin\maya.exe"
        elif app_launch_name.startswith("Houdini"):
            cmd = fr"C:\Program Files\Side Effects Software\{app_launch_name}\bin\houdinifx.exe"
        elif app_launch_name == "Blender":
            cmd = fr"C:\Program Files\Blender Foundation\{app_launch_name}\blender.exe"
        elif app_launch_name.startswith("Mocha"):
            cmd = fr"C:\Program Files\Imagineer Systems Ltd\{app_launch_name}\bin\mochapro.exe"
        elif app_launch_name.startswith("Silhouette"):
            cmd = fr"C:\Program Files\SilhouetteFX\{app_launch_name}\Silhouette.exe"
        subprocess.Popen(cmd)


if __name__ == '__main__':
    app = QApplication()
    launcher = ApplauncherUI()
    launcher.show()
    sys.exit(app.exec_())
