import sys
import os
import subprocess
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit, QPushButton, QFileDialog, QLineEdit, QLabel, QHBoxLayout
)
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QTextCursor, QColor

class FirewallGUI(QMainWindow):
    def __init__(self, log_file="firewall.log"):
        super().__init__()
        self.log_file = log_file
        self.firewall_process = None  # To store the firewall process
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Firewall Traffic Monitor")
        self.setGeometry(100, 100, 800, 600)

        # Main layout
        layout = QVBoxLayout()

        # Search bar for filtering logs
        search_layout = QHBoxLayout()
        self.search_label = QLabel("Filter Logs:")
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Enter keyword (e.g., BLOCKED, ICMP)")
        self.search_bar.textChanged.connect(self.filter_logs)
        search_layout.addWidget(self.search_label)
        search_layout.addWidget(self.search_bar)
        layout.addLayout(search_layout)

        # Text area to display logs
        self.log_viewer = QTextEdit(self)
        self.log_viewer.setReadOnly(True)
        layout.addWidget(self.log_viewer)

        # Button to refresh logs
        self.refresh_button = QPushButton("Refresh Logs", self)
        self.refresh_button.clicked.connect(self.load_logs)
        layout.addWidget(self.refresh_button)

        # Button to select a different log file
        self.select_file_button = QPushButton("Select Log File", self)
        self.select_file_button.clicked.connect(self.select_log_file)
        layout.addWidget(self.select_file_button)

        # Button to export logs
        self.export_button = QPushButton("Export Logs", self)
        self.export_button.clicked.connect(self.export_logs)
        layout.addWidget(self.export_button)

        # Button to start the firewall
        self.start_firewall_button = QPushButton("Start Firewall", self)
        self.start_firewall_button.clicked.connect(self.start_firewall)
        layout.addWidget(self.start_firewall_button)

        # Button to stop the firewall
        self.stop_firewall_button = QPushButton("Stop Firewall", self)
        self.stop_firewall_button.clicked.connect(self.stop_firewall)
        layout.addWidget(self.stop_firewall_button)

        # Set the central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Timer to auto-refresh logs every 5 seconds
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.load_logs)
        self.timer.start(5000)  # Refresh every 5000 ms (5 seconds)

        # Load initial logs
        self.load_logs()

    def load_logs(self):
        """Load and display logs from the log file."""
        if os.path.exists(self.log_file):
            with open(self.log_file, "r") as f:
                logs = f.read()
                self.log_viewer.setText(logs)
                self.highlight_alerts()  # Highlight specific log entries
        else:
            self.log_viewer.setText(f"Log file '{self.log_file}' not found.")

    def filter_logs(self):
        """Filter logs based on the search bar input."""
        keyword = self.search_bar.text().strip()
        if os.path.exists(self.log_file):
            with open(self.log_file, "r") as f:
                logs = f.readlines()
                filtered_logs = [log for log in logs if keyword.lower() in log.lower()]
                self.log_viewer.setText("".join(filtered_logs))
                self.highlight_alerts()  # Highlight specific log entries

    def highlight_alerts(self):
        """Highlight specific log entries (e.g., threats or blocked packets)."""
        cursor = self.log_viewer.textCursor()
        cursor.movePosition(QTextCursor.Start)
        fmt = self.log_viewer.currentCharFormat()

        while not cursor.atEnd():
            cursor.select(QTextCursor.LineUnderCursor)
            line = cursor.selectedText()
            if "BLOCKED" in line or "WARNING" in line:
                fmt.setForeground(QColor("red"))  # Highlight in red
                cursor.setCharFormat(fmt)
            cursor.movePosition(QTextCursor.Down)

    def select_log_file(self):
        """Allow the user to select a different log file."""
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Log File", "", "Log Files (*.log);;All Files (*)", options=options)
        if file_path:
            self.log_file = file_path
            self.load_logs()

    def export_logs(self):
        """Export the current logs to a file."""
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Export Logs", "", "Log Files (*.log);;All Files (*)", options=options)
        if file_path:
            with open(file_path, "w") as f:
                f.write(self.log_viewer.toPlainText())
            self.log_viewer.append(f"\nLogs exported to {file_path}")

    def start_firewall(self):
        """Start the firewall process."""
        if self.firewall_process is None:
            self.firewall_process = subprocess.Popen(["python", "main.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.log_viewer.append("\nFirewall started.")

    def stop_firewall(self):
        """Stop the firewall process."""
        if self.firewall_process is not None:
            self.firewall_process.terminate()
            self.firewall_process = None
            self.log_viewer.append("\nFirewall stopped.")

    def closeEvent(self, event):
        """Ensure the firewall process is terminated when the GUI is closed."""
        self.stop_firewall()
        super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = FirewallGUI()
    gui.show()
    sys.exit(app.exec_())