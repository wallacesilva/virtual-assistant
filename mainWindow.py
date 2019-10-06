from audioManager import AudioRecorder
from dialog import Dialog

from PySide2.QtWidgets import QWidget, QHBoxLayout

class MainWindow(QWidget):
    def __init__(self, audioRecorder, dialog):
        super(MainWindow, self).__init__()

        # self.setStyleSheet("background-color: white;")

        self.audioRecorder = audioRecorder
        self.dialog = dialog

        self.mainLayout = QHBoxLayout()

        self.gadgetLayout = QHBoxLayout()
        self.conversationLayout = QHBoxLayout()

        self.gadgetLayout.addWidget(self.audioRecorder)
        self.conversationLayout.addWidget(self.dialog)

        self.mainLayout.addLayout(self.conversationLayout)
        self.mainLayout.addLayout(self.gadgetLayout)

        self.setLayout(self.mainLayout)
