# 👻 GhostPass - Secure Local Password Manager

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Security](https://img.shields.io/badge/Security-Encryption-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

**GhostPass** is a robust, CLI-based password manager built with Python. It focuses on **Data Security** and **Secure Coding practices**. 
Unlike simple storage tools, GhostPass implements a custom encryption mechanism to ensure that passwords are never stored in plain text (Encryption at Rest).

---

## 🚀 Key Features

* **🔐 Encryption at Rest:** Passwords are encrypted using a custom logic (XOR Operation + Base64 Encoding) before being stored in the database.
* **🛡️ Leak Detection:** Integrated check against the famous **RockYou.txt** dataset to warn users if their password has been previously compromised.
* **🎲 Strong Generator:** Generates cryptographically strong, random passwords using Python's `secrets` module.
* **💉 SQL Injection Protection:** Utilizes parameterized queries to prevent SQL injection attacks.
* **📂 Local Storage:** Uses SQLite3 for efficient, server-less data management.

---

## 🛠️ Technical Implementation

### The Encryption Logic
To protect user data, the tool does not store raw passwords. Instead, it processes them through a two-step obfuscation layer:
1.  **XOR Operation:** The plain password is XORed with a private `SECRET_KEY`.
2.  **Encoding:** The result is encoded into `Base64` to ensure safe storage in the text fields of the database.

> **Note:** This project is developed for educational purposes to demonstrate secure coding and data protection concepts.

---

## 📸 Screenshots

| Main Menu | Encryption Logic |
|:---:|:---:|
| ![Menu](YOUR_IMAGE_LINK_HERE) | ![Code](YOUR_IMAGE_LINK_HERE) |

*(Add screenshots of your tool here)*

---

## 💻 Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/GhostPass.git](https://github.com/YOUR_USERNAME/GhostPass.git)
    cd GhostPass
    ```

2.  **Install dependencies:**
    ```bash
    pip install termcolor pyfiglet
    ```

3.  **Run the tool:**
    ```bash
    python main.py
    ```

4.  **(Optional) Setup RockYou:**
    Ensure `rockyou.txt` is placed in the `password_manager/` directory for leak detection to work.

---

## 👤 Author

**Ammar Ahmad Alsaidi** Cyber Security Student @ JUST  
[LinkedIn Profile](YOUR_LINKEDIN_URL)

---

**⚠️ Disclaimer:** This tool is intended for personal use and educational demonstration. Always use industry-standard encryption (like AES) for enterprise-grade applications.
