# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\view\SecondForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(411, 270)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(-1, -1, 9, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.color_selected_recog_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.color_selected_recog_label.setFont(font)
        self.color_selected_recog_label.setObjectName("color_selected_recog_label")
        self.horizontalLayout_4.addWidget(self.color_selected_recog_label)
        self.color_selected_recog_toolButton = QtWidgets.QToolButton(self.frame)
        self.color_selected_recog_toolButton.setObjectName("color_selected_recog_toolButton")
        self.horizontalLayout_4.addWidget(self.color_selected_recog_toolButton)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.color_signature_recog_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.color_signature_recog_label.setFont(font)
        self.color_signature_recog_label.setObjectName("color_signature_recog_label")
        self.horizontalLayout_6.addWidget(self.color_signature_recog_label)
        self.color_signature_recog_toolButton = QtWidgets.QToolButton(self.frame)
        self.color_signature_recog_toolButton.setObjectName("color_signature_recog_toolButton")
        self.horizontalLayout_6.addWidget(self.color_signature_recog_toolButton)
        self.gridLayout.addLayout(self.horizontalLayout_6, 5, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scale_x_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.scale_x_label.setFont(font)
        self.scale_x_label.setObjectName("scale_x_label")
        self.horizontalLayout_2.addWidget(self.scale_x_label)
        self.scale_x_comboBox = QtWidgets.QComboBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.scale_x_comboBox.setFont(font)
        self.scale_x_comboBox.setObjectName("scale_x_comboBox")
        self.horizontalLayout_2.addWidget(self.scale_x_comboBox)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scaley_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.scaley_label.setFont(font)
        self.scaley_label.setObjectName("scaley_label")
        self.horizontalLayout.addWidget(self.scaley_label)
        self.scale_y_comboBox = QtWidgets.QComboBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.scale_y_comboBox.setFont(font)
        self.scale_y_comboBox.setObjectName("scale_y_comboBox")
        self.horizontalLayout.addWidget(self.scale_y_comboBox)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_3.setSpacing(30)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.recog_error_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.recog_error_label.setFont(font)
        self.recog_error_label.setObjectName("recog_error_label")
        self.horizontalLayout_3.addWidget(self.recog_error_label)
        self.recog_error_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.recog_error_doubleSpinBox.setFont(font)
        self.recog_error_doubleSpinBox.setDecimals(1)
        self.recog_error_doubleSpinBox.setMaximum(1.0)
        self.recog_error_doubleSpinBox.setSingleStep(0.1)
        self.recog_error_doubleSpinBox.setProperty("value", 0.6)
        self.recog_error_doubleSpinBox.setObjectName("recog_error_doubleSpinBox")
        self.horizontalLayout_3.addWidget(self.recog_error_doubleSpinBox)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.color_unselected_recog_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.color_unselected_recog_label.setFont(font)
        self.color_unselected_recog_label.setObjectName("color_unselected_recog_label")
        self.horizontalLayout_5.addWidget(self.color_unselected_recog_label)
        self.color_unselected_recog_toolButton = QtWidgets.QToolButton(self.frame)
        self.color_unselected_recog_toolButton.setObjectName("color_unselected_recog_toolButton")
        self.horizontalLayout_5.addWidget(self.color_unselected_recog_toolButton)
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.ok_pushButton = QtWidgets.QPushButton(self.frame)
        self.ok_pushButton.setObjectName("ok_pushButton")
        self.horizontalLayout_7.addWidget(self.ok_pushButton)
        self.cancel_pushButton = QtWidgets.QPushButton(self.frame)
        self.cancel_pushButton.setObjectName("cancel_pushButton")
        self.horizontalLayout_7.addWidget(self.cancel_pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_7, 6, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        color = QtGui.QColor(0, 0, 0)
        self.color_selected_recog_toolButton.clicked.connect(self.color_picker)

        #self.cancel_pushButton.clicked.connect(self.cancel)

   # def cancel(self):

        

    def color_picker(self):
        # opening color dialog
        self.color = QtWidgets.QColorDialog(self).getColor()
        # self.color.setOptions(QtWidgets.QColorDialog.DontUseNativeDialog)
        self.color.show()


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.color_selected_recog_label.setText(_translate("Form", "Цвет выделения распознанного лица"))
        self.color_selected_recog_toolButton.setText(_translate("Form", "..."))
        self.color_signature_recog_label.setText(_translate("Form", "Цвет подписи распознанного лица"))
        self.color_signature_recog_toolButton.setText(_translate("Form", "..."))
        self.scale_x_label.setText(_translate("Form", "Масштаб кадра обработки по X"))
        self.scaley_label.setText(_translate("Form", "Масштаб кадра обработки по У"))
        self.recog_error_label.setText(_translate("Form", "Погрешность распознавания"))
        self.color_unselected_recog_label.setText(_translate("Form", "Цвет выделения неизвестного лица"))
        self.color_unselected_recog_toolButton.setText(_translate("Form", "..."))
        self.ok_pushButton.setText(_translate("Form", "ОК"))
        self.cancel_pushButton.setText(_translate("Form", "Отменить"))

