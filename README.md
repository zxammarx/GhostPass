# GhostPass

A secure, local CLI Password Manager built with Python.

## Overview
This tool allows you to store, generate, and check passwords locally. It focuses on secure coding practices by using custom encryption (XOR + Base64) to protect data at rest and integrates with the RockYou dataset to detect leaked passwords.

## Features
- **Secure Storage:** Passwords are encrypted/obfuscated before saving to the local SQLite database.
- **Leak Detection:** Checks your passwords against the famous **RockYou.txt** leak list.
- **Password Generator:** Creates cryptographically strong, random passwords using Python's secrets module.
- **Safe Queries:** Utilizes parameterized SQL queries to prevent Injection attacks.

## How to Run

1. **Clone the repository:**
   git clone https://github.com/zxammarx/GhostPass.git
   cd GhostPass

2. **Install dependencies:**
   pip install termcolor pyfiglet

3. **Run the application:**
   python main.py

**Important Note:**
For the Leak Detection feature to work, you must place the `rockyou.txt` file in the same directory as `main.py`.

---
Created by Ammar Ahmad Alsaidi - Cyber Security Student
