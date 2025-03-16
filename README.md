# 🖩 PyQt6 Calculator 

## 📜 Overview
This is a simple calculator application built using **Python and PyQt6**. It follows the **Model-View-Controller (MVC)** design pattern, ensuring a clear separation between:
- **Model (calculator.py)** – Handles the core calculation logic.
- **View & Controller (gui.py)** – Manages the user interface and event handling.

---

## ✨ Features
✅ Perform basic arithmetic operations: **Addition (+), Subtraction (-), Multiplication (×), Division (÷)**  
✅ **User-friendly graphical interface** using PyQt6  
✅ **Input and results displayed** in a `QLineEdit` field  
✅ **AC (All Clear) button** to reset the input field  
✅ **Backspace (←) button** to delete the last digit  
✅ **Toggle sign (+/-) button** to switch between positive and negative numbers  
✅ **Error handling** for invalid expressions and division by zero  

---

## 🛠️ Technologies Used

- **Python**
- **PyQt6** for GUI development
- **MVC architecture**

---

## 📂 Project Structure
```
├── calculator.ui   # Your Qt Designer GUI file
├── calculator.py   # The logic model
├── gui.py          # Loads the .ui file and connects buttons
├── main.py         # Entry point 
├── README.md
```

## Sample Input/Output:

---

### Example 1:
8 + 10 = 18

### Example 2:
19 / 0 = Error: Division

![image](https://github.com/user-attachments/assets/8fcfe75d-b0c1-4714-b669-8495cc13d2aa)
![image](https://github.com/user-attachments/assets/a68e040e-fc18-40c8-b82b-faae67c12c29)
![image](https://github.com/user-attachments/assets/63aeef23-8898-4d6f-85bb-7929ea3ab342)
![image](https://github.com/user-attachments/assets/c0ec5193-6a94-4270-948d-ad0dc1c8e0e0)
