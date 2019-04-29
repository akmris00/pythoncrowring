import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QUrl, QThread
import datetime
import re
from lib.You_viewer_layout import Ui_MainWindow
from lib.AuthDialog import AuthDialog
import pytube
from PyQt5.QtMultimedia import QSound
from lib.IntroWalker import IntroWalker

#form_class = uic.loadUiType('C:/Atom/Crowring/section6/ui/you_viewer_v1.0.ui')[0]

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        #초기화
        self.setupUi(self)
        #초기 잠금
        self.initAuthLock()
        #시그널 초기화
        self.initSignal()

        #로그인관련 변수 선언
        self.user_id = None
        self.user_pw = None
        #재생 여부
        self.is_play = False
        #youtube 관련 작업
        self.youtb = None
        self.youtb_fsize = 0

        #배경음악 Thread 작업 선언
        self.initIntroThread()
        #QSound.play('C:/Users/analysis/Downloads/section6/resource/intro.wav')


    #기본 UI 비활성화 세팅
    def initAuthLock(self):
        self.previewButten.setEnabled(False)
        self.fileNavButton.setEnabled(False)
        self.streamCombobox.setEnabled(False)
        self.startButton.setEnabled(False)
        self.calendarWidget.setEnabled(False)
        self.urlTextEdit.setEnabled(False)
        self.pathTextEdit.setEnabled(False)
        self.showStatusMsg('인증안됨')

    #기본 UI 활성화
    def initAuthActive(self):
        self.previewButten.setEnabled(True)
        self.fileNavButton.setEnabled(True)
        self.streamCombobox.setEnabled(True)
        self.calendarWidget.setEnabled(True)
        self.urlTextEdit.setEnabled(True)
        self.pathTextEdit.setEnabled(True)
        self.showStatusMsg('인증완료')

    def showStatusMsg(self, msg):
        self.statusbar.showMessage(msg)

    def initSignal(self):
        self.loginButton.clicked.connect(self.authCheck)
        self.previewButten.clicked.connect(self.load_url)
        self.exitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.webEngineView.loadProgress.connect(self.showProgressBrowserLoding)
        self.fileNavButton.clicked.connect(self.selectDownPath)
        self.calendarWidget.clicked.connect(self.append_date)
        self.startButton.clicked.connect(self.downloadYoutb)

    #인트로 쓰레드 초기화 및 활성화
    def initIntroThread(self):
        #walker 선언
        self.introObj = IntroWalker()
        #Qthread 선언
        self.introThread = QThread()
        #walker를 쓰레드로 전환
        self.introObj.moveToThread(self.introThread)
        #시그널 연결
        self.introObj.startMsg.connect(self.showIntroInfo)
        #쓰레드 시작 메소드 연결
        self.introThread.started.connect(self.introObj.playBgm)
        #쓰레드 스타트
        self.introThread.start()

    #인트로 쓰레드 signal 실행
    def showIntroInfo(self, userName, fileName):
        self.plainTextEdit.appendPlainText('Program started by : ' + userName)
        self.plainTextEdit.appendPlainText('Playing intro information is : ' + fileName)



    @pyqtSlot()
    def authCheck(self):
        dlg = AuthDialog()
        dlg.exec_()
        self.user_id = dlg.user_id
        self.user_pw = dlg.user_pw

        # 이부분에서 DB와 정보 확인해서 인증

        #print("id : %s password: %s" %(self.user_id, self.user_pw))
        if True:
            self.initAuthActive()
            self.loginButton.setText("인증완료")
            self.loginButton.setEnabled(False)
            self.urlTextEdit.setFocus(True)
            self.append_log_msg("login Success")

        else:
            QMessageBox.about(self,"인증오류","ID 또는 PW 인증 오류")


    def load_url(self):
        url = self.urlTextEdit.text().strip()
        v = re.compile('^https://www.youtube.com/?')
        if self.is_play:
            self.append_log_msg('Stop Click')
            self.webEngineView.load(QUrl('about:blank'))
            self.previewButten.setText("재생")
            self.is_play = False
            self.urlTextEdit.clear()
            self.urlTextEdit.setFocus(True)
            self.startButton.setEnabled(False)
            self.streamCombobox.clear()
            self.progressBar_2.setValue(0)
            self.showStatusMsg("인증완료")
        else:
            if v.match(url) is not None:
                self.append_log_msg('Play Click')
                self.webEngineView.load(QUrl(url))
                self.showStatusMsg(url + "재생 중")
                self.previewButten.setText("중지")
                self.is_play = True
                self.startButton.setEnabled(True)
                self.initialYouWork(url)

            else:
                QMessageBox.about(self,"URL 오류", "URL 오류")
                self.urlTextEdit.clear()
                self.urlTextEdit.setFocus(True)

    def initialYouWork(self,url):
        video_list = pytube.YouTube(url)
        #로딩바 계산
        video_list.register_on_progress_callback(self.showProgressDownLoding)
        self.youtb = video_list.streams.all()
        self.streamCombobox.clear()
        for q in self.youtb:
            tmp_list, str_list = [],[]
            tmp_list.append(str(q.mime_type or ''))
            tmp_list.append(str(q.res or ''))
            tmp_list.append(str(q.fps or ''))
            tmp_list.append(str(q.abr or ''))

            str_list = [x for x in tmp_list if x != '']

            self.streamCombobox.addItem(','.join(str_list))


    #로그 남기기
    def append_log_msg(self,act):
        now = datetime.datetime.now()
        nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
        app_msg = self.user_id + ' : ' + act + ' - (' + nowDatetime + ')'
        self.plainTextEdit.appendPlainText(app_msg) #insert plaintext

        #활동 로그 저장
        with open('c:/Atom/Crowring/section6/log/log.txt', 'a') as f:
            f.write(app_msg+ '\n')

    @pyqtSlot(int)
    def showProgressBrowserLoding(self, v):
        self.progressBar.setValue(v)

    @pyqtSlot()
    def selectDownPath(self):
        #파일 선택
        #fname = QFileDialog.getOpenFileName(self)
        #self.pathTextEdit.setText(fname[0])

        #경로 선택
        fpath = QFileDialog.getExistingDirectory(self,'Select Directory')
        self.pathTextEdit.setText(fpath)

    def append_date(self):
        cur_date = self.calendarWidget.selectedDate()
        #print(self.calendarWidget.selectedDate().toString())
        #print(cur_date)
        self.append_log_msg('Calender click')


    def downloadYoutb(self):
        down_dir = self.pathTextEdit.text().strip()
        if down_dir is None or down_dir == '' or not down_dir:
            QMessageBox.about(self,'경로 선택', '다운 경로 선택')
            return None

        self.youtb_fsize = self.youtb[self.streamCombobox.currentIndex()].filesize
        self.youtb[self.streamCombobox.currentIndex()].download(down_dir)
        self.append_log_msg('Download Click')

    def showProgressDownLoding(self, stream, chunk, finle_handle, bytes_remaining):
        self.progressBar_2.setValue(int(((self.youtb_fsize - bytes_remaining) / self.youtb_fsize)*100))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    you_viewer_main = Main()
    you_viewer_main.show()
    app.exec()
