import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap
from pytube import YouTube

class Downloader(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Adding the logo/image
        logo_label = QLabel(self)
        pixmap = QPixmap('logo.jpeg')  # Replace 'logo.png' with your image file
        logo_label.setPixmap(pixmap)
        layout.addWidget(logo_label)

        self.label = QLabel("Enter YouTube URL:")
        self.url_input = QLineEdit()

        self.download_button = QPushButton("Download")
        self.download_button.clicked.connect(self.download_video)

        layout.addWidget(self.label)
        layout.addWidget(self.url_input)
        layout.addWidget(self.download_button)

        self.setLayout(layout)
        self.setWindowTitle("YouTube Downloader")
        self.show()

    def download_video(self):
        url = self.url_input.text()
        try:
            yt = YouTube(url)
            video = yt.streams.get_highest_resolution()
            print(f"Downloading: {video.title}...")
            video.download()
            print("Download complete!")
        except Exception as e:
            print(f"Error: {str(e)}")

def main():
    app = QApplication(sys.argv)
    window = Downloader()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
