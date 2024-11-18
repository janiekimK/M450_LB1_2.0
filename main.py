import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from sdbms import DBHelper, AddStudent, Window

def main():
    # Initialize the application
    app = QApplication(sys.argv)

    # Initialize the database helper (optional to ensure the DB is ready)
    db = DBHelper()
    print("Database initialized and tables are ready.")

    # Show the main application window
    main_window = Window()
    main_window.show()

    # Start the application's event loop
    try:
        sys.exit(app.exec_())
    except Exception as e:
        print(f"Application exited with an error: {e}")

if __name__ == "__main__":
    main()
