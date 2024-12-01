# Form implementation generated from reading ui file 'SDEV220_final_project_UI.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6 import QtCore, QtGui, QtWidgets
from db import open_connection



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(848, 582)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.columnView_2 = QtWidgets.QColumnView(parent=self.centralwidget)
        self.columnView_2.setGeometry(QtCore.QRect(0, 0, 381, 501))
        self.columnView_2.setObjectName("columnView_2")
        self.columnView = QtWidgets.QColumnView(parent=self.centralwidget)
        self.columnView.setGeometry(QtCore.QRect(375, 0, 421, 501))
        self.columnView.setObjectName("columnView")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 371, 501))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.path_vertical_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.path_vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.path_vertical_layout.setObjectName("path_vertical_layout")

        #skill_label
        self.skill_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.skill_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.skill_label.setObjectName("skill_label")
        self.path_vertical_layout.addWidget(self.skill_label)

        #skill combo box
        self.skill_combo_box = QtWidgets.QComboBox(parent=self.verticalLayoutWidget)
        self.skill_combo_box.setObjectName("skill_combo_box")
        self.path_vertical_layout.addWidget(self.skill_combo_box)

        #populate items from database
        items = ["", "Cloud security", 
        "Cyber Defense & Blue Team Operations",
        "Offensive Operations",
        "Digital Forensics and Incident Response",
        "Industrial Control Systems (ICS)",
        "Cyber Security Leadership"]
        self.skill_combo_box.addItems(items)
        self.skill_combo_box.currentIndexChanged.connect(self.on_skill_combo_box_changed)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.path_vertical_layout.addItem(spacerItem)
        
        #role_label
        self.role_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.role_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.role_label.setObjectName("role_label")
        self.path_vertical_layout.addWidget(self.role_label)

        #role combo box
        self.rol_combo_box = QtWidgets.QComboBox(parent=self.verticalLayoutWidget)
        self.rol_combo_box.setObjectName("rol_combo_box")
        self.rol_combo_box.currentIndexChanged.connect(self.on_rol_combo_box_changed)

        self.path_vertical_layout.addWidget(self.rol_combo_box)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.path_vertical_layout.addItem(spacerItem1)

        #role_list_view
        #self.Role_list_view = QtWidgets.QListWidget(parent=self.verticalLayoutWidget)
        self.Role_list_view = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.Role_list_view.setObjectName("Role_list_view")
        self.path_vertical_layout.addWidget(self.Role_list_view)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(380, 0, 421, 501))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        #skill description
        self.skill_description = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.skill_description.setObjectName("skill_description")
        self.verticalLayout_2.addWidget(self.skill_description)

        #skill list
        #self.skill_description_list = QtWidgets.QListWidget(parent=self.verticalLayoutWidget_2)
        self.skill_description_list = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)

        self.skill_description_list.setObjectName("skill_description_list")
        self.verticalLayout_2.addWidget(self.skill_description_list)

        self.role_description_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.role_description_label.setObjectName("role_description_label")
        self.verticalLayout_2.addWidget(self.role_description_label)
        
        #self.Role_description_list = QtWidgets.QListWidget(parent=self.verticalLayoutWidget_2)
        self.Role_description_list = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)

        self.Role_description_list.setObjectName("Role_description_list")
        self.verticalLayout_2.addWidget(self.Role_description_list)
        self.classes_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.classes_label.setObjectName("classes_label")
        self.verticalLayout_2.addWidget(self.classes_label)
        self.Class_list = QtWidgets.QListWidget(parent=self.verticalLayoutWidget_2)
        self.Class_list.setObjectName("Class_list")
        self.verticalLayout_2.addWidget(self.Class_list)
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 500, 111, 41))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 848, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.skill_label.setText(_translate("MainWindow", "Skill Path"))        
        self.skill_description.setText(_translate("MainWindow", "Skill Description"))

        self.role_label.setText(_translate("MainWindow", "Role Path"))
        self.role_description_label.setText(_translate("MainWindow", "Role Description"))

        self.classes_label.setText(_translate("MainWindow", "Classes"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))

    def on_skill_combo_box_changed(self, index):
        print("skill combo selected")
        selectedItem = self.skill_combo_box.currentText()
        if selectedItem == "Cloud security":
            ItemDescription = "Our SANS Cyber Defense curriculum provides intensive, immersion training designed to help you and your staff master the practical steps necessary for defending your organization assets in the cloud"
            self.skill_description_list.setText(ItemDescription) 
        
        if selectedItem == "Cloud security":
            items = ["",
                    "Cloud security Analyst", 
                    "Cloud Security Engineer",
                    "Cloud Security Architect",
                    "Cloud Security Manager",
                    "Cloud Threat Detection"]
            self.rol_combo_box.addItems(items)

    def on_rol_combo_box_changed(self, index):            
        print("role combo selected")
        selectedItem = self.rol_combo_box.currentText()
        if selectedItem == "Cloud security Analyst":
            roledescription = "Cloud security Analyst: Using cloud security solutions to respond to incidents and enable defenses"
            #print(roledescription)
            #self.role_description_label.setText(roledescription) 
            self.Role_list_view.setText(roledescription)
            items = ["SEC388	Introduction to Cloud Computing and Security",
                    "SEC488	Cloud Security Essentials",
                    "SEC510	Cloud Security Controls and Mitigations",
                    "SEC541	Cloud Security Threat Detection"]
            self.Class_list.addItems(items)

if __name__ == "__main__":
    import sys
    from PyQt6.QtSql import QSqlDatabase

    app = QtWidgets.QApplication(sys.argv)
    if not open_connection():
        sys.exit(1)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    QSqlDatabase.close()
    sys.exit(app.exec())