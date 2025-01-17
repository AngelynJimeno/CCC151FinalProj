# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceFtLuLu.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

from Custom_Widgets.Widgets import QCustomSlideMenu
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(978, 481)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	color: #000;\n"
"	border: none;\n"
"}\n"
"#centralwidget{\n"
"	background-color: #F0F0F0;\n"
"\n"
"}\n"
" #frame_11{\n"
"	background-color: #2596be;\n"
"}\n"
"QLineEdit{\n"
"	background: transparent;\n"
"	color: #2596be;\n"
"}\n"
"#searchFrame{\n"
"	border-radius: 10px;\n"
"	border: 2px solid #2596be;\n"
"}\n"
"#appHeader{\n"
"	color: #2596be;\n"
"}\n"
"#card1, #card2, #card3, #card4 {\n"
"	background-color: #fefeff;\n"
"	border-radius: 20px;\n"
"}\n"
"#pushButton, #pushButton_2{\n"
"	background-color: #2596be;\n"
"	color: #fff;\n"
"	border-radius: 10px;\n"
"}\n"
"#widget_4, #widget_5, #profileCont, #frame_15{\n"
"	background-color: #fefeff;\n"
"	border-radius: 20px;\n"
"}\n"
"#headerFrame{\n"
"	background-color: #fefeff;\n"
"}\n"
"#pushButton_3{\n"
"	background-color: #fefeff;\n"
"	padding: 10px 5px;\n"
"	text-align: left;\n"
"	border-top-left-radius: 20px ;\n"
"}\n"
"QPushButton{\n"
"	padding: 10px 5px;\n"
"	text-align: left;\n"
"}\n"
"#mainBody\n"
"{\n"
"	background-color:#F0F0F0\n"
"}\n"
"#leftMenu"
                        "\n"
