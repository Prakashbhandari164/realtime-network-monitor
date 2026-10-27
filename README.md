# 📡 Network Packet Analyzer & Visualizer

A lightweight Python tool that intercepts network packets in real-time using **Scapy** and displays network activity on a live web dashboard built with **Flask**.

## 🚀 Features
- **Real-Time Sniffing**: Captures IP packets flowing through network interfaces.
- **Protocol Classification**: Identifies TCP, UDP, ICMP, and other protocols.
- **Live Web Dashboard**: Displays real-time network traffic automatically refreshing UI.

## 🛠️ Tech Stack
- **Language**: Python 3.x
- **Network Engine**: Scapy
- **Web Framework**: Flask
- **Frontend**: HTML5, CSS3, JavaScript (Fetch API)

## 📋 Prerequisites
Make sure you have Npcap (Windows) or libpcap (Linux/Mac) installed for packet capturing.

## 📦 Installation & Setup

1. Clone or extract the repository:
   ```bash
   cd network-packet-analyzer
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application (Requires Administrator / Sudo privileges):
   - **Windows** (Run Command Prompt / Terminal as Administrator):
     ```bash
     python app.py
     ```
   - **Linux / Mac**:
     ```bash
     sudo python3 app.py
     ```

4. Open your browser and go to `http://127.0.0.1:5000`
