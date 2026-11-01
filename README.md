<div align="center">

# 💰 Personal Expense Tracker

### Know where your money goes. Plan where it should go next.

A simple, formula-driven spreadsheet for tracking your **monthly budget**, **fixed expenses** and **everyday spending**, with a colourful dashboard that summarises any month at a glance.

![Excel](https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white)
![Google Sheets](https://img.shields.io/badge/Google_Sheets-34A853?style=for-the-badge&logo=googlesheets&logoColor=white)
![LibreOffice](https://img.shields.io/badge/LibreOffice-18A303?style=for-the-badge&logo=libreoffice&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-F7B500?style=for-the-badge)

**No macros &nbsp;•&nbsp; No add-ins &nbsp;•&nbsp; No subscriptions**
## Just a standard `.xlsx` file.

<br>

## Expenses tracker dashboard tab, shown with sample demo data, showing budget, spending by category and a budget vs spent chart
<img width="845" height="421" alt="a" src="https://github.com/user-attachments/assets/2ff48a1b-6021-47e7-b232-d41d23a2cc92" />





</div>

---

## 📦 What's in this repository

Expenses-Tracker
├── README.md                          
├── Expense_Tracker_Template.xlsx  ←the blank spreadsheet
├── build_expense_tracker.py      
└── LICENSE                        ← MIT license
```

| 📁 File | 📝 What it is |
|---|---|
| [`files/Expense_Tracker_Template.xlsx`](files/Expense_Tracker_Template.xlsx) | The ready-to-use, blank spreadsheet. **Start here.** |
| [`files/build_expense_tracker.py`](files/build_expense_tracker.py) | Python script that rebuilds the spreadsheet from scratch. |
| [`files/LICENSE`](files/LICENSE) | MIT license: use it, change it, share it. |

---

## ✨ Features

| Feature | Details |
|---|---|
| **Dashboard** | Month selector, key totals (income, budget, spent, remaining, money left) and a budget vs. spending chart. |
<img width="845" height="421" alt="a" src="https://github.com/user-attachments/assets/3fd2a113-91c9-44c3-bb38-3fdbc189b902" />



| **Category breakdown** | Budget, fixed costs, everyday spending, total spent, remaining and % used for every category. |
<img width="491" height="443" alt="b" src="https://github.com/user-attachments/assets/0150ec66-4da9-432c-b53c-8047852fb2d1" />

| **Colour-coded progress** | 🟢 under 80% &nbsp;•&nbsp; 🟡 80–100% &nbsp;•&nbsp; 🔴 over budget |
| **Fixed expenses** | Enter rent, car instalment, internet and more **once**. They count automatically every month while active. |
<img width="461" height="424" alt="d" src="https://github.com/user-attachments/assets/6e547cc5-48b8-4721-b671-f749dc87c9f1" />

| **Everyday transactions** | Log date, description, category and amount, with a handy category dropdown. |
<img width="461" height="422" alt="e" src="https://github.com/user-attachments/assets/744c4c53-dc8e-41ca-be51-fb52176ce2c7" />


| **Any currency** | Currency-neutral. Use whatever you spend in. |


---

## 🖼️ Screenshots

> [!NOTE]
> All screenshots use **made-up demo data** to show how the tracker works. None of it belongs to a real person.

### 📊 Dashboard

Pick a month, and see your income, total budget, total spent, what's left of the budget, and how much money you have left after spending. The table breaks everything down by category, and the chart compares budget against actual spending.

<img width="845" height="421" alt="a" src="https://github.com/user-attachments/assets/1dd3f18a-9118-45ef-a1f7-53d5b05b8bf0" />


### 💵 Budget

Set your monthly income and a budget for each category. Rename categories to fit your life.
<img width="491" height="443" alt="b" src="https://github.com/user-attachments/assets/9818c2bc-236d-4883-b33d-c58734c2a43f" />

### 🏠 Fixed Expenses

List recurring costs once. Use the **Active?** dropdown to switch an expense on or off.
<img width="461" height="424" alt="d" src="https://github.com/user-attachments/assets/6e547cc5-48b8-4721-b671-f749dc87c9f1" />

### 🛒 Transactions

Log everyday purchases. The **Category** column has a dropdown built from your Budget tab.
<img width="461" height="422" alt="e" src="https://github.com/user-attachments/assets/0add8879-2f34-445e-b5f3-59fe4a300c6c" />

---

## 🚀 Getting started

1. Download **`files/Expense_Tracker_Template.xlsx`** from this repository.
2. Open it in **Excel**, **LibreOffice** or **Google Sheets** (upload to Drive, then open with Google Sheets).
3. Follow the four setup steps below.

> [!TIP]
> Make a copy of the template for your own use and keep the original blank. Then you can always start fresh.

### 1️⃣ Budget tab 💵

- Enter your **monthly income** (after tax) in cell `B2`.
- Set a **monthly budget** for each category.
- Rename any category you like (for example, change "Shopping" to "Clothing"). There are **13 category slots**.

### 2️⃣ Fixed Expenses tab 🏠

List recurring costs once: rent, car instalment, insurance, internet, and so on.

| Column | What to enter |
|---|---|
| **Expense** | A name, e.g. "Car instalment" |
| **Category** | Pick from the dropdown (it comes from the Budget tab) |
| **Amount / month** | The monthly amount |
| **Due day** | Day of the month it is due (for your reference) |
| **Active?** | `Yes` to include it, `No` to pause it (e.g. after a loan is paid off) |

Active fixed expenses are included in **every month** you view on the Dashboard. There is room for **20 entries**.

### 3️⃣ Transactions tab 🛒

Add one row per purchase: **Date**, **Description**, **Category** (dropdown) and **Amount**.
Each month you only need to add new rows here. There is room for about **1,000 rows**.

### 4️⃣ Dashboard tab 📊

Type any date in the month you want to view into the **Select month** cell. It defaults to today's month, but you can type e.g. `2026-11-01`. The dashboard updates immediately.

---

## 🎬 See it in action

The screenshots above use this demo setup, so you can follow the numbers yourself.

**Demo income:** 30,000.00 &nbsp;•&nbsp; **Demo total budget:** 29,700.00

| 🏠 Fixed expense | Category | Amount | Active |
|---|---|---|---|
| Rent | Housing | 8,000.00 | ✅ Yes |
| Car instalment | Transport | 4,500.00 | ✅ Yes |
| Car insurance | Insurance | 900.00 | ✅ Yes |
| Internet | Internet | 700.00 | ✅ Yes |

| 🛒 Everyday spending | Category | Amount |
|---|---|---|
| Supermarket | Groceries | 1,250.50 |
| Fuel | Transport | 900.00 |
| Dinner out | Eating Out | 480.00 |
| Streaming | Subscriptions | 199.00 |

**What the Dashboard shows for October 2026**

- 🚗 **Transport** = 4,500 car instalment (fixed) + 900 fuel (everyday) = **5,400** of a 5,500 budget, so **98%** 🟡
- 🏠 **Housing** and 🌐 **Internet** are fully used at **100%** 🟡, because they are fixed costs that match their budgets exactly.
- 🛡️ **Insurance** is at **90%** 🟡.
- 💸 **Total spent:** 16,929.50 &nbsp;→&nbsp; 💚 **Budget remaining:** 12,770.50 &nbsp;→&nbsp; 💰 **Money left (income − spent):** 13,070.50

### ⏸️ What happens when you pause a fixed expense?

Set **Active? = No** for the car instalment and car insurance, and the Dashboard updates straight away. Transport drops to **16%** and total spent falls to **11,529.50**.

<div align="center">
<img src="screenshots/dashboard-paused-expenses.png" alt="Dashboard after pausing two fixed expenses" width="900">
</div>

This is handy for loans that finish, or subscriptions you cancel.

---

## 🧮 How it works

For the selected month and each category:

| Column | Formula |
|---|---|
| 🏠 **Fixed** | Sum of *active* fixed expenses in that category |
| 🛒 **Everyday** | Sum of transactions in that category dated within the selected month (`SUMIFS` with `EOMONTH`) |
| 💸 **Total spent** | Fixed + Everyday |
| 💚 **Remaining** | Budget − Total spent |
| 📈 **% used** | Total spent ÷ Budget |

**Cell colour guide**

| Colour | Meaning |
|---|---|
| 🟨 Yellow background | An input cell, yours to edit |
| 🔵 Blue text | A number you enter |
| 🟢 Green text | A value linked from another tab |
| ⚫ Black text | A formula, so leave it alone |

**Progress colours on the Dashboard**

| % used | Colour | Meaning |
|---|---|---|
| Under 80% | 🟢 Green | You're on track |
| 80% – 100% | 🟡 Amber | Getting close to your limit |
| Over 100% | 🔴 Red | Over budget |

---

## 💡 Tips

- ⚡ **Bills that vary** (electricity, water): enter an average as a fixed expense, or leave them out and log the real bill under Transactions each month.
- ⏸️ Mark a fixed expense **Active = No** when it ends instead of deleting it, so you keep a record.
- 🕰️ To look at a past month, just change the month on the Dashboard. Old transactions are still there.
- 🎨 **Make it yours:** change the Dashboard title, fonts and colours. Only edit the yellow input cells and leave the formulas alone, and everything will keep working.

> [!WARNING]
> Fixed expenses apply to **all months**. If an amount changes (e.g. a rent increase), the change also applies to past months you view. For accurate history, save a copy of the file for each year.

---

## 🔧 Customising

- ➕ **More categories:** the Dashboard and Budget tabs hold 13 categories. To add more, edit `files/build_expense_tracker.py` (the `cats` list and the row ranges) and regenerate, or extend the ranges in the formulas by hand.
- 💱 **Currency formatting:** select the amount cells and apply your preferred currency format.
- 🐍 **Rebuild from code:** the workbook is generated by a Python script.

```bash
cd files
pip install openpyxl
python build_expense_tracker.py
```

This creates a fresh `Expense_Tracker_Template.xlsx` in the `files` folder.

> [!NOTE]
> Open the generated file once in Excel or LibreOffice so the formulas calculate and the values are cached.

---

## 🔒 Privacy

Everything stays in your file. Nothing is sent anywhere.

> [!IMPORTANT]
> **Never commit your personal version with real financial data to a public repository.** Only the blank template belongs on GitHub. Keep your personal copy outside the repo, or add its name to `.gitignore`.

---

## 📜 License

Released under the [MIT License](files/LICENSE). Use it, change it, share it. 🎉

<div align="center">

⭐ **If this helped you, consider giving the repo a star!** ⭐

</div>
