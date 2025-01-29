from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt

class FiturPage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.init_ui()

    def init_ui(self):
        # Layout utama
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)

        
        # Header (tetap independen dari elemen lain)
        header_layout = QHBoxLayout()

        # Header SecureHealth (absolutely positioned)
        header_label = QLabel(self)
        header_label.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        header_label.setText("<span style='color: rgba(88, 160, 226, 1);'>Secure</span>"
                             "<span style='color: rgba(0, 0, 0, 1);'>Health</span>")
        header_label.setStyleSheet("border: none;")
        header_label.setGeometry(20, 10, 300, 50)  # Atur posisi (x, y, width, height)


        # Tombol "About App" di kanan atas
        about_button = QPushButton("About App")
        about_button.setFont(QFont("Arial", 14))
        about_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(88, 160, 226, 1);
                color: white;
                border-radius: 8px;
                padding: 6px 12px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        about_button.clicked.connect(self.show_about_page)

        # Tombol "Home" di kanan atas
        home_button = QPushButton("🏠")
        home_button.setFont(QFont("Arial", 14))
        home_button.setStyleSheet("background: #FFFFFF; border: none; color: black;")
        home_button.clicked.connect(self.show_main_page)

        # Tambahkan elemen header ke layout header
        header_layout.addWidget(header_label, alignment=Qt.AlignmentFlag.AlignLeft)
        header_layout.addStretch()
        header_layout.addWidget(home_button)
        header_layout.addWidget(about_button)

        # Tambahkan header ke main layout (tanpa memengaruhi elemen lain)
        main_layout.addLayout(header_layout)

        # Kontainer utama
        container = QFrame(self)
        container.setFixedSize(800, 500)
        container.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 15px;          
            }
        """)
        container_layout = QHBoxLayout(container)
        container_layout.setContentsMargins(0, 0, 0, 0)

        # Gambar
        logo_label = QLabel()
        pixmap = QPixmap("./Assets/Picture1.png")  # Replace with your logo path
        logo_label.setPixmap(pixmap)
        logo_label.setScaledContents(True)
        logo_label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Konten dalam box
        right_layout = QVBoxLayout()
        right_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        right_layout.setSpacing(20)

        # Title
        title = QLabel("SecureHealth")
        title.setFont(QFont("Arial", 36, QFont.Weight.Bold))
        title.setStyleSheet("""
            QLabel {
                border: none;
            }
        """)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setText("""
        <span style='color: rgba(88, 160, 226, 1);'>AES</span><br>
        <span style='color: rgba(88, 160, 226, 1);'>Without</span> 
        <span style='color: rgba(0, 0, 0, 1);'>Key</span>
        """)

        # Tombol
        get_started_button = QPushButton("Enkripsi")
        get_started_button.setFont(QFont("Arial", 14))
        get_started_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(88, 160, 226, 1);
                color: white;
                border-radius: 8px;
                padding: 10px 20px;
            }
        """)
        get_started_button.clicked.connect(self.show_enkripsi_page)

        about_button = QPushButton("Dekripsi")
        about_button.setFont(QFont("Arial", 14))
        about_button.setStyleSheet("""
            QPushButton {
                background-color: #E0E0E0;
                color: black;
                border-radius: 8px;
                padding: 10px 20px;
            }
        """)
        about_button.clicked.connect(self.show_dekripsi_page)

        # Layout tombol
        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        button_layout.addWidget(get_started_button)
        button_layout.addWidget(about_button)

        # Tambahkan widgets ke right layout
        right_layout.addWidget(title)
        right_layout.addLayout(button_layout)

        # Tambahkan elemen ke container layout
        container_layout.addWidget(logo_label)
        container_layout.addLayout(right_layout)

        # Tambahkan container ke main layout
        main_layout.addWidget(container, alignment=Qt.AlignmentFlag.AlignCenter)

        # Sesuaikan tinggi gambar dengan container
        container_layout.setStretch(0, 1)
        container_layout.setStretch(1, 2)


    def show_enkripsi_page(self):
        self.stacked_widget.setCurrentIndex(3)
    
    def show_dekripsi_page(self):
        self.stacked_widget.setCurrentIndex(4)

    def deskripsi_action(self):
        print("Tombol Deskripsi diklik!")

    def show_main_page(self):
        self.stacked_widget.setCurrentIndex(0)

    def show_about_page(self):
        self.stacked_widget.setCurrentIndex(1)
