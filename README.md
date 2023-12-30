# Entry Code Verification

Entry Code Verification is a simple desktop application written in Python that serves various verification purposes. This README provides an overview of the project, installation instructions, and usage guidelines.

## About the App

This application was initially created for verifying the entry of people to a farewell party whose names are on the guest list. It features a basic design and offers two main functionalities:

Code Generation: You can enter a name and click the "Generate" button. This action generates a 4-digit alphanumeric code associated with the name. The generated code is saved in the Audit.txt file, along with the name and a serial number.

Code Verification: After generating codes, you can open or close the app as needed. When the audit file (Audit.txt) is present in the same folder as the application, you can use the "Verification" tab to enter a code. The app will then check if the entered code is valid and display the name of the corresponding person as "Verified" or "Not Verified" if the code is invalid.

### Please note that the application's design is basic and may require improvements. Contributions and suggestions for enhancements are welcome.

## Installation

Compilation Steps for Python Script
Before running the application, you may need to compile the verification.py script on your specific operating system. Here are the compilation steps for Windows, macOS, and major Linux distributions:

Windows, MacOs, Linux:

Ensure you have Python installed on your Windows machine.
Open Command Prompt and navigate to the project directory.
Run the following command to create an executable from the Python script:
`pyinstaller --onefile verification.py`
This will create an executable file in the dist directory.

Pre-built Executable (Arch Linux)
For Arch Linux users, a pre-built executable file is provided in the repository. You can directly use this executable on your Arch Linux system. However, please note that it may or may not work on other systems, as it hasn't been tested on them.

## Usage

1. Run the compiled or pre-built executable file for your operating system.
2. Use the "Generate" tab to create 4-digit alphanumeric codes associated with names.
  - The Code and Names are stored in Audit.txt file. (make sure it's in the same folder)
3. Use the "Verification" tab to verify entry codes. If the Audit.txt file is present in the same folder, the app will display whether the entered code is verified and the name associated with it.

## Contributing

Contributions to improve the application's design and functionality are highly appreciated. If you have suggestions, bug reports, or want to contribute code, please feel free to create issues or pull requests in this repository.

### Thank you for using Entry Code Verification!
