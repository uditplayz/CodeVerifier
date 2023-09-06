import random
import string
import sys
from PyQt5 import QtWidgets, QtCore

class VerificationApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title
        self.setWindowTitle("Verification System")

        # Set window dimensions
        self.setFixedSize(400, 400)

        # Create widgets
        self.name_label = QtWidgets.QLabel("Name:")
        self.name_input = QtWidgets.QLineEdit()
        self.number_label = QtWidgets.QLabel("Sr. No:")
        self.number_input = QtWidgets.QLineEdit()
        self.generate_code_button = QtWidgets.QPushButton("Generate Verification Code")
        self.verify_code_button = QtWidgets.QPushButton("Verify Code")
        self.verify_label = QtWidgets.QLabel("Verification Code:")
        self.verify_input = QtWidgets.QLineEdit()
        self.verify_output = QtWidgets.QTextEdit()
        self.verify_output.setReadOnly(True)

        # Set button connections
        self.generate_code_button.clicked.connect(self.generate_code)
        self.verify_code_button.clicked.connect(self.verify_code)

        # Create layout and add widgets
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.number_label)
        layout.addWidget(self.number_input)
        layout.addWidget(self.generate_code_button)
        layout.addWidget(self.verify_label)
        layout.addWidget(self.verify_input)
        layout.addWidget(self.verify_code_button)
        layout.addWidget(self.verify_output)

        # Set main widget and layout
        main_widget = QtWidgets.QWidget()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

        # Create list to store verified codes
        self.verified_codes = []

        # Load existing codes from file
        self.load_codes()

    def generate_code(self):
        # Generate a random 4-character alphanumeric verification code
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))

        # Display code to user
        self.verify_input.setText(code)

        # Add code to list of verified codes
        self.verified_codes.append((self.name_input.text(), self.number_input.text(), code))

        # Save codes to file
        self.save_codes()

    def verify_code(self):
        # Get input code
        input_code = self.verify_input.text()

        # Check if code is in verified codes list
        match = [code for code in self.verified_codes if code[2] == input_code]

        # Display result to user
        if match:
            self.verify_output.append(f"Verified: {match[0][0]} ({match[0][1]})\n")
        else:
            self.verify_output.append("Invalid code\n")

    def load_codes(self):
        # Load existing codes from file
        try:
            with open('audit.txt', 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    self.verified_codes.append((parts[0], parts[1], parts[2]))
        except FileNotFoundError:
            pass

    def save_codes(self):
        # Save codes to file
        with open('audit.txt', 'w') as file:
            for code in self.verified_codes:
                file.write(f"{code[0]},{code[1]},{code[2]}\n")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    verification_app = VerificationApp()
    verification_app.show()
    sys.exit(app.exec_())
