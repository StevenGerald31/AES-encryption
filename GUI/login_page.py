from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QFrame, QPushButton, QSizePolicy, QLineEdit
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt


class loginPage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget

        # Deklarasi akun
        self.valid_username = "admin"
        self.valid_password = "password123"

        self.init_ui()

    def init_ui(self):
        # Layout utama
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(20)

        # Header SecureHealth (absolutely positioned)
        header_label = QLabel(self)
        header_label.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        header_label.setText("<span style='color: rgba(88, 160, 226, 1);'>Secure</span>"
                             "<span style='color: rgba(0, 0, 0, 1);'>Health</span>")
        header_label.setStyleSheet("border: none;")
        header_label.setGeometry(20, 10, 300, 50)

        # Box container
        container = QFrame(self)
        container.setFixedSize(800, 500)
        container.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 15px;          
            }
        """)
        container_layout = QHBoxLayout(container)
        container_layout.setContentsMargins(20, 20, 20, 20)

        # Logo
        logo_label = QLabel()
        pixmap = QPixmap("./Assets/Picture1.png")  # Replace with your logo path
        logo_label.setPixmap(pixmap)
        logo_label.setScaledContents(True)
        logo_label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Konten dalam box
        right_layout = QVBoxLayout()
        right_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        right_layout.setSpacing(15)

        # Title
        title = QLabel("SecureHealth")
        title.setFont(QFont("Arial", 36, QFont.Weight.Bold))
        title.setStyleSheet("border: none;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setText("<span style='color: rgba(88, 160, 226, 1);'>Secure</span><span style='color: rgba(0, 0, 0, 1);'>Health</span>")

        # Subtitle
        subtitle = QLabel("Jaga Privasi Medis, Jaga Kesehatan Anda")
        subtitle.setFont(QFont("Arial", 14))
        subtitle.setStyleSheet("color: #666666;")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Username input
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        self.username_input.setFont(QFont("Arial", 12))
        self.username_input.setStyleSheet(
            "border: 1px solid #B0B0B0; border-radius: 5px; padding: 8px; color:black;"
        )

        # Password input
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setFont(QFont("Arial", 12))
        self.password_input.setStyleSheet(
            "border: 1px solid #B0B0B0; border-radius: 5px; padding: 8px; color:black;"
        )

        # Tombol
        login_button = QPushButton("Login")
        login_button.setFont(QFont("Arial", 14))
        login_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(88, 160, 226, 1);
                color: white;
                border-radius: 8px;
                padding: 10px 20px;
            }
        """)
        # login_button.clicked.connect(self.go_to_fitur_page)
        # Ubah koneksi tombol login
        login_button.clicked.connect(self.login)

        # Layout tombol
        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        button_layout.addWidget(login_button)

        # Tambahkan widgets ke right layout
        right_layout.addWidget(title)
        right_layout.addWidget(subtitle)
        right_layout.addWidget(self.username_input)
        right_layout.addWidget(self.password_input)
        right_layout.addLayout(button_layout)

        # Tambahkan elemen ke container layout
        container_layout.addWidget(logo_label)
        container_layout.addLayout(right_layout)

        # Tambahkan container ke main layout
        main_layout.addWidget(container, alignment=Qt.AlignmentFlag.AlignCenter)

        # Sesuaikan tinggi gambar dengan container
        container_layout.setStretch(0, 1)
        container_layout.setStretch(1, 2)

    # def go_to_about_page(self):
    #     self.stacked_widget.setCurrentIndex(1)

    def go_to_fitur_page(self):
        self.stacked_widget.setCurrentIndex(1)

        

        # Tambahkan fungsi login
    def login(self):
        if self.username_input.text() == self.valid_username and self.password_input.text() == self.valid_password:
            self.go_to_fitur_page()
        else:
            self.username_input.clear()
            self.password_input.clear()
            self.username_input.setPlaceholderText("Invalid username or password")
            self.password_input.setPlaceholderText("Invalid username or password")

        
