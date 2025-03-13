# Network Monitoring System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6%2B-yellow)

## Fitur Utama
- Pemindaian jaringan terintegrasi
- Analisis WHOIS
- Deteksi teknologi web

## Penggunaan
```bash
# Install dependencies
pip3 install -r requirements.txt
npm install

# Jalankan scanner
python3 scanner.py example.com
# Untuk sistem Debian/Ubuntu
sudo apt update && sudo apt install -y \
    python3 \
    python3-pip \
    curl \
    whois \
    jq \
    whatweb \
    php-cli \
    npm

# Install Python packages
pip3 install requests python-whois
