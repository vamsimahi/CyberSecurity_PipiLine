# Cybersecurity Pipeline using Streamlit, Nmap & Gobuster

OUTPUT:


This project is an agentic cybersecurity pipeline that automates security audits using Streamlit, Nmap, and Gobuster. It allows users to perform penetration testing, scan networks, and analyze security vulnerabilities interactively.

🚀 Features

Nmap Integration: Perform network scanning & vulnerability detection.

Gobuster Integration: Conduct directory enumeration for hidden files and directories.

Streamlit UI: User-friendly web interface to trigger and monitor security scans.

Automated Workflow: Executes security tools in a structured pipeline.

📌 Prerequisites

Ensure you have the following installed:

Python 3.8+ - Download here

pip (Python Package Manager)

Streamlit - Install using:
pip install streamlit
Nmap - Install from Nmap Official Website

Gobuster - Install using:

sudo apt install gobuster  # Linux
brew install gobuster       # macOS
choco install gobuster      # Windows (via Chocolatey)

📂 Project Structure

Cybersecurity-Pipeline/
│── main.py          # Main Streamlit App
│── requirements.txt # Dependencies
│── wordlists/       # Wordlists for Gobuster
│── README.md        # Documentation

🔧 Installation & Setup

Step 1️⃣: Clone the Repository

git clone https://github.com/your-username/cybersecurity-pipeline.git
cd cybersecurity-pipeline

Step 2️⃣: Create a Virtual Environment

python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

Step 3️⃣: Install Dependencies

pip install -r requirements.txt

🛠️ Usage

Step 4️⃣: Run the Streamlit App

streamlit run main.py

The app will be accessible at http://localhost:8501.

Step 5️⃣: Perform a Security Scan

Enter the Target URL/IP

Select Nmap Scan or Gobuster Scan

Click "Start Scan" to execute

🛡️ Running Nmap Scan Manually

nmap -sV -A -T4 <TARGET-IP>

🔍 Running Gobuster Manually

gobuster dir -u "http://target.com/" -w "wordlists/common.txt" --exclude-status 301 -r
