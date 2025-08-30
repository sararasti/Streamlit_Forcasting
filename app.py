import streamlit as st
import pandas as pd
import joblib
from datetime import date

# مدل آموزش داده شده رو لود می‌کنیم
model = joblib.load("reg.joblib")

# عنوان اپ
st.title("🎯 Lottery Participation Prediction")

# گرفتن ورودی‌ها از کاربر
gender = st.selectbox("جنسیت", ["Male", "Female"])
tier = st.selectbox("سطح مشتری (Tier)", ["Bronze", "Silver", "Gold", "Platinum"])
total_purchase = st.number_input("میزان کل خرید (TotalPurchase)", min_value=0, max_value=100000000, value=500000)
frequency = st.slider("تعداد دفعات خرید (Frequency)", min_value=0, max_value=500, value=10)
longlife = st.slider("طول عمر مشتری (LongLife - ماه)", min_value=0, max_value=120, value=24)
register_date = st.date_input("تاریخ ثبت نام (RegisterDate)", value=date(2020, 1, 1))
last_lottery_date = st.date_input("آخرین تاریخ لاتاری (LastLotteryDate)", value=date(2023, 1, 1))

# محاسبه ستون‌های مشتق‌شده
today = pd.to_datetime(date.today())
DaysSinceRegister = (today - pd.to_datetime(register_date)).days
DaysSinceParticipate = (today - pd.to_datetime(last_lottery_date)).days

# مپ Tier به عدد (مطابق دیتای آموزش)
tier_map = {
    "Bronze": 0,
    "Silver": 1,
    "Gold": 2,
    "Platinum": 3
}

# ساخت دیتا برای پیش‌بینی
row = {
    "Gender": gender,
    "Tier": tier_map[tier],
    "TotalPurchase": total_purchase,
    "Frequency": frequency,
    "LongLife": longlife,
    "DaysSinceRegister": DaysSinceRegister,
    "DaysSinceParticipate": DaysSinceParticipate
}
X = pd.DataFrame([row])

# تابع پیش‌بینی
def predict():
    prediction = model.predict(X)

    if prediction[0] == 1:
        st.success("✅ مشتری در لاتاری شرکت می‌کند")
    else:
        st.error("❌ مشتری در لاتاری شرکت نمی‌کند")

# دکمه اجرا
st.button("Predict", on_click=predict)
