from PyQt5 import QtWidgets as qt, QtCore as qc, QtGui as qg
from sys import argv, exit
import api, ML_backend


class MainWindow(qt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.widget = qt.QWidget()
        self.widget .setObjectName('mainwidget')
        self.hlayout = qt.QVBoxLayout()
        self.linedit = api.linedit(self.check_url)
        self.pushbutton = qt.QPushButton('Check this url')
        self.pushbutton.setFixedWidth(400)
        self.pushbutton.clicked.connect(self.check_url)
        self.linedit.text()
        self.linedit.setFocus()
        self.linedit.setEnabled(True)
        self.linedit.setFixedWidth(700)
        font = qg.QFont()
        font.setPixelSize(16)
        font.setFamily('Open sans')
        self.linedit.setFont(font)
        self.prompt = qt.QLabel('Enter your Url here and press Enter.')
        self.prompt.setFont(font)
        self.loading_label = qt.QLabel('Loading..')
        self.loading_label.hide()
        self.label = qt.QLabel()
        pic = qg.QPixmap('../assets/phishing-detection.png')
        self.label.setPixmap(pic)
        self.label.setObjectName('image')
        self.table = qt.QTableWidget()
        self.table.hide()
        self.hlayout.addWidget(self.label, 1, qc.Qt.AlignCenter | qc.Qt.AlignTop)
        self.hlayout.addWidget(self.prompt, 0, qc.Qt.AlignCenter)
        self.hlayout.addWidget(self.linedit, 0, qc.Qt.AlignCenter | qc.Qt.AlignTop)
        self.hlayout.addWidget(self.pushbutton, 1, qc.Qt.AlignTop | qc.Qt.AlignCenter)
        self.hlayout.addWidget(self.loading_label, 1, qc.Qt.AlignCenter | qc.Qt.AlignTop)
        self.hlayout.addWidget(self.table, 10)
        self.widget.setLayout(self.hlayout)
        self.setCentralWidget(self.widget)
        self.setWindowTitle("Phishing Detector")
        self.setGeometry(0,0,1300, 720)
        self.setStyleSheet(
            """
                background-color: #212121;
                color: white;
                QLabel#image{
                    border-raidus: 10%;
                    border: none;
                }
            """
        )
        self.show()

    def check_url(self):
        url = self.linedit.text()
        if url == "":
            self.linedit.setPlaceholderText('Please Enter a URL.')
        else:
            self.loading_label.show()
            value = ML_backend.callabale_info(url, [])
            new = value[0][0]
            feature_names = value[2]
            self.table.setColumnCount(feature_names.__len__())              
            self.table.setRowCount(1)
            self.table.setHorizontalHeaderLabels(feature_names)
            self.messagedialog = qt.QMessageBox()
            for i in range(0, feature_names.__len__()):
                tablewidgetitem = qt.QTableWidgetItem(str(new[i]))
                self.table.setItem(0, i, tablewidgetitem)
            self.loading_label.hide()
            if "https" not in url:
                self.messagedialog.setText("Given url is not valid since it does not contain ssl certification or does not include 'https'.")
                self.messagedialog.show()
                return
            self.messagedialog.setText(value[1])
            self.table.show()
            self.messagedialog.show()

def main():
    app = qt.QApplication(argv)
    ex = MainWindow()
    exit(app.exec_())

if __name__ == "__main__":
    main()