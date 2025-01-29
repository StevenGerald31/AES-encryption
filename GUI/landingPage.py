import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
)
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt


class SecureHealthApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SecureHealth")
        self.setFixedSize(800, 500)
        self.init_ui()

    def init_ui(self):
        # Main container
        main_container = QWidget()
        main_layout = QVBoxLayout(main_container)

        # Header section
        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(20, 10, 20, 10)

        # Logo
        logo_label = QLabel()
        pixmap = QPixmap("logo.png")  # Replace with the logo image path
        scaled_pixmap = pixmap.scaled(40, 40, Qt.AspectRatioMode.KeepAspectRatio)
        logo_label.setPixmap(scaled_pixmap)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        # App name in header
        app_name_label = QLabel("SecureHealth")
        app_name_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        app_name_label.setStyleSheet("color: #3D88F7;")
        app_name_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        # Add logo and app name to header layout
        header_layout.addWidget(logo_label)
        header_layout.addWidget(app_name_label)
        header_layout.addStretch()  # Push everything to the left

        # Content section (image and text)
        content_layout = QHBoxLayout()

        # Left section with image
        image_label = QLabel()
        pixmap = QPixmap("Picture1.png")  # Replace with the image path
        scaled_pixmap = pixmap.scaled(400, 400, Qt.AspectRatioMode.KeepAspectRatio)
        image_label.setPixmap(scaled_pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Right section with text and buttons
        text_layout = QVBoxLayout()
        text_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # App title
        title_label = QLabel("SecureHealth")
        title_label.setFont(QFont("Arial", 30, QFont.Weight.Bold))
        title_label.setStyleSheet("color: #3D88F7;")

        # Subtitle
        subtitle_label = QLabel("Jaga Privasi Medis, Jaga Kesehatan Anda")
        subtitle_label.setFont(QFont("Arial", 14))
        subtitle_label.setStyleSheet("color: #666666;")

        # Buttons
        button_layout = QHBoxLayout()

        get_started_button = QPushButton("Get Started")
        get_started_button.setFont(QFont("Arial", 12))
        get_started_button.setStyleSheet(
            """
            QPushButton {
                background-color: #3D88F7;
                color: white;
                border-radius: 5px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #3072C4;
            }
            """
        )

        about_app_button = QPushButton("About App")
        about_app_button.setFont(QFont("Arial", 12))
        about_app_button.setStyleSheet(
            """
            QPushButton {
                background-color: #E0E0E0;
                color: black;
                border-radius: 5px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #C0C0C0;
            }
            """
        )

        button_layout.addWidget(get_started_button)
        button_layout.addWidget(about_app_button)

        # Add widgets to text layout
        text_layout.addWidget(title_label)
        text_layout.addWidget(subtitle_label)
        text_layout.addSpacing(20)
        text_layout.addLayout(button_layout)

        # Add sections to content layout
        content_layout.addWidget(image_label)
        content_layout.addLayout(text_layout)

        # Add header and content to main layout
        main_layout.addLayout(header_layout)
        main_layout.addLayout(content_layout)

        # Set main layout
        self.setCentralWidget(main_container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SecureHealthApp()
    window.show()
    sys.exit(app.exec())
