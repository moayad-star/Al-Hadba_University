# Al-Hadba University Application

This application is designed to provide students of Al-Hadba University with easy access to their information, exam results, and login management.

## Features

* **Login Management**: Securely stores login credentials for easy access.
* **User Information Display**: Displays student information in a structured table.
* **Exam Results**: Provides access to mid-term and final-term exam results.
* **Logout Functionality**: Safely removes stored login credentials.
* **Error Handling**: Robust error handling for network issues and invalid login attempts.
* **Bidi Text Rendering**: Supports right-to-left languages using `awesometkinter.bidirender`.

* **`assets/images`**: Contains image files used in the application.
* **`data/config.json`**: Stores user login credentials.
* **`requirements.txt`**: Lists the Python packages required to run the application.
* **`src/Al-Hadba_University_app.py`**: Contains the main application code.

## Installation

1.  **Install dependencies:**

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

* `requests`
* `mechanicalsoup`
* `tkinter`
* `awesometkinter`

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

Read more about [LICENSE](LICENSE)
