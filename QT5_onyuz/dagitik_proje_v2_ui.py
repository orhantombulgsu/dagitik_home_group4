# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dagitik_proje_v2.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(843, 542)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(300, 10, 61, 21))
        self.label_7.setObjectName("label_7")
        self.username_field = QtWidgets.QLineEdit(self.centralwidget)
        self.username_field.setGeometry(QtCore.QRect(380, 45, 142, 25))
        self.username_field.setObjectName("username_field")
        self.connect_button = QtWidgets.QPushButton(self.centralwidget)
        self.connect_button.setGeometry(QtCore.QRect(660, 10, 81, 21))
        self.connect_button.setObjectName("connect_button")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(530, 80, 63, 17))
        self.label_4.setObjectName("label_4")
        self.UserNameLabel_field = QtWidgets.QLabel(self.centralwidget)
        self.UserNameLabel_field.setGeometry(QtCore.QRect(78, 47, 41, 17))
        self.UserNameLabel_field.setObjectName("UserNameLabel_field")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(380, 80, 120, 17))
        self.label_3.setObjectName("label_3")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(210, 80, 132, 17))
        self.label_10.setObjectName("label_10")
        self.SuggestedUser_field = QtWidgets.QListWidget(self.centralwidget)
        self.SuggestedUser_field.setGeometry(QtCore.QRect(380, 100, 121, 159))
        self.SuggestedUser_field.setObjectName("SuggestedUser_field")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(9, 47, 53, 17))
        self.label.setObjectName("label")
        self.RefleshtheFeeds_button = QtWidgets.QPushButton(self.centralwidget)
        self.RefleshtheFeeds_button.setGeometry(QtCore.QRect(50, 470, 131, 21))
        self.RefleshtheFeeds_button.setObjectName("RefleshtheFeeds_button")
        self.UnBlock_button = QtWidgets.QPushButton(self.centralwidget)
        self.UnBlock_button.setGeometry(QtCore.QRect(420, 470, 80, 25))
        self.UnBlock_button.setObjectName("UnBlock_button")
        self.Block_button = QtWidgets.QPushButton(self.centralwidget)
        self.Block_button.setGeometry(QtCore.QRect(550, 470, 80, 25))
        self.Block_button.setObjectName("Block_button")
        self.SendMessage_button = QtWidgets.QPushButton(self.centralwidget)
        self.SendMessage_button.setGeometry(QtCore.QRect(720, 470, 101, 25))
        self.SendMessage_button.setObjectName("SendMessage_button")
        self.Pubkey_button = QtWidgets.QPushButton(self.centralwidget)
        self.Pubkey_button.setGeometry(QtCore.QRect(660, 40, 81, 21))
        self.Pubkey_button.setObjectName("Pubkey_button")
        self.port_field = QtWidgets.QLineEdit(self.centralwidget)
        self.port_field.setGeometry(QtCore.QRect(571, 8, 84, 25))
        self.port_field.setObjectName("port_field")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(531, 8, 30, 17))
        self.label_8.setObjectName("label_8")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(294, 45, 72, 17))
        self.label_15.setObjectName("label_15")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(60, 80, 41, 17))
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(230, 220, 83, 17))
        self.label_11.setObjectName("label_11")
        self.Twit_field = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Twit_field.setGeometry(QtCore.QRect(189, 101, 181, 91))
        self.Twit_field.setObjectName("Twit_field")
        self.Followed_field = QtWidgets.QListWidget(self.centralwidget)
        self.Followed_field.setGeometry(QtCore.QRect(510, 100, 121, 159))
        self.Followed_field.setObjectName("Followed_field")
        self.Share_button = QtWidgets.QPushButton(self.centralwidget)
        self.Share_button.setGeometry(QtCore.QRect(290, 190, 81, 21))
        self.Share_button.setObjectName("Share_button")
        self.UnSubscribe_button = QtWidgets.QPushButton(self.centralwidget)
        self.UnSubscribe_button.setGeometry(QtCore.QRect(510, 260, 121, 25))
        self.UnSubscribe_button.setObjectName("UnSubscribe_button")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(410, 290, 55, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(530, 290, 67, 17))
        self.label_6.setObjectName("label_6")
        self.Blocked_field = QtWidgets.QListWidget(self.centralwidget)
        self.Blocked_field.setGeometry(QtCore.QRect(380, 310, 121, 161))
        self.Blocked_field.setObjectName("Blocked_field")
        self.Followers_field = QtWidgets.QListWidget(self.centralwidget)
        self.Followers_field.setGeometry(QtCore.QRect(510, 310, 121, 161))
        self.Followers_field.setObjectName("Followers_field")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(670, 290, 131, 17))
        self.label_12.setObjectName("label_12")
        self.SendMessage_field = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.SendMessage_field.setGeometry(QtCore.QRect(640, 310, 181, 161))
        self.SendMessage_field.setObjectName("SendMessage_field")
        self.LogLabel_field = QtWidgets.QLabel(self.centralwidget)
        self.LogLabel_field.setGeometry(QtCore.QRect(9, 492, 811, 17))
        self.LogLabel_field.setObjectName("LogLabel_field")
        self.LogOut_button = QtWidgets.QPushButton(self.centralwidget)
        self.LogOut_button.setGeometry(QtCore.QRect(750, 10, 71, 21))
        self.LogOut_button.setObjectName("LogOut_button")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(710, 80, 42, 17))
        self.label_13.setObjectName("label_13")
        self.Feeds_field = QtWidgets.QListWidget(self.centralwidget)
        self.Feeds_field.setGeometry(QtCore.QRect(10, 100, 171, 371))
        self.Feeds_field.setObjectName("Feeds_field")
        self.MyBlogList_field = QtWidgets.QListWidget(self.centralwidget)
        self.MyBlogList_field.setGeometry(QtCore.QRect(190, 240, 181, 231))
        self.MyBlogList_field.setObjectName("MyBlogList_field")
        self.Subscribe_button = QtWidgets.QPushButton(self.centralwidget)
        self.Subscribe_button.setGeometry(QtCore.QRect(379, 260, 121, 25))
        self.Subscribe_button.setObjectName("Subscribe_button")
        self.Inbox_field = QtWidgets.QListView(self.centralwidget)
        self.Inbox_field.setGeometry(QtCore.QRect(640, 100, 181, 181))
        self.Inbox_field.setObjectName("Inbox_field")
        self.ip_field = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_field.setGeometry(QtCore.QRect(380, 10, 142, 25))
        self.ip_field.setObjectName("ip_field")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(9, 9, 276, 32))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.sugchbx1 = QtWidgets.QCheckBox(self.centralwidget)
        self.sugchbx1.setGeometry(QtCore.QRect(390, 118, 101, 23))
        self.sugchbx1.setObjectName("sugchbx1")
        self.sugchbx3 = QtWidgets.QCheckBox(self.centralwidget)
        self.sugchbx3.setGeometry(QtCore.QRect(390, 158, 101, 23))
        self.sugchbx3.setObjectName("sugchbx3")
        self.sugchbx5 = QtWidgets.QCheckBox(self.centralwidget)
        self.sugchbx5.setGeometry(QtCore.QRect(390, 198, 101, 23))
        self.sugchbx5.setObjectName("sugchbx5")
        self.sugchbx4 = QtWidgets.QCheckBox(self.centralwidget)
        self.sugchbx4.setGeometry(QtCore.QRect(390, 178, 101, 23))
        self.sugchbx4.setObjectName("sugchbx4")
        self.sugchbx2 = QtWidgets.QCheckBox(self.centralwidget)
        self.sugchbx2.setGeometry(QtCore.QRect(390, 140, 101, 21))
        self.sugchbx2.setObjectName("sugchbx2")
        self.users_button = QtWidgets.QPushButton(self.centralwidget)
        self.users_button.setGeometry(QtCore.QRect(750, 40, 71, 21))
        self.users_button.setObjectName("users_button")
        self.blkchbx3 = QtWidgets.QCheckBox(self.centralwidget)
        self.blkchbx3.setGeometry(QtCore.QRect(390, 360, 101, 23))
        self.blkchbx3.setObjectName("blkchbx3")
        self.blkchbx1 = QtWidgets.QCheckBox(self.centralwidget)
        self.blkchbx1.setGeometry(QtCore.QRect(390, 320, 101, 23))
        self.blkchbx1.setObjectName("blkchbx1")
        self.blkchbx2 = QtWidgets.QCheckBox(self.centralwidget)
        self.blkchbx2.setGeometry(QtCore.QRect(390, 340, 101, 23))
        self.blkchbx2.setObjectName("blkchbx2")
        self.blkchbx5 = QtWidgets.QCheckBox(self.centralwidget)
        self.blkchbx5.setGeometry(QtCore.QRect(390, 400, 101, 23))
        self.blkchbx5.setObjectName("blkchbx5")
        self.blkchbx4 = QtWidgets.QCheckBox(self.centralwidget)
        self.blkchbx4.setGeometry(QtCore.QRect(390, 380, 101, 23))
        self.blkchbx4.setObjectName("blkchbx4")
        self.flwchbx3 = QtWidgets.QCheckBox(self.centralwidget)
        self.flwchbx3.setGeometry(QtCore.QRect(520, 360, 101, 23))
        self.flwchbx3.setObjectName("flwchbx3")
        self.flwchbx1 = QtWidgets.QCheckBox(self.centralwidget)
        self.flwchbx1.setGeometry(QtCore.QRect(520, 320, 101, 23))
        self.flwchbx1.setObjectName("flwchbx1")
        self.flwchbx2 = QtWidgets.QCheckBox(self.centralwidget)
        self.flwchbx2.setGeometry(QtCore.QRect(520, 340, 101, 23))
        self.flwchbx2.setObjectName("flwchbx2")
        self.flwchbx5 = QtWidgets.QCheckBox(self.centralwidget)
        self.flwchbx5.setGeometry(QtCore.QRect(520, 400, 101, 23))
        self.flwchbx5.setObjectName("flwchbx5")
        self.flwchbx4 = QtWidgets.QCheckBox(self.centralwidget)
        self.flwchbx4.setGeometry(QtCore.QRect(520, 380, 101, 23))
        self.flwchbx4.setObjectName("flwchbx4")
        self.fldchbx1 = QtWidgets.QCheckBox(self.centralwidget)
        self.fldchbx1.setGeometry(QtCore.QRect(520, 120, 101, 23))
        self.fldchbx1.setObjectName("fldchbx1")
        self.fldchbx2 = QtWidgets.QCheckBox(self.centralwidget)
        self.fldchbx2.setGeometry(QtCore.QRect(520, 140, 101, 23))
        self.fldchbx2.setObjectName("fldchbx2")
        self.fldchbx3 = QtWidgets.QCheckBox(self.centralwidget)
        self.fldchbx3.setGeometry(QtCore.QRect(520, 160, 101, 23))
        self.fldchbx3.setObjectName("fldchbx3")
        self.fldchbx4 = QtWidgets.QCheckBox(self.centralwidget)
        self.fldchbx4.setGeometry(QtCore.QRect(520, 180, 101, 23))
        self.fldchbx4.setObjectName("fldchbx4")
        self.fldchbx5 = QtWidgets.QCheckBox(self.centralwidget)
        self.fldchbx5.setGeometry(QtCore.QRect(520, 200, 101, 23))
        self.fldchbx5.setObjectName("fldchbx5")
        self.Blocked_field.raise_()
        self.Followers_field.raise_()
        self.Followed_field.raise_()
        self.SuggestedUser_field.raise_()
        self.label_7.raise_()
        self.username_field.raise_()
        self.connect_button.raise_()
        self.label_4.raise_()
        self.UserNameLabel_field.raise_()
        self.label_3.raise_()
        self.label_10.raise_()
        self.label.raise_()
        self.RefleshtheFeeds_button.raise_()
        self.UnBlock_button.raise_()
        self.Block_button.raise_()
        self.SendMessage_button.raise_()
        self.Pubkey_button.raise_()
        self.port_field.raise_()
        self.label_8.raise_()
        self.label_15.raise_()
        self.label_9.raise_()
        self.label_11.raise_()
        self.Twit_field.raise_()
        self.Share_button.raise_()
        self.UnSubscribe_button.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_12.raise_()
        self.SendMessage_field.raise_()
        self.LogLabel_field.raise_()
        self.LogOut_button.raise_()
        self.label_13.raise_()
        self.Feeds_field.raise_()
        self.MyBlogList_field.raise_()
        self.Subscribe_button.raise_()
        self.Inbox_field.raise_()
        self.ip_field.raise_()
        self.label_14.raise_()
        self.sugchbx1.raise_()
        self.sugchbx3.raise_()
        self.sugchbx5.raise_()
        self.sugchbx4.raise_()
        self.sugchbx2.raise_()
        self.users_button.raise_()
        self.fldchbx3.raise_()
        self.fldchbx1.raise_()
        self.fldchbx2.raise_()
        self.fldchbx5.raise_()
        self.fldchbx4.raise_()
        self.blkchbx3.raise_()
        self.blkchbx1.raise_()
        self.blkchbx2.raise_()
        self.blkchbx5.raise_()
        self.blkchbx4.raise_()
        self.flwchbx3.raise_()
        self.flwchbx1.raise_()
        self.flwchbx2.raise_()
        self.flwchbx5.raise_()
        self.flwchbx4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 843, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "Ip :"))
        self.connect_button.setText(_translate("MainWindow", "Connect"))
        self.label_4.setText(_translate("MainWindow", "Followed"))
        self.UserNameLabel_field.setText(_translate("MainWindow", "Name"))
        self.label_3.setText(_translate("MainWindow", "Suggestted Users"))
        self.label_10.setText(_translate("MainWindow", "What\'s happening ?"))
        self.label.setText(_translate("MainWindow", "Profile :"))
        self.RefleshtheFeeds_button.setText(_translate("MainWindow", "Refresh the Feeds"))
        self.UnBlock_button.setText(_translate("MainWindow", "UnBlock"))
        self.Block_button.setText(_translate("MainWindow", "Block"))
        self.SendMessage_button.setText(_translate("MainWindow", "Send Message"))
        self.Pubkey_button.setText(_translate("MainWindow", "PubKey"))
        self.label_8.setText(_translate("MainWindow", "Port"))
        self.label_15.setText(_translate("MainWindow", "UserName"))
        self.label_9.setText(_translate("MainWindow", "Feeds"))
        self.label_11.setText(_translate("MainWindow", "My Blog List"))
        self.Share_button.setText(_translate("MainWindow", "Share"))
        self.UnSubscribe_button.setText(_translate("MainWindow", "UnSubscribe"))
        self.label_5.setText(_translate("MainWindow", "Blocked"))
        self.label_6.setText(_translate("MainWindow", "Followers"))
        self.label_12.setText(_translate("MainWindow", "Send Message"))
        self.LogLabel_field.setText(_translate("MainWindow", "LogLabel"))
        self.LogOut_button.setText(_translate("MainWindow", "LogOut"))
        self.label_13.setText(_translate("MainWindow", "Inbox "))
        self.Subscribe_button.setText(_translate("MainWindow", "Subscribe"))
        self.label_14.setText(_translate("MainWindow", "TWITTER from Group4"))
        self.sugchbx1.setText(_translate("MainWindow", "sugusr1"))
        self.sugchbx3.setText(_translate("MainWindow", "sugusr3"))
        self.sugchbx5.setText(_translate("MainWindow", "sugusr5"))
        self.sugchbx4.setText(_translate("MainWindow", "sugusr4"))
        self.sugchbx2.setText(_translate("MainWindow", "sugusr2"))
        self.users_button.setText(_translate("MainWindow", "Users"))
        self.blkchbx3.setText(_translate("MainWindow", "blkusr3"))
        self.blkchbx1.setText(_translate("MainWindow", "blkusr1"))
        self.blkchbx2.setText(_translate("MainWindow", "blkusr2"))
        self.blkchbx5.setText(_translate("MainWindow", "blkusr5"))
        self.blkchbx4.setText(_translate("MainWindow", "blkusr4"))
        self.flwchbx3.setText(_translate("MainWindow", "flwusr3"))
        self.flwchbx1.setText(_translate("MainWindow", "flwusr1"))
        self.flwchbx2.setText(_translate("MainWindow", "flwusr2"))
        self.flwchbx5.setText(_translate("MainWindow", "flwusr5"))
        self.flwchbx4.setText(_translate("MainWindow", "flwusr4"))
        self.fldchbx1.setText(_translate("MainWindow", "fldusr1"))
        self.fldchbx2.setText(_translate("MainWindow", "fldusr2"))
        self.fldchbx3.setText(_translate("MainWindow", "fldusr3"))
        self.fldchbx4.setText(_translate("MainWindow", "fldusr4"))
        self.fldchbx5.setText(_translate("MainWindow", "fldusr5"))
