from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame, QSizePolicy
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt


class AboutPage(QWidget):
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


        # Tombol "Home" di kanan atas
        home_button = QPushButton("🏠")
        home_button.setFont(QFont("Arial", 14))
        home_button.setStyleSheet("background: #FFFFFF; border: none; color: black;")
        home_button.clicked.connect(self.show_main_page)

        # Tambahkan elemen header ke layout header
        header_layout.addWidget(header_label, alignment=Qt.AlignmentFlag.AlignLeft)
        header_layout.addStretch()
        header_layout.addWidget(home_button)

        # Tambahkan header ke main layout (tanpa memengaruhi elemen lain)
        main_layout.addLayout(header_layout)

        # Konten utama
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

        # Bagian teks
        text_layout = QVBoxLayout()
        text_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Judul
        title_label = QLabel("Melindungi Rekam Medis Elektronik\nMenggunakan Kriptografi")
        title_label.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("color: #3D88F7;")

        # Deskripsi
        description_label = QLabel(
            "SecureHealth menggunakan teknologi kriptografi untuk melindungi rekam medis elektronik. "
            "Dengan enkripsi, data medis aman dari akses yang tidak sah, dan hanya pihak berwenang yang dapat membukanya."
        )
        description_label.setFont(QFont("Arial", 12))
        description_label.setStyleSheet("color: #666666;")
        description_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        description_label.setWordWrap(True)

        # Tombol
        button_layout = QHBoxLayout()

        # Layout untuk tombol Enkripsi
        encrypt_layout = QVBoxLayout()
        encrypt_button = QPushButton("Enkripsi")
        encrypt_button.setFont(QFont("Arial", 12))
        encrypt_button.setStyleSheet(
            "background-color: #3D88F7; color: white; border-radius: 5px; padding: 10px 20px;"
        )
        encrypt_label = QLabel("Ubah data menjadi kode rahasia yang tidak dapat dibaca oleh pihak tidak berwenang.")
        encrypt_label.setFont(QFont("Arial", 10))
        encrypt_label.setStyleSheet("color: gray;")
        encrypt_label.setWordWrap(True)
        encrypt_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        encrypt_label.setFixedWidth(200)  # Atur lebar tetap untuk teks label
        encrypt_layout.addWidget(encrypt_button)
        encrypt_layout.addWidget(encrypt_label)
        encrypt_button.clicked.connect(self.show_enkripsi_page)

        # Layout untuk tombol Deskripsi
        decrypt_layout = QVBoxLayout()
        decription_button = QPushButton("Deskripsi")
        decription_button.setFont(QFont("Arial", 12))
        decription_button.setStyleSheet(
            "background-color: #E0E0E0; color: black; border-radius: 5px; padding: 10px 20px;"
        )
        decrypt_label = QLabel("Mengembalikan data ke bentuk aslinya menggunakan kunci rahasia.")
        decrypt_label.setFont(QFont("Arial", 10))
        decrypt_label.setStyleSheet("color: gray;")
        decrypt_label.setWordWrap(True)
        decrypt_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        decrypt_label.setFixedWidth(200)  # Atur lebar tetap untuk teks label
        decrypt_layout.addWidget(decription_button)
        decrypt_layout.addWidget(decrypt_label)
        decription_button.clicked.connect(self.show_dekripsi_page)

        # Tambahkan layout tombol ke layout utama
        button_layout.addLayout(encrypt_layout)
        button_layout.addLayout(decrypt_layout)

        # Tambahkan teks ke layout
        text_layout.addWidget(title_label)
        text_layout.addWidget(description_label)
        text_layout.addSpacing(20)
        text_layout.addLayout(button_layout)

        # Tambahkan bagian gambar dan teks ke layout utama
        right_layout.addLayout(text_layout)

        # Tambahkan header dan konten ke layout utama
        container_layout.addWidget(logo_label)
        container_layout.addLayout(right_layout)

        main_layout.addWidget(container, alignment=Qt.AlignmentFlag.AlignCenter)

        # Sesuaikan tinggi gambar dengan container
        container_layout.setStretch(0, 1)
        container_layout.setStretch(1, 2)


    def show_main_page(self):
        self.stacked_widget.setCurrentIndex(1)  # Kembali ke halaman utama
    
    def show_enkripsi_page(self):
        self.stacked_widget.setCurrentIndex(4)  # Pindah ke halaman enkripsi

    def show_dekripsi_page(self):
        self.stacked_widget.setCurrentIndex(5)  # Pindah ke halaman dekripsi
