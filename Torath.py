import sys

from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,QLabel,\
    QComboBox,QVBoxLayout,QHBoxLayout,QLineEdit

class Comp(QWidget):
    def __init__(self):
        super(Comp, self).__init__()
        self.lbl = QLabel('')
        self.lbl1 = QLabel('   ')
        self.apartnum = QLabel('رقم الوحدة')
        self.apartnumC = QComboBox()
        self.apartnumC.addItems(['','1','2','3'])
        self.time = QLabel('مدة القسط')
        self.timeC = QComboBox()
        self.timeC.addItems(['6','12','18','24','30','36'])
        self.price = QLabel('طريقة الدفع')
        self.priceC = QComboBox()
        self.priceC.addItem('كاش')
        self.priceC.addItem('قسط')
        self.area = QLabel('')
        self.lbl_area = QLabel('متر مربع')
        self.meterprice = QLabel('')
        self.lbl_meterprice = QLabel('جنية')
        self.totalprice = QLabel('')
        self.lbl_totalprice = QLabel('جنية')
        self.lbl_adv = QLabel('المقدم')
        self.adv = QLineEdit(self)
        self.percent = QLineEdit(self)
        self.percent.setFixedWidth(45)
        self.lbl_percent = QLabel('%')
        self.lbl_quart = QLabel('قيمة القسط ربع السنوي')
        self.quart = QLineEdit(self)
        self.metersys = QLabel('')
        self.lbl_metersys = QLabel('جنية')
        self.totalsys = QLabel('')
        self.lbl_totalsys = QLabel('جنية')
        self.lblsys = QLabel('أســعار التقسيــــط')

        self.num_area = {1:'133',2:'108',3:'118'}
        self.num_pric = {1:'4200',2:'4050',3:'3950'}
        self.time_pric = {6:1.02,12:1.06,18:1.09,24:1.12,30:1.16,36:1.2}


        self.init_ui()

    def init_ui(self):
        v_layout = QVBoxLayout()
        h_layout1 = QHBoxLayout()
        h_layout2 = QHBoxLayout()
        h_layout3 = QHBoxLayout()
        h_layout4 = QHBoxLayout()

        h_layout1.addWidget(self.time)
        h_layout1.addWidget(self.timeC)
        h_layout1.addWidget(self.price)
        h_layout1.addWidget(self.priceC)
        h_layout1.addWidget(self.apartnum)
        h_layout1.addWidget(self.apartnumC)

        h_layout2.addWidget(self.lbl_totalprice)
        h_layout2.addWidget(self.totalprice)
        h_layout2.addWidget(self.lbl_meterprice)
        h_layout2.addWidget(self.meterprice)
        h_layout2.addWidget(self.lbl_area)
        h_layout2.addWidget(self.area)

        h_layout3.addWidget(self.quart)
        h_layout3.addWidget(self.lbl_quart)
        h_layout3.addWidget(self.lbl1)
        h_layout3.addWidget(self.lbl_percent)
        h_layout3.addWidget(self.percent)
        h_layout3.addWidget(self.adv)
        h_layout3.addWidget(self.lbl_adv)

        h_layout4.addWidget(self.lbl_totalsys)
        h_layout4.addWidget(self.totalsys)
        h_layout4.addWidget(self.lbl_metersys)
        h_layout4.addWidget(self.metersys)
        h_layout4.addWidget(self.lblsys)

        v_layout.addLayout(h_layout1)
        v_layout.addWidget(self.lbl)
        v_layout.addLayout(h_layout2)
        v_layout.addWidget(self.lbl)
        v_layout.addLayout(h_layout3)
        v_layout.addWidget(self.lbl)
        v_layout.addLayout(h_layout4)
        v_layout.addStretch()

        self.priceC.currentTextChanged.connect(self.all_func)
        self.apartnumC.currentTextChanged.connect(self.all_func)
        self.apartnumC.currentTextChanged.connect(self.percent_func)
        self.adv.textChanged.connect(self.percent_func)
        self.timeC.currentTextChanged.connect(self.percent_func)
        self.percent.textChanged.connect(self.color_adv)
        self.adv.textChanged.connect(self.sys_func)
        self.timeC.currentTextChanged.connect(self.sys_func)
        self.apartnumC.currentTextChanged.connect(self.sys_func)

        self.setLayout(v_layout)



    def all_func(self):
        try:
            if self.priceC.currentText() == 'كاش':
                if self.apartnumC.currentText() != '':
                    self.timeC.setCurrentText('')
                    self.timeC.setDisabled(True)
                    self.time.setDisabled(True)
                    self.quart.setDisabled(True)
                    self.lbl_quart.setDisabled(True)
                    self.percent.setDisabled(True)
                    self.lbl_percent.setDisabled(True)
                    self.adv.setDisabled(True)
                    self.lbl_adv.setDisabled(True)
                    self.metersys.setDisabled(True)
                    self.lbl_metersys.setDisabled(True)
                    self.totalsys.setDisabled(True)
                    self.lbl_totalsys.setDisabled(True)
                    self.lblsys.setDisabled(True)

                    self.area.setText(self.num_area[int(self.apartnumC.currentText())])
                    self.meterprice.setText(self.num_pric[int(self.apartnumC.currentText())])
                    self.totalprice.setText(str(int(self.meterprice.text()) * int(self.area.text())))
                else:
                    self.area.setText('')
                    self.meterprice.setText('')
                    self.totalprice.setText('')
            elif self.priceC.currentText() == 'قسط':
                if self.apartnumC.currentText() != '':
                    self.timeC.setDisabled(False)
                    self.time.setDisabled(False)
                    self.quart.setDisabled(False)
                    self.lbl_quart.setDisabled(False)
                    self.percent.setDisabled(False)
                    self.lbl_percent.setDisabled(False)
                    self.adv.setDisabled(False)
                    self.lbl_adv.setDisabled(False)
                    self.metersys.setDisabled(False)
                    self.lbl_metersys.setDisabled(False)
                    self.totalsys.setDisabled(False)
                    self.lbl_totalsys.setDisabled(False)
                    self.lblsys.setDisabled(False)
                    self.area.setText(self.num_area[int(self.apartnumC.currentText())])
                    self.meterprice.setText(self.num_pric[int(self.apartnumC.currentText())])
                    self.totalprice.setText(str(int(self.meterprice.text()) * int(self.area.text())))

        except:
            pass

    def percent_func(self):
        try:
            if self.priceC.currentText() == 'قسط':
                if self.adv.text() != '':
                    self.percent.setText(str(round((100 * ((int(self.adv.text()) / int(self.totalprice.text())))), 2)))
                    self.quart.setText(str(round(int((int(self.totalprice.text()) - int(self.adv.text())) / (int(self.timeC.currentText()) / 3)),1)))
        except:
            pass

    def color_adv(self):
        try:
            if float(self.percent.text()) < 30 or float(self.percent.text()) > 100:
                self.adv.setStyleSheet("color:red")
            else:
                self.adv.setStyleSheet("color:blue")
        except:
            pass

    def sys_func(self):
        try:
            if self.adv.text() != '':
                still = int(self.totalprice.text()) - int(self.adv.text())
                modistill = round(still * float(self.time_pric[int(self.timeC.currentText())]), 0) + int(
                    self.adv.text())
                self.totalsys.setText(str(modistill))
                self.metersys.setText(str(round(modistill / int(self.area.text()), 0)))
            else:
                pass
        except:
            pass

class window(QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.formWidget = Comp()
        self.setCentralWidget(self.formWidget)
        self.setWindowTitle('Pricing')

        self.init_ui()

    def init_ui(self):

        self.show()

app = QApplication(sys.argv)
win = window()
sys.exit(app.exec_())