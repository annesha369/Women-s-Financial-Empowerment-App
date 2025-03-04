import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def set_background():
    st.markdown(
        """
        <style>
            .stApp {
                background: linear-gradient(135deg, #1a1a40, #4b0082, #8a2be2, #ff69b4);
                color: white;
                font-family: 'Arial', sans-serif;
            }
            .stMarkdown, .stTextInput, .stNumberInput, .stSelectbox, .stButton, .stDataFrame, .stHeader {
                color: white !important;
            }
            .stButton>button {
                background-color: #ff4500 !important;
                color: white !important;
                border-radius: 10px;
                font-weight: bold;
            }
            .stDataFrame, .stTable {
                background-color: rgba(255, 255, 255, 0.1) !important;
                border-radius: 12px;
            }
            .sidebar .sidebar-content {
                background: linear-gradient(135deg, #4b0082, #1a1a40);
            }
        </style>
        """,
        unsafe_allow_html=True
    )

def educational_resources():
    st.header("📚 Financial Education for Women")
    st.markdown("""
    - **Budgeting Tips:** Learn how to manage your income effectively.
    - **Investment Basics:** Understand stocks, mutual funds, and SIPs.
    - **Savings Strategies:** Tips for building an emergency fund.
    - **Retirement Planning:** Secure your future with smart financial planning.
    """)

def budget_planner():
    st.header("💡 Budget Planner")
    income = st.number_input("💵 Monthly Income (₹)", min_value=0.0, step=100.0)
    expenses = st.number_input("💸 Estimated Monthly Expenses (₹)", min_value=0.0, step=100.0)
    
    if st.button("📊 Calculate Budget", use_container_width=True):
        savings = income - expenses
        st.success(f"💰 Estimated Savings: ₹{savings:,.2f}")
        st.progress(min(max(savings/income, 0), 1))

def expense_tracker():
    st.header("📊 Expense Tracker")
    if "expenses" not in st.session_state:
        st.session_state.expenses = []
    
    date = st.date_input("📅 Date")
    category = st.selectbox("📌 Category", ["Food", "Transport", "Shopping", "Rent", "Other"])
    amount = st.number_input("💰 Amount (₹)", min_value=0.0, step=0.1)
    
    if st.button("➕ Add Expense", use_container_width=True):
        st.session_state.expenses.append({"Date": date, "Category": category, "Amount": amount})
    
    if st.session_state.expenses:
        df = pd.DataFrame(st.session_state.expenses)
        st.dataframe(df)
        st.subheader("Category-wise Expense Distribution")
        st.bar_chart(df.groupby("Category")["Amount"].sum())

def financial_planning():
    st.header("📅 Financial Planning")
    goal = st.text_input("🎯 Financial Goal")
    target_amount = st.number_input("💰 Target Amount (₹)", min_value=0.0, step=100.0)
    years = st.number_input("📆 Timeframe (years)", min_value=1, step=1)
    
    if st.button("📌 Plan Now", use_container_width=True):
        monthly_savings = target_amount / (years * 12)
        st.success(f"📈 You need to save ₹{monthly_savings:,.2f} per month to reach your goal.")

def sip_calculator():
    st.header("📈 SIP Calculator")
    monthly_investment = st.number_input("💵 Monthly Investment (₹)", min_value=0.0, step=100.0)
    annual_return = st.number_input("📊 Expected Annual Return (%)", min_value=0.0, step=0.1)
    years = st.number_input("⏳ Investment Duration (years)", min_value=1, step=1)
    
    if st.button("📉 Calculate SIP", use_container_width=True):
        months = years * 12
        rate = (annual_return / 100) / 12
        future_value = monthly_investment * (((1 + rate) ** months - 1) / rate) * (1 + rate)
        st.success(f"💰 Future Value: ₹{future_value:,.2f}")

def emi_calculator():
    st.header("🏦 EMI Calculator")
    loan_amount = st.number_input("💰 Loan Amount (₹)", min_value=0.0, step=1000.0)
    interest_rate = st.number_input("📈 Annual Interest Rate (%)", min_value=0.0, step=0.1)
    tenure_years = st.number_input("📆 Loan Tenure (years)", min_value=1, step=1)
    
    if st.button("🧮 Calculate EMI", use_container_width=True):
        monthly_rate = (interest_rate / 100) / 12
        tenure_months = tenure_years * 12
        emi = (loan_amount * monthly_rate * (1 + monthly_rate) ** tenure_months) / ((1 + monthly_rate) ** tenure_months - 1)
        st.success(f"💸 Monthly EMI: ₹{emi:,.2f}")

def investment_tracker():
    st.header("💼 Investment Portfolio Tracker")
    if "investments" not in st.session_state:
        st.session_state.investments = []
    
    asset = st.text_input("🏆 Asset Name")
    invested_amount = st.number_input("💰 Invested Amount (₹)", min_value=0.0, step=100.0)
    current_value = st.number_input("📈 Current Value (₹)", min_value=0.0, step=100.0)
    
    if st.button("➕ Add Investment", use_container_width=True):
        st.session_state.investments.append({"Asset": asset, "Invested Amount": invested_amount, "Current Value": current_value})
    
    if st.session_state.investments:
        df = pd.DataFrame(st.session_state.investments)
        df["Profit/Loss"] = df["Current Value"] - df["Invested Amount"]
        st.dataframe(df)
        st.subheader("📊 Profit/Loss Analysis")
        st.bar_chart(df.set_index("Asset")["Profit/Loss"])

def main():
    st.set_page_config(page_title="Women's Financial Tracker", page_icon="💰", layout="wide")
    set_background()
    st.title("💰 Women's Financial Empowerment App")
    menu = ["Educational Resources", "Budget Planner", "Expense Tracker", "Financial Planning", "SIP Calculator", "EMI Calculator", "Investment Portfolio"]
    choice = st.sidebar.radio("📌 Select Feature", menu)
    
    if choice == "Educational Resources":
        educational_resources()
    elif choice == "Budget Planner":
        budget_planner()
    elif choice == "Expense Tracker":
        expense_tracker()
    elif choice == "Financial Planning":
        financial_planning()
    elif choice == "SIP Calculator":
        sip_calculator()
    elif choice == "EMI Calculator":
        emi_calculator()
    elif choice == "Investment Portfolio":
        investment_tracker()

if __name__ == "__main__":
    main()
