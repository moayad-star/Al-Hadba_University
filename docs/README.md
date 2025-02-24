<img src="https://img.shields.io/badge/Language-python_3.x-crimson"> <img src="https://img.shields.io/badge/version-1.0-blue"> <img src="https://img.shields.io/badge/license-GPLv3-red"> <img src="https://img.shields.io/badge/Source-open-blue"> <img src="https://img.shields.io/badge/platform-linux-ffb703"> <img src="https://img.shields.io/badge/platform-windows-success"> <img src="https://img.shields.io/badge/platform-macOS-silver">


# Al-Hadba University of Iraq Application

### Al-Hadba University Student Companion

In the digital age, access to academic information should be seamless and readily available. This project emerged from a personal endeavor to bridge a gap for Al-Hadba University students who, like myself, sought a more convenient way to interact with their university data. Recognizing the absence of an official desktop application, and finding the mobile-centric approach somewhat limiting, I embarked on creating this student companion.

This application is a labor of independent development, crafted with the aim of providing a practical tool for fellow students. It's designed to offer a familiar desktop experience, allowing for easy access to essential information such as student profiles and exam results. Built with cross-platform compatibility in mind, it strives to serve as a reliable resource for students across Windows, Linux, and macOS environments.

It's important to note that this is not an official university-endorsed application. Rather, it's a project born out of a desire to enhance the student experience. As such, it's maintained and updated independently. While every effort has been made to ensure accuracy and reliability, users should exercise discretion and verify critical information through official university channels.

This project is open-source, inviting contributions and feedback from the community. It's a testament to the power of individual initiative and the spirit of collective improvement. By sharing this tool, I hope to contribute to a more accessible and efficient academic journey for Al-Hadba University students.

## Features

* **Login Management**: Securely stores login credentials for easy access.
* **User Information Display**: Displays student information in a structured table.
* **Exam Results**: Provides access to mid-term and final-term exam results.
* **Logout Functionality**: Safely removes stored login credentials.
* **`data/config.json`**: Stores user login credentials.
* **`requirements.txt`**: Lists the Python packages required to run the application.

## Installation

1. **Install Python**

   [Read more](https://www.python.org/)

3.  **Clone the repository:**

    ```bash
    git clone https://github.com/moayad-star/Al-Hadba_University.git
    cd Al-Hadba_University
    ```

4.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the application:**

    ```bash
    cd Al-Hadba_University/src/
    python3 Al-Hadba_University_app.py
    ```

2.  **Login:** Enter your university credentials.
3.  **Navigate:** Use the buttons on the home page to access different features.

## Dependencies

* `python 3.x`
* `requests`
* `mechanicalsoup`
* `tkinter`
* `awesometkinter`

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

<img src="https://www.gnu.org/graphics/gplv3-127x51.png">

Read more about [LICENSE](LICENSE)
