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
from utils.AES import encrypt, Mode, fit_string
import shutil


class EnkripsiPage(QWidget):
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
        title = QLabel("<span style='color: rgba(88, 160, 226, 1);'>Enkripsi</span>"
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

        # Tombol Enkripsi
        encrypt_button = QPushButton("Enkripsi File")
        encrypt_button.setFont(QFont("Arial", 14))
        encrypt_button.setStyleSheet("""
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
        encrypt_button.clicked.connect(self.run_process)
        container_layout.addWidget(encrypt_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Hasil Enkripsi dan Tombol Download
        self.result_layout = QHBoxLayout()
        self.hasil_txt = QLabel("Hasil Enkripsi.txt")
        self.hasil_txt.setFont(QFont("Arial", 14))
        self.hasil_txt.setStyleSheet("color: black;")

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
        self.result_layout.addWidget(self.hasil_txt, alignment=Qt.AlignmentFlag.AlignLeft)
        self.result_layout.addStretch()
        self.result_layout.addWidget(self.download_button, alignment=Qt.AlignmentFlag.AlignRight)
        container_layout.addLayout(self.result_layout)

        self.result_layout2= QHBoxLayout()
        self.hasil_metadata = QLabel("Hasil Enkripsi metadata")
        self.hasil_metadata.setFont(QFont("Arial", 14))
        self.hasil_metadata.setStyleSheet("color: black;")

        self.download_button2 = QPushButton("Download File")
        self.download_button2.setFont(QFont("Arial", 12))
        self.download_button2.setStyleSheet("""
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
        self.result_layout2.addWidget(self.hasil_metadata, alignment=Qt.AlignmentFlag.AlignLeft)
        self.result_layout2.addStretch()
        self.result_layout2.addWidget(self.download_button2, alignment=Qt.AlignmentFlag.AlignRight)
        container_layout.addLayout(self.result_layout2)

        # Tambahkan container ke main layout
        main_layout.addWidget(container, alignment=Qt.AlignmentFlag.AlignCenter)

    class Mode(Enum):
        ECB = 'ECB'
        CTR = 'CTR'

    def get_key_from_file(self, file_path, key_length):
        try:
            with open(file_path, 'rb') as f:
                file_content = f.read()
            file_size = len(file_content)
            if file_size < key_length:
                print("File size is too small to extract the key.")
                return None

            # Ambil karakter tengah
            mid_point = file_size // 2
            start_index = max(0, mid_point - (key_length // 2))
            key = file_content[start_index:start_index + key_length]

            # Jika key panjangnya kurang dari yang diminta, pad dengan nol
            if len(key) < key_length:
                key = key.ljust(key_length, b'\0')
            
            return key
        except Exception as e:
            print(f"Error extracting key from file: {e}")
            return None
        
    def browse_input_file(self):
        # Filter untuk membatasi jenis file yang diperbolehkan
        file, _ = QFileDialog.getOpenFileName(
            self,
            "Select Input File",
            "",
            "Supported Files (*.docx *.pdf *.xls *.xlsx)"  # Filter file
        )
        if file:
            # Validasi ekstensi file
            valid_extensions = {'.docx', '.pdf', '.xls', '.xlsx'}
            if os.path.splitext(file)[1].lower() in valid_extensions:
                # Mengubah placeholder menjadi nama file
                self.file_input.setText(os.path.basename(file))
                self.input_file_path = file
            else:
                QMessageBox.warning(
                    self,
                    "Invalid File",
                    "Please select a valid file with extensions: .docx, .pdf, .xls, or .xlsx."
                )



    def run_process(self):
        input_file = self.input_file_path
        if not input_file or not os.path.isfile(input_file):
            print("Please provide a valid input file.")
            return

        # Ambil key dari file (karakter tengah)
        key = self.get_key_from_file(input_file, 16)  # Ambil 32 byte untuk AES-256
        if key is None:
            print("Failed to extract a valid key from the file.")
            return

        iv = None

        start_time = time.time()  # Start timing

        
        encrypted_file, metadata_file = self.encrypt_file(input_file, key, iv)
        print(f"Encryption completed. Encrypted file: {encrypted_file}, Metadata: {metadata_file}")
        processing_time = time.time() - start_time  # End timing
        # self.time_label.setText(f"Processing Time: {processing_time:.2f} seconds")
        
        # Update the QLabel with the result filenames
        self.hasil_txt.setText(f"Hasil Enkripsi: {os.path.basename(encrypted_file)}")
        self.hasil_metadata.setText(f"Hasil Enkripsi metadata: {os.path.basename(metadata_file)}")

        # Enable the download buttons
        self.download_button.clicked.connect(lambda: self.download_file(encrypted_file))
        self.download_button2.clicked.connect(lambda: self.download_file(metadata_file))

        # Show a message box to notify success
        self.show_encryption_success_popup()
    
    def show_encryption_success_popup(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Enkripsi Selesai")
        msg.setText("Enkripsi berhasil! File telah disimpan.")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)

        # Set stylesheet untuk mengatur warna teks
        msg.setStyleSheet("QLabel { color: black; }")

        msg.exec()

    def download_file(self, file_path):
        if os.path.exists(file_path):
            # Tambahkan ekstensi .txt hanya jika file bukan metadata
            if not file_path.endswith(".txt") and not file_path.endswith(".meta"):
                file_path += ".txt"

            # Open save file dialog to let the user choose where to save the file
            save_path, _ = QFileDialog.getSaveFileName(
                self, "Simpan File", file_path, "All Files (*);;Text Files (*.txt);;Metadata Files (*.meta)"
            )

            if save_path:
                # Jangan tambahkan .txt jika file metadata
                if file_path.endswith(".meta") and not save_path.endswith(".meta"):
                    save_path += ".meta"
                elif file_path.endswith(".txt") and not save_path.endswith(".txt"):
                    save_path += ".txt"

                # Copy the file to the chosen location
                try:
                    shutil.copy(file_path, save_path)
                    print(f"File telah disalin ke: {save_path}")
                except Exception as e:
                    print(f"Error saat menyalin file: {e}")


    

    # def download_file(self, file_path):
    #     if os.path.exists(file_path):
    #         # Tambahkan ekstensi .txt jika belum ada
    #         if not file_path.endswith(".txt"):
    #             file_path += ".txt"

    #         # Open save file dialog to let the user choose where to save the file
    #         save_path, _ = QFileDialog.getSaveFileName(
    #             self, "Simpan File", file_path, "Text Files (*.txt);;All Files (*)"
    #         )

    #         if save_path:
    #             # Pastikan file yang disimpan tetap memiliki ekstensi .txt
    #             if not save_path.endswith(".txt"):
    #                 save_path += ".txt"

    #             # Copy the file to the chosen location
    #             try:
    #                 shutil.copy(file_path, save_path)
    #                 print(f"File telah disalin ke: {save_path}")
    #             except Exception as e:
    #                 print(f"Error saat menyalin file: {e}")

    



    def encrypt_file(self, input_file, key, iv):
        # Generate unique ID for filenames
        unique_id = str(uuid.uuid4())

        # Define output directories
        txt_folder = os.path.join("results", "enkripsi", "txt")
        metadata_folder = os.path.join("results", "enkripsi", "metadata")
        os.makedirs(txt_folder, exist_ok=True)
        os.makedirs(metadata_folder, exist_ok=True)

        # Define output file paths
        encrypted_file = os.path.join(txt_folder, f"{unique_id}.txt")
        metadata_file = os.path.join(metadata_folder, f"{unique_id}.meta")

        # Get original extension and save metadata
        original_ext = os.path.splitext(input_file)[1]
        metadata = {"originalExt": original_ext, "key": key.hex()}  # Save the key as hex string}
        with open(metadata_file, 'w') as meta_f:
            json.dump(metadata, meta_f)

        # Encrypt the file
        with open(input_file, 'rb') as f:
            message = f.read()
        encrypted_data = encrypt(message, key, Mode.ECB, iv, 11)  # Replace with your encryption logic
        with open(encrypted_file, 'wb') as f:
            f.write(encrypted_data)

        return encrypted_file, metadata_file




    def show_main_page(self):
        self.stacked_widget.setCurrentIndex(1)

    def show_about_page(self):
        self.stacked_widget.setCurrentIndex(2)
