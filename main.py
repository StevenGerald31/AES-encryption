import sys
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtWidgets import QApplication, QStackedWidget, QMainWindow
from GUI.main_page import MainPage
from GUI.about_page import AboutPage
from GUI.fitur_page import FiturPage
from GUI.enkripsi_page import EnkripsiPage
from GUI.dekripsi_page import DekripsiPage


class SecureHealthApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SecureHealth")
        screen = QGuiApplication.primaryScreen().availableGeometry()
        width = screen.width()
        height = screen.height()

        # Menyesuaikan ukuran jendela aplikasi
        self.resize(int(width * 0.8), int(height * 0.8))  # Menggunakan 80% dari ukuran layar

        # Central widget with stacked layout
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        # Initialize pages
        self.main_page = MainPage(self.central_widget)
        self.about_page = AboutPage(self.central_widget)
        self.fitur_page = FiturPage(self.central_widget)  # Halaman fitur
        self.enkripsi_page = EnkripsiPage(self.central_widget)
        self.dekripsi_page = DekripsiPage(self.central_widget)

        # Add pages to stacked widget
        self.central_widget.addWidget(self.main_page)  # Index 0
        self.central_widget.addWidget(self.about_page)  # Index 1
        self.central_widget.addWidget(self.fitur_page)  # Index 2
        self.central_widget.addWidget(self.enkripsi_page)
        self.central_widget.addWidget(self.dekripsi_page)

        # Show main page by default
        self.central_widget.setCurrentWidget(self.main_page)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Atur latar belakang putih untuk semua halaman
    app.setStyleSheet("QWidget { background-color: rgba(231, 231, 231, 1); }")
    window = SecureHealthApp()
    window.show()
    sys.exit(app.exec())
