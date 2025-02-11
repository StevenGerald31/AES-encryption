from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QFrame, QPushButton, QHBoxLayout, QLineEdit, QFileDialog, QMessageBox,
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import os
import uuid
from enum import Enum
import time
import json
from utils.AES import decrypt, Mode, fit_string
import shutil

class DekripsiPage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.init_ui()

    def init_ui(self):
        # Layout utama
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        # Header
        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(0, 0, 0, 0)

        # Logo SecureHealth
        header_label = QLabel("<span style='color: rgba(88, 160, 226, 1);'>Secure</span>"
                              "<span style='color: rgba(0, 0, 0, 1);'>Health</span>")
        header_label.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        header_label.setStyleSheet("border: none;")

        # Tombol Home dan About App
        home_button = QPushButton("🏠")
        home_button.setFont(QFont("Arial", 14))
        home_button.setStyleSheet("background: #FFFFFF; border: none; color: black;")
        home_button.clicked.connect(self.show_main_page)

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

        # Tambahkan elemen ke header
        header_layout.addWidget(header_label, alignment=Qt.AlignmentFlag.AlignLeft)
        header_layout.addStretch()
        header_layout.addWidget(home_button)
        header_layout.addWidget(about_button)
        main_layout.addLayout(header_layout)

        # Kontainer utama
        container = QFrame(self)
        container.setFixedSize(800, 500)
        container.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 15px; 
                padding: 20px;         
            }
        """)
        container_layout = QVBoxLayout(container)
        container_layout.setContentsMargins(20, 20, 20, 20)
        container_layout.setSpacing(20)

        # Judul
        title = QLabel("<span style='color: rgba(88, 160, 226, 1);'>Dekripsi</span>"
                       "<span style='color: rgba(0, 0, 0, 1);'> File</span>")
        title.setFont(QFont("Arial", 28, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        container_layout.addWidget(title)

        # Input file dan tombol pilih file
        file_layout = QHBoxLayout()
        self.file_input = QLineEdit()
        self.file_input.setPlaceholderText("File Rekam Medis Elektronik")
        self.file_input.setFont(QFont("Arial", 12))
        self.file_input.setStyleSheet("""
            QLineEdit {
                padding: 8px; 
                border: 1px solid #CCCCCC; 
                border-radius: 5px; 
                color: black;
            }
        """)

        file_button = QPushButton("Pilih File")
        file_button.setFont(QFont("Arial", 12))
        file_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(88, 160, 226, 1);
                color: white;
                border-radius: 5px;
                padding: 8px 12px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        file_button.clicked.connect(self.browse_input_file)

        file_layout.addWidget(self.file_input, stretch=3)
        file_layout.addWidget(file_button, stretch=1)
        container_layout.addLayout(file_layout)

        meta_layout = QHBoxLayout()
        self.meta_input = QLineEdit()
        self.meta_input.setPlaceholderText("File metadata")
        self.meta_input.setFont(QFont("Arial", 12))
        self.meta_input.setStyleSheet("""
            QLineEdit {
                padding: 8px; 
                border: 1px solid #CCCCCC; 
                border-radius: 5px; 
                color: black;
            }
        """)

        meta_button = QPushButton("Pilih File")
        meta_button.setFont(QFont("Arial", 12))
        meta_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(88, 160, 226, 1);
                color: white;
                border-radius: 5px;
                padding: 8px 12px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        meta_button.clicked.connect(self.browse_meta_file)
        meta_layout.addWidget(self.meta_input, stretch=3)
        meta_layout.addWidget(meta_button, stretch=1)
        container_layout.addLayout(meta_layout)

        # Tombol Enkripsi
        decrypt_button = QPushButton("Dekripsi File")
        decrypt_button.setFont(QFont("Arial", 14))
        decrypt_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(88, 160, 226, 1);
                color: white;
                border-radius: 8px;
                padding: 12px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        container_layout.addWidget(decrypt_button, alignment=Qt.AlignmentFlag.AlignCenter)
        decrypt_button.clicked.connect(self.run_process)

        # Hasil Enkripsi dan Tombol Download
        result_layout = QHBoxLayout()
        self.result_label = QLabel("Hasil Dekripsi ")
        self.result_label.setFont(QFont("Arial", 14))
        self.result_label.setStyleSheet("color: black;")

        self.download_button = QPushButton("Download File")
        self.download_button.setFont(QFont("Arial", 12))
        self.download_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(88, 160, 226, 1);
                color: white;
                border-radius: 5px;
                padding: 8px 12px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        result_layout.addWidget(self.result_label, alignment=Qt.AlignmentFlag.AlignLeft)
        result_layout.addStretch()
        result_layout.addWidget(self.download_button, alignment=Qt.AlignmentFlag.AlignRight)
        container_layout.addLayout(result_layout)

        self.download_button.clicked.connect(self.download_decrypted_file)
        self.download_button.setEnabled(False)  # Nonaktifkan tombol hingga file tersedia


        # Tambahkan container ke main layout
        main_layout.addWidget(container, alignment=Qt.AlignmentFlag.AlignCenter)

    def browse_input_file(self):
        file, _ = QFileDialog.getOpenFileName(
            self,
            "Select Input File",
            "",
            "Text Files (*.txt)"  # Filter hanya file .txt
        )
        if file:
            if os.path.splitext(file)[1].lower() == '.txt':
                self.file_input.setText(file)
            else:
                QMessageBox.warning(
                    self,
                    "Invalid File",
                    "Please select a valid .txt file."
                )

    def browse_meta_file(self):
        file, _ = QFileDialog.getOpenFileName(
            self,
            "Select Metadata File",
            "",
            "Metadata Files (*.meta)"  # Filter hanya file .meta
        )
        if file:
            if os.path.splitext(file)[1].lower() == '.meta':
                self.meta_input.setText(file)
            else:
                QMessageBox.warning(
                    self,
                    "Invalid File",
                    "Please select a valid .meta file."
                )

    
    def run_process(self):
        input_file = self.file_input.text()
        meta_file = self.meta_input.text()

        if not input_file or not os.path.isfile(input_file):
            print("Please provide a valid input file.")
            return
        
        if not meta_file or not os.path.isfile(meta_file):
            print("Please provide a valid metadata file.")
            return

        try:
            with open(meta_file, 'r') as meta_f:
                metadata = json.load(meta_f)

            key = bytes.fromhex(metadata.get("key"))
            original_ext = metadata.get("originalExt", ".txt")

            decrypt_folder = os.path.join("results", "dekripsi")
            os.makedirs(decrypt_folder, exist_ok=True)

            output_file = os.path.join(decrypt_folder, f"decrypted_{uuid.uuid4()}{original_ext}")

            with open(input_file, 'rb') as f:
                encrypted_data = f.read()

            decrypted_data = decrypt(encrypted_data, key, Mode.ECB, None, 11)

            with open(output_file, 'wb') as f:
                f.write(decrypted_data)

            self.result_label.setText(f"Hasil Dekripsi: {os.path.basename(output_file)}")
            self.download_button.setEnabled(True)
            self.decrypted_file = output_file

            processing_time = time.time() - time.time()
            self.show_success_popup(processing_time)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Terjadi kesalahan: {str(e)}")

    def show_success_popup(self, processing_time):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Dekripsi Selesai")
        msg.setText(f"Dekripsi berhasil dilakukan")
        msg.setStyleSheet("""
            QMessageBox {
                color: black;  /* Warna teks */
            }
        """)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

    def decrypt_file(self, input_file, meta_file, key, iv):
        # Read metadata for original extension
        with open(meta_file, 'r') as meta_f:
            metadata = json.load(meta_f)
        original_ext = metadata.get("originalExt", ".txt")
        key = bytes.fromhex(metadata.get("key"))  # Read the key from metadata
    
        # Define output directory
        decrypt_folder = os.path.join("results", "dekripsi")
        os.makedirs(decrypt_folder, exist_ok=True)

        # Define output file path
        output_file = os.path.join(decrypt_folder, f"decrypted_{uuid.uuid4()}{original_ext}")

        # Decrypt the file
        with open(input_file, 'rb') as f:
            encrypted_data = f.read()
        decrypted_data = decrypt(encrypted_data, key, Mode.ECB, iv, 11)  # Replace with your decryption logic
        with open(output_file, 'wb') as f:
            f.write(decrypted_data)

        return output_file
    
    

    def download_decrypted_file(self):
        if hasattr(self, "decrypted_file") and os.path.isfile(self.decrypted_file):
            # Ambil ekstensi asli dari nama file decrypted
            _, original_ext = os.path.splitext(self.decrypted_file)

            # Siapkan nama default dengan ekstensi asli
            default_filename = os.path.basename(self.decrypted_file)

            # Buka dialog penyimpanan dengan ekstensi default
            save_path, _ = QFileDialog.getSaveFileName(
                self,
                "Simpan File",
                default_filename,
                f"{original_ext.upper()} Files (*{original_ext});;All Files (*)"
            )

            if save_path:
                # Pastikan ekstensi sesuai jika belum ada
                if original_ext and not save_path.endswith(original_ext):
                    save_path += original_ext

                try:
                    shutil.copy(self.decrypted_file, save_path)
                    # Pesan sukses
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Icon.Information)
                    msg.setWindowTitle("Download Selesai")
                    msg.setText("File berhasil disimpan.")
                    msg.setStyleSheet("QMessageBox { color: black; }")
                    msg.setStandardButtons(QMessageBox.StandardButton.Ok)
                    msg.exec()
                except Exception as e:
                    print(f"Error saat menyalin file: {e}")



    def show_main_page(self):
        self.stacked_widget.setCurrentIndex(1)

    def show_about_page(self):
        self.stacked_widget.setCurrentIndex(2)