"{\n"
"	background-color:#31302E\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QCustomSlideMenu(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.verticalLayout_7 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.leftMenu)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_11)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(15, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_58 = QLabel(self.frame_12)
        self.label_58.setObjectName(u"label_58")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_58.setFont(font)

        self.horizontalLayout_16.addWidget(self.label_58, 0, Qt.AlignTop)


        self.verticalLayout_8.addWidget(self.frame_12, 0, Qt.AlignTop)

        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_13)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy1)
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_14)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.frame_14)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setIconSize(QSize(24, 24))

        self.verticalLayout_9.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_14)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setIconSize(QSize(24, 24))

        self.verticalLayout_9.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_14)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setIconSize(QSize(24, 24))

        self.verticalLayout_9.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_14)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setIconSize(QSize(24, 24))

        self.verticalLayout_9.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.frame_14)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setIconSize(QSize(24, 24))

        self.verticalLayout_9.addWidget(self.pushButton_7)


        self.verticalLayout_10.addWidget(self.frame_14, 0, Qt.AlignTop)


        self.verticalLayout_8.addWidget(self.frame_13)


        self.verticalLayout_7.addWidget(self.frame_11)


        self.horizontalLayout.addWidget(self.leftMenu)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        self.verticalLayout = QVBoxLayout(self.mainBody)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.headerFrame = QWidget(self.mainBody)
        self.headerFrame.setObjectName(u"headerFrame")
        self.horizontalLayout_2 = QHBoxLayout(self.headerFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 10)
        self.widget = QWidget(self.headerFrame)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.menuBtn = QPushButton(self.widget)
        self.menuBtn.setObjectName(u"menuBtn")
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.menuBtn)

        self.appHeader = QLabel(self.widget)
        self.appHeader.setObjectName(u"appHeader")
        self.appHeader.setFont(font)

        self.horizontalLayout_3.addWidget(self.appHeader)


        self.horizontalLayout_2.addWidget(self.widget, 0, Qt.AlignLeft)

        self.widget_2 = QWidget(self.headerFrame)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.searchFrame = QFrame(self.widget_2)
        self.searchFrame.setObjectName(u"searchFrame")
        self.searchFrame.setFrameShape(QFrame.StyledPanel)
        self.searchFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.searchFrame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.searchFrame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_5.addWidget(self.lineEdit)

        self.label_2 = QLabel(self.searchFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(30, 30))
        self.label_2.setMaximumSize(QSize(30, 30))
        self.label_2.setPixmap(QPixmap(u":/icons/icons/search.svg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_2)


        self.horizontalLayout_4.addWidget(self.searchFrame, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.widget_2, 0, Qt.AlignHCenter)

        self.widget_3 = QWidget(self.headerFrame)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.accountBtn = QPushButton(self.widget_3)
        self.accountBtn.setObjectName(u"accountBtn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.accountBtn.setIcon(icon1)
        self.accountBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.accountBtn)


        self.horizontalLayout_2.addWidget(self.widget_3, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.headerFrame, 0, Qt.AlignTop)

        self.cardsFrame = QWidget(self.mainBody)
        self.cardsFrame.setObjectName(u"cardsFrame")
        self.horizontalLayout_7 = QHBoxLayout(self.cardsFrame)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.card1 = QFrame(self.cardsFrame)
        self.card1.setObjectName(u"card1")
        self.card1.setMinimumSize(QSize(160, 0))
        self.card1.setFrameShape(QFrame.StyledPanel)
        self.card1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.card1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.card1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        self.label.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(40, 40))
        self.label_3.setPixmap(QPixmap(u":/icons/icons/list.svg"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_3)


        self.verticalLayout_3.addWidget(self.frame, 0, Qt.AlignTop)

        self.label_4 = QLabel(self.card1)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.label_4.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_4)

        self.label_5 = QLabel(self.card1)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)


        self.horizontalLayout_7.addWidget(self.card1)

        self.card2 = QFrame(self.cardsFrame)
        self.card2.setObjectName(u"card2")
        self.card2.setMinimumSize(QSize(160, 0))
        self.card2.setFrameShape(QFrame.StyledPanel)
        self.card2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.card2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.card2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.horizontalLayout_11.addWidget(self.label_12)

        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(40, 40))
        self.label_13.setPixmap(QPixmap(u":/icons/icons/list.svg"))
        self.label_13.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.label_13)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.label_9 = QLabel(self.card2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_9, 0, Qt.AlignTop)

        self.label_8 = QLabel(self.card2)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_2.addWidget(self.label_8, 0, Qt.AlignTop)


        self.horizontalLayout_7.addWidget(self.card2)

        self.card3 = QFrame(self.cardsFrame)
        self.card3.setObjectName(u"card3")
        self.card3.setMinimumSize(QSize(160, 0))
        self.card3.setFrameShape(QFrame.StyledPanel)
        self.card3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.card3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_3 = QFrame(self.card3)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_16 = QLabel(self.frame_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.horizontalLayout_12.addWidget(self.label_16)

        self.label_17 = QLabel(self.frame_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(40, 40))
        self.label_17.setPixmap(QPixmap(u":/icons/icons/list.svg"))
        self.label_17.setScaledContents(True)

        self.horizontalLayout_12.addWidget(self.label_17)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.label_15 = QLabel(self.card3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_15, 0, Qt.AlignTop)

        self.label_14 = QLabel(self.card3)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_4.addWidget(self.label_14)


        self.horizontalLayout_7.addWidget(self.card3)

        self.card4 = QFrame(self.cardsFrame)
        self.card4.setObjectName(u"card4")
        self.card4.setMinimumSize(QSize(160, 0))
        self.card4.setFrameShape(QFrame.StyledPanel)
        self.card4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.card4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_4 = QFrame(self.card4)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_20 = QLabel(self.frame_4)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)

        self.horizontalLayout_13.addWidget(self.label_20)

        self.label_21 = QLabel(self.frame_4)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(40, 40))
        self.label_21.setPixmap(QPixmap(u":/icons/icons/list.svg"))
        self.label_21.setScaledContents(True)

        self.horizontalLayout_13.addWidget(self.label_21)


        self.verticalLayout_5.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.label_19 = QLabel(self.card4)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_19, 0, Qt.AlignTop)

        self.label_18 = QLabel(self.card4)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_5.addWidget(self.label_18, 0, Qt.AlignTop)


        self.horizontalLayout_7.addWidget(self.card4)


        self.verticalLayout.addWidget(self.cardsFrame)

        self.mainFrame = QWidget(self.mainBody)
        self.mainFrame.setObjectName(u"mainFrame")
        sizePolicy.setHeightForWidth(self.mainFrame.sizePolicy().hasHeightForWidth())
        self.mainFrame.setSizePolicy(sizePolicy)
        self.horizontalLayout_14 = QHBoxLayout(self.mainFrame)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.widget_4 = QWidget(self.mainFrame)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_6 = QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_5 = QFrame(self.widget_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_22 = QLabel(self.frame_5)
        self.label_22.setObjectName(u"label_22")
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(True)
        self.label_22.setFont(font3)

        self.horizontalLayout_15.addWidget(self.label_22, 0, Qt.AlignLeft)

        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/arrow-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_15.addWidget(self.pushButton, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_5, 0, Qt.AlignTop)

        self.frame_6 = QFrame(self.widget_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_23 = QLabel(self.frame_6)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(110, 20, 131, 16))

        self.verticalLayout_6.addWidget(self.frame_6)


        self.horizontalLayout_14.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.mainFrame)
        self.widget_5.setObjectName(u"widget_5")
        self.gif = QLabel(self.widget_5)
        self.gif.setObjectName(u"gif")
        self.gif.setGeometry(QRect(0, -5, 341, 271))
        self.gif.setPixmap(QPixmap(u"../OneDrive/Desktop/ccc151final/gifsample.gif"))
        self.gif.setScaledContents(True)

        self.horizontalLayout_14.addWidget(self.widget_5)


        self.verticalLayout.addWidget(self.mainFrame)


        self.horizontalLayout.addWidget(self.mainBody)

        self.profileCont = QCustomSlideMenu(self.centralwidget)
        self.profileCont.setObjectName(u"profileCont")
        self.profileCont.setMinimumSize(QSize(100, 0))
        self.verticalLayout_11 = QVBoxLayout(self.profileCont)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.profileCont)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_15)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_59 = QLabel(self.frame_15)
        self.label_59.setObjectName(u"label_59")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        self.label_59.setFont(font4)
        self.label_59.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_59, 0, Qt.AlignTop)

        self.label_60 = QLabel(self.frame_15)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font4)
        self.label_60.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_60, 0, Qt.AlignTop)

        self.label_61 = QLabel(self.frame_15)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMinimumSize(QSize(50, 50))
        self.label_61.setMaximumSize(QSize(50, 50))
        self.label_61.setPixmap(QPixmap(u"../OneDrive/Desktop/ccc151final/gifsample.gif"))
        self.label_61.setScaledContents(True)
        self.label_61.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_61, 0, Qt.AlignHCenter)

        self.pushButton_8 = QPushButton(self.frame_15)
        self.pushButton_8.setObjectName(u"pushButton_8")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon3)

        self.verticalLayout_12.addWidget(self.pushButton_8)


        self.verticalLayout_11.addWidget(self.frame_15, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.profileCont, 0, Qt.AlignTop)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"TechAbangan", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Tenants", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Units", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Rentals", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Payments", None))
        self.menuBtn.setText("")
        self.appHeader.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_2.setText("")
        self.accountBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"TOTAL RENTALS", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"72", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"+20% month over month", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"TOTAL TENANTS", None))
        self.label_13.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"2,405", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"+33% month over month", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"AVAILABLE UNITS", None))
        self.label_17.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"24", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"??????", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"TOTAL INCOME", None))
        self.label_21.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"$45,678.90", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"+20% month over month", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"TOTAL INCOME", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"View More", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"line graph ni", None))
        self.gif.setText("")
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"TechAbangan", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Admin", None))
        self.label_61.setText("")
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
    # retranslateUi

