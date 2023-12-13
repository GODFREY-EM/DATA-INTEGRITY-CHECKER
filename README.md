# DATA-INTEGRITY-CHECKER
digital signature and Contents verification 

Certainly! Here's a sample README file that you can use for your app:

---

 Data Integrity Checker

 Overview

The Data Integrity Checker is a tool designed to verify the integrity of files and provide essential information about them, including hash values, digital signatures, and details about the file's owner or creator.

 Features

- Hash Calculation: The app calculates MD5, SHA-1, and SHA-256 hash values for the selected file to ensure data integrity.

- Digital Signature: It generates a digital signature for the file, providing an additional layer of verification.

- Owner/Creator Information: The app extracts and displays information about the owner or creator of the file.

- Graphical User Interface (GUI): The app provides a user-friendly GUI for an intuitive experience.

- Command-Line Interface (CLI): For users who prefer the command line, the app offers a CLI with the same functionality.

 How to Use

 Graphical User Interface (GUI)

1. Installation:
   - Make sure you have Python installed.
   - Clone the repository and navigate to the project directory.

2. Create a Virtual Environment:
   ```bash
   python -m venv myenv
   ```

3. Activate the Virtual Environment:
   - On Linux or MacOS:
     ```bash
     source myenv/bin/activate
     ```
   - On Windows:
     ```bash
     .\myenv\Scripts\activate
     ```

4. Install Dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the GUI App:
   ```bash
   python gui_app.py
   ```

6. Browse and Calculate:
   - Click the "Browse" button to select a file.
   - Click "Calculate Hashes and Signature" to obtain hash values and digital signature.

7. View Results:
   - The GUI displays MD5, SHA-1, SHA-256 hashes, digital signature, and owner/creator information.

 Command-Line Interface (CLI)

1. Installation and Setup:
   - Follow steps 1-4 from the GUI instructions.

2. Run the CLI App:
   ```bash
   python cli_app.py
   ```

3. Enter File Path:
   - Type the path of the file when prompted and press Enter.

4. View Results:
   - The CLI displays MD5, SHA-1, SHA-256 hashes, digital signature, and owner/creator information.

 Notes

- For the GUI app, ensure you have a graphical environment to display the window.

- Some files may not contain owner/creator information, resulting in a default message.

- The CLI version is suitable for users comfortable with the command line.

---

Feel free to customize this README based on your app's specific details and requirements.
