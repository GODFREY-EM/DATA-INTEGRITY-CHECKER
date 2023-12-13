import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QDesktopWidget, QFileDialog
import hashlib

class IntegrityCheckerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.file_label = QLabel("Selected File:")
        self.file_input = QLineEdit()
        self.browse_button = QPushButton("Browse")
        self.browse_button.clicked.connect(self.browse_file)

        self.md5_label = QLabel("MD5:")
        self.sha1_label = QLabel("SHA-1:")
        self.sha256_label = QLabel("SHA-256:")
        self.digital_signature_label = QLabel("Digital Signature:")
        self.owner_label = QLabel("Owner/Creator:")

        self.calculate_button = QPushButton("Calculate Hashes and Signature")
        self.calculate_button.clicked.connect(self.calculate_hashes_and_signature)

        layout = QVBoxLayout()
        layout.addWidget(self.file_label)
        layout.addWidget(self.file_input)
        layout.addWidget(self.browse_button)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.md5_label)
        layout.addWidget(self.sha1_label)
        layout.addWidget(self.sha256_label)
        layout.addWidget(self.digital_signature_label)
        layout.addWidget(self.owner_label)

        self.setLayout(layout)
        self.setWindowTitle("Data Integrity Checker")

        # Set minimum window size
        self.setMinimumSize(500, 400)

        # Center the window on the screen
        self.center()

    def browse_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.txt);;Python Files (*.py)", options=options)
        if file_path:
            self.file_input.setText(file_path)

    def calculate_hashes_and_signature(self):
        file_path = self.file_input.text()
        if not file_path:
            return  # Do nothing if the file path is empty

        md5_hash = self.calculate_hash(file_path, "md5")
        sha1_hash = self.calculate_hash(file_path, "sha1")
        sha256_hash = self.calculate_hash(file_path, "sha256")
        digital_signature = self.generate_digital_signature(file_path)
        owner_info = self.extract_owner_info(file_path)

        self.md5_label.setText(f"MD5: {md5_hash}")
        self.sha1_label.setText(f"SHA-1: {sha1_hash}")
        self.sha256_label.setText(f"SHA-256: {sha256_hash}")
        self.digital_signature_label.setText(f"Digital Signature: {digital_signature}")
        self.owner_label.setText(f"Owner/Creator: {owner_info}")

    def calculate_hash(self, file_path, algorithm):
        hasher = hashlib.new(algorithm)
        with open(file_path, "rb") as file:
            while chunk := file.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()

    def generate_digital_signature(self, file_path):
        # For simplicity, this example uses the SHA-256 hash as the digital signature.
        return self.calculate_hash(file_path, "sha256")

    def extract_owner_info(self, file_path):
        try:
            result = subprocess.check_output(["exiftool", "-Creator", "-Software", file_path])
            return result.decode("utf-8").strip()
        except subprocess.CalledProcessError:
            return "Owner/Creator information not available"

    def center(self):
        # Center the window on the screen
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = IntegrityCheckerApp()
    window.show()
    sys.exit(app.exec_())
