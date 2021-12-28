import os
import sys
import subprocess

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *


apps_dict = {
            "Blender Foundation": "Blender",
            "Autodesk": "Maya",
            "Side Effects Software": "Houdini",
            "INRIA": "Natron",
            "SilhouetteFX": "Silhouette",
            "Imagineer Systems Ltd": "Mocha",
            "Adobe": ["Adobe Photoshop", "Adobe Premiere", "Adobe After Effects"]
        }


class ApplauncherUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Smart Launch")
        self.setMinimumSize(400, 600)
        self.vlayout = QVBoxLayout()
        self.list_widget = QListWidget()
        self.list_widget.setSelectionMode(QAbstractItemView.NoSelection)
        self.list_widget.setStyleSheet("""
            QScrollBar:vertical{
            height: 25px;
            width: 10px;
            }
            QScrollBar::handle {
            background: grey;
            border-radius: 5px;
            }
        """)

        self.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.setWindowIcon(QIcon("./icons/launcher.ico"))
        self.app_source_path = r"C:\Program Files"
        self.all_apps_list = os.listdir(self.app_source_path)
        self.dcc_installed_apps = dict()
        self.dcc_apps_list = (
            "Nuke", "Natron", "Fusion",
        )
        self.get_dcc_apps_list()
        self.vlayout.addWidget(self.list_widget)
        self.setLayout(self.vlayout)

    def get_dcc_apps_list(self):
        for inst_app_name in self.all_apps_list:
            for dcc_app in self.dcc_apps_list:
                if inst_app_name.startswith(dcc_app):
                    self.create_app_buttons(app_name=inst_app_name, icon_name=dcc_app)

        for company_name in apps_dict.keys():
            if company_name == "Adobe":
                for adobe_app in apps_dict["Adobe"]:
                    self.get_software_versions(company_name, adobe_app)
            else:
                self.get_software_versions(company_name, apps_dict[company_name])

    def get_software_versions(self, company_name, software_name):
        for inst_app_name in self.all_apps_list:
            if inst_app_name == company_name:
                softwares_version_list = os.listdir(os.path.join(self.app_source_path, company_name))
                for software_version in softwares_version_list:
                    if software_version.startswith(software_name):
                        self.create_app_buttons(app_name=software_version, icon_name=software_name)

    def create_app_buttons(self, app_name, icon_name):
        self.app_button = QPushButton("   " + app_name)
        self.app_button.setFont(QFont("consolas", 10))
        self.app_button.setStyleSheet("""
        QPushButton {
        color: rgb(76, 78, 93);
        background-color: rgb(245, 245, 245);
        text-align: left;
        border-radius:25px;
        }
        QPushButton:pressed{
        color:green;
        background-color: rgb(200, 200, 200);
        }
        """
                                      )
        item = QListWidgetItem(self.list_widget)
        item.setSizeHint(QSize(30, 70))
        self.app_button.setIcon(QIcon("./icons/{}.png".format(icon_name)))
        self.app_button.setIconSize(QSize(100, 70))
        self.list_widget.setItemWidget(item, self.app_button)
        self.list_widget.setSpacing(3)
        self.app_button.clicked.connect(lambda: self.launch_application(app_name))

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
        elif app_launch_name.startswith("Blender"):
            cmd = fr"C:\Program Files\Blender Foundation\{app_launch_name}\blender.exe"
        elif app_launch_name.startswith("Mocha"):
            cmd = fr"C:\Program Files\Imagineer Systems Ltd\{app_launch_name}\bin\mochapro.exe"
        elif app_launch_name.startswith("Silhouette"):
            cmd = fr"C:\Program Files\SilhouetteFX\{app_launch_name}\Silhouette.exe"
        elif app_launch_name.startswith("Adobe Premiere"):
            cmd = fr"C:\Program Files\Adobe\{app_launch_name}\Adobe Premiere Pro.exe"
        elif app_launch_name.startswith("Adobe Photoshop"):
            cmd = fr"C:\Program Files\Adobe\{app_launch_name}\Photoshop.exe"
        elif app_launch_name.startswith("Adobe After Effects"):
            cmd = fr"C:\Program Files\Adobe\{app_launch_name}\Support Files\AfterFX.exe"
        subprocess.Popen(cmd)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    launcher = ApplauncherUI()
    launcher.show()
    sys.exit(app.exec_())
