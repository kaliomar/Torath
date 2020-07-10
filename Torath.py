import sys

from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,QLabel,QComboBox,QVBoxLayout,QHBoxLayout,QLineEdit

class Comp(QWidget):
    def __init__(self):
        super(Comp, self).__init__()
        self.lbl = QLabel('')
        self.lbl1 = QLabel('   ')
        self.apartnum = QLabel('رقم الوحدة')
        self.apartnumC = QComboBox()
        self.apartnumC.addItem('1')
        self.apartnumC.addItem('2')
        self.apartnumC.addItem('3')
        self.time = QLabel('مدة القسط')
        self.timeC = QComboBox()
        self.timeC.addItem('6')
        self.timeC.addItem('12')
        self.timeC.addItem('18')
        self.timeC.addItem('24')
        self.timeC.addItem('30')
        self.timeC.addItem('36')
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
        self.percent = QLabel('55')
        self.lbl_percent = QLabel('%')
        self.lbl_quart = QLabel('قيمة القسط ربع السنوي')
        self.quart = QLineEdit(self)


        self.init_ui()

    def init_ui(self):
        v_layout = QVBoxLayout()
        h_layout1 = QHBoxLayout()
        h_layout2 = QHBoxLayout()
        h_layout3 = QHBoxLayout()


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


        v_layout.addLayout(h_layout1)
        v_layout.addWidget(self.lbl)
        v_layout.addLayout(h_layout2)
        v_layout.addWidget(self.lbl)
        v_layout.addLayout(h_layout3)
        v_layout.addStretch()

        self.setLayout(v_layout)
        self.resize(600,400)
        self.show()



class window(QMainWindow):
    def __init__(self):
        super(window, self).__init__()

        self.init_ui()

    def init_ui(self):
        pass

        self.show()

app = QApplication(sys.argv)
win = Comp()
sys.exit(app.exec_())