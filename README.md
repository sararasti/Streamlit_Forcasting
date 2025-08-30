# 🎯 Lottery Participation Prediction App

This project is an interactive [Streamlit](https://streamlit.io/) application that predicts whether a **customer will participate in a lottery** based on their profile and purchase behavior.  
A machine learning model (trained and saved as `reg.joblib`) is used along with a custom preprocessing pipeline.

---

## 🚀 Features
- Simple and user-friendly interface built with Streamlit
- Accepts user input (Gender, Tier, Total Purchase, Frequency, Lifetime, Registration Date, Last Lottery Date)
- Data preprocessing with a custom `Preprocessor` class
- Trained ML model saved as `reg.joblib`
- Prediction results displayed clearly as ✅ *Participates* or ❌ *Does not participate*

---

## 🛠️ Project Structure
📂 Streamlit_Forcasting
┣ 📜 app.py # Streamlit application
┣ 📜 utils_1.py # Custom preprocessing class
┣ 📜 reg.joblib # Trained ML model
┣ 📜 requirements.txt # Required dependencies
┗ 📜 README.md # Project documentation


---

## 📊 Features Used
- **Gender**: Customer gender (Male/Female)
- **Tier**: Customer tier (Bronze, Silver, Gold, Platinum)
- **TotalPurchase**: Total purchase amount
- **Frequency**: Number of purchases
- **LongLife**: Customer lifetime (months)
- **RegisterDate**: Registration date
- **LastLotteryDate**: Last lottery participation date
- **DaysSinceRegister**: Days since registration
- **DaysSinceParticipate**: Days since last lottery participation

---
## 📷 Demo
<img width="689" height="828" alt="image" src="https://github.com/user-attachments/assets/50accba1-a785-4c1f-969d-e54063edd2af" />


## ⚙️ Installation & Run

### 1. Clone the repository
```bash
git clone https://github.com/sararasti/Streamlit_Forcasting.git
cd Streamlit_Forcasting
