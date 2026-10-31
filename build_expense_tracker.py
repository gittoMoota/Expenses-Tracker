"""Generates Expense_Tracker_Template.xlsx.  Usage: pip install openpyxl && python build_expense_tracker.py"""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.chart import BarChart, Reference
from openpyxl.formatting.rule import CellIsRule, DataBarRule
from openpyxl.worksheet.datavalidation import DataValidation
from datetime import date

F = "Arial"
def font(**k): return Font(name=F, size=k.pop("size",10), **k)
BLUE = "0000FF"; GREEN="008000"
HDR = PatternFill("solid", fgColor="1F3A5F")
INP = PatternFill("solid", fgColor="FFF9DB")
KPI = PatternFill("solid", fgColor="EEF3F9")
thin = Side(style="thin", color="D0D7DE")
box = Border(left=thin,right=thin,top=thin,bottom=thin)
NUM = '#,##0.00;[Red](#,##0.00);-'
PCT = '0%'

wb = Workbook()
d = wb.active; d.title = "Dashboard"
b = wb.create_sheet("Budget")
fx = wb.create_sheet("Fixed Expenses")
tx = wb.create_sheet("Transactions")

def header(ws, row, labels, col=1):
    for i,l in enumerate(labels):
        c = ws.cell(row=row, column=col+i, value=l)
        c.font = font(bold=True, color="FFFFFF"); c.fill = HDR
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True); c.border = box

# ---------- Budget ----------
b["A1"] = "Monthly Budget"; b["A1"].font = font(size=16, bold=True)
b["A2"] = "Monthly income (after tax)"; b["A2"].font = font(bold=True)
b["B2"] = 0; b["B2"].font = font(color=BLUE); b["B2"].fill = INP; b["B2"].number_format = NUM; b["B2"].border = box
b["C2"] = "← enter your income"; b["C2"].font = font(italic=True, color="666666")
header(b, 4, ["Category", "Monthly budget"])
cats = [("Housing",0),("Transport",0),("Groceries",0),("Utilities",0),("Internet",0),("Insurance",0),
        ("Health",0),("Eating Out",0),("Entertainment",0),("Shopping",0),("Savings",0),
        ("Subscriptions",0),("Other",0)]
for i,(c,a) in enumerate(cats):
    r = 5+i
    b.cell(r,1,c).font = font(color=BLUE); b.cell(r,1).fill = INP; b.cell(r,1).border = box
    x = b.cell(r,2,a); x.font = font(color=BLUE); x.fill = INP; x.number_format = NUM; x.border = box
b["A18"] = "Total"; b["A18"].font = font(bold=True)
b["B18"] = "=SUM(B5:B17)"; b["B18"].font = font(bold=True); b["B18"].number_format = NUM
b["A20"] = "Yellow cells are yours to edit. Rename categories freely - everything else updates. "
b["A20"].font = font(italic=True, color="666666")
b.column_dimensions["A"].width = 28; b.column_dimensions["B"].width = 18; b.column_dimensions["C"].width = 28

# ---------- Fixed expenses ----------
fx["A1"] = "Fixed / Recurring Expenses"; fx["A1"].font = font(size=16, bold=True)
fx["A2"] = "Counted automatically in every month while Active = Yes (rent, car instalment, insurance...)."
fx["A2"].font = font(italic=True, color="666666")
header(fx, 4, ["Expense", "Category", "Amount / month", "Due day", "Active?"])
fixed = []  # example rows are removed on the final template
_old = [("Rent","Housing",8000,1,"Yes"),("Car instalment","Transport",4500,25,"Yes"),
         ("Car insurance","Insurance",900,1,"Yes"),("Internet","Internet",700,5,"Yes")]
for i in range(20):
    r = 5+i
    for c in range(1,6):
        cell = fx.cell(r,c); cell.fill = INP; cell.border = box; cell.font = font(color=BLUE)
    fx.cell(r,3).number_format = NUM
    if i < len(fixed):
        for c,v in enumerate(fixed[i],1): fx.cell(r,c,v)
dv = DataValidation(type="list", formula1="=Budget!$A$5:$A$17", allow_blank=True); fx.add_data_validation(dv); dv.add("B5:B24")
dv2 = DataValidation(type="list", formula1='"Yes,No"', allow_blank=True); fx.add_data_validation(dv2); dv2.add("E5:E24")
fx["A26"] = "Total active fixed"; fx["A26"].font = font(bold=True)
fx["C26"] = '=SUMIFS(C5:C24,E5:E24,"Yes")'; fx["C26"].font = font(bold=True); fx["C26"].number_format = NUM
for col,w in zip("ABCDE",[26,20,18,10,10]): fx.column_dimensions[col].width = w

# ---------- Transactions ----------
tx["A1"] = "Transactions (everyday spending)"; tx["A1"].font = font(size=16, bold=True)
tx["A2"] = "Add one row per purchase. Pick the category from the dropdown. Start typing in row 5."
tx["A2"].font = font(italic=True, color="666666")
header(tx, 4, ["Date", "Description", "Category", "Amount"])
ex = []  # example rows are removed on the final template
_old_ex = [(date(2026,10,2),"Supermarket","Groceries",1250.50),(date(2026,10,5),"Fuel","Transport",900),
      (date(2026,10,8),"Dinner out","Eating Out",480),(date(2026,10,12),"Streaming","Subscriptions",199)]
for i in range(996):
    r = 5+i
    for c in range(1,5):
        cell = tx.cell(r,c); cell.border = box; cell.font = font(color=BLUE)
    tx.cell(r,1).number_format = "yyyy-mm-dd"; tx.cell(r,4).number_format = NUM
    if i < len(ex):
        for c,v in enumerate(ex[i],1): tx.cell(r,c,v)
dv3 = DataValidation(type="list", formula1="=Budget!$A$5:$A$17", allow_blank=True); tx.add_data_validation(dv3); dv3.add("C5:C1000")
dv4 = DataValidation(type="date", operator="greaterThan", formula1="36526", allow_blank=True,
                     error="Enter a valid date, e.g. 2026-10-15"); tx.add_data_validation(dv4); dv4.add("A5:A1000")
for col,w in zip("ABCD",[14,32,20,16]): tx.column_dimensions[col].width = w
tx.freeze_panes = "A5"

# ---------- Dashboard ----------
d.sheet_view.showGridLines = False
d["A1"] = "Expense Tracker Dashboard"; d["A1"].font = font(size=18, bold=True, color="1F3A5F")
d["A3"] = "Select month"; d["A3"].font = font(bold=True)
d["B3"] = "=TODAY()"; d["B3"].number_format = "mmmm yyyy"; d["B3"].font = font(color=BLUE, bold=True)
d["B3"].fill = INP; d["B3"].border = box; d["B3"].alignment = Alignment(horizontal="center")
d["C3"] = "← type any date in the month you want to view (defaults to today's month)"; d["C3"].font = font(italic=True, color="666666")
d["A4"] = "Period"; d["A4"].font = font(bold=True)
d["B4"] = '=TEXT(EOMONTH(B3,-1)+1,"d mmm yyyy")&" - "&TEXT(EOMONTH(B3,0),"d mmm yyyy")'
d["B4"].font = font(color="666666")

kp = [("Income","=Budget!B2"),("Total budget","=B25"),("Total spent","=E25"),
      ("Budget remaining","=B25-E25"),("Money left (income - spent)","=A7-C7")]
for i,(l,f) in enumerate(kp):
    c = d.cell(6,1+i,l); c.font = font(bold=True, color="555555", size=9); c.fill = KPI
    c.alignment = Alignment(horizontal="center", wrap_text=True, vertical="center")
    v = d.cell(7,1+i,f); v.font = font(bold=True, size=14); v.fill = KPI; v.number_format = NUM
    v.alignment = Alignment(horizontal="center", vertical="center")
d["A7"].font = font(bold=True, size=14, color=GREEN)
d.row_dimensions[6].height = 28; d.row_dimensions[7].height = 28
d["E7"] = "=A7-C7"
d["D7"] = "=B25-E25"
d["B7"] = "=B25"; d["C7"] = "=E25"

d["A9"] = "Spending by category"; d["A9"].font = font(size=12, bold=True)
header(d, 11, ["Category","Budget","Fixed","Everyday","Total spent","Remaining","% used"])
START = "(EOMONTH($B$3,-1)+1)"; END = "EOMONTH($B$3,0)"
for i in range(13):
    r = 12+i; br = 5+i
    d.cell(r,1,f'=IF(Budget!A{br}="","",Budget!A{br})').font = font(color=GREEN)
    d.cell(r,2,f'=IF($A{r}="","",Budget!B{br})').font = font(color=GREEN)
    d.cell(r,3,f'=IF($A{r}="","",SUMIFS(\'Fixed Expenses\'!$C$5:$C$24,\'Fixed Expenses\'!$B$5:$B$24,$A{r},\'Fixed Expenses\'!$E$5:$E$24,"Yes"))')
    d.cell(r,4,f'=IF($A{r}="","",SUMIFS(Transactions!$D$5:$D$1000,Transactions!$C$5:$C$1000,$A{r},Transactions!$A$5:$A$1000,">="&{START},Transactions!$A$5:$A$1000,"<="&{END}))')
    d.cell(r,5,f'=IF($A{r}="","",C{r}+D{r})')
    d.cell(r,6,f'=IF($A{r}="","",B{r}-E{r})')
    d.cell(r,7,f'=IF($A{r}="","",IF(B{r}=0,0,E{r}/B{r}))')
    for c in range(1,8):
        cell = d.cell(r,c); cell.border = box
        if c not in (2,): 
            if cell.font.color is None or cell.font.color.rgb in (None,"00000000"): cell.font = font()
        if 2 <= c <= 6: cell.number_format = NUM
    d.cell(r,7).number_format = PCT
    d.cell(r,7).font = font()


d["A25"] = "Total"
for c,col in zip(range(2,7),"BCDEF"):
    d.cell(25,c,f"=SUM({col}12:{col}24)")
d["G25"] = "=IF(B25=0,0,E25/B25)"
for c in range(1,8):
    cell = d.cell(25,c); cell.font = font(bold=True); cell.fill = KPI; cell.border = box
    if 2<=c<=6: cell.number_format = NUM
d["G25"].number_format = PCT

red = PatternFill("solid", bgColor="F8CBCB"); amb = PatternFill("solid", bgColor="FFE8A8"); grn = PatternFill("solid", bgColor="CDEBD3")
d.conditional_formatting.add("G12:G24", CellIsRule(operator="greaterThan", formula=["1"], fill=red))
d.conditional_formatting.add("G12:G24", CellIsRule(operator="between", formula=["0.8","1"], fill=amb))
d.conditional_formatting.add("G12:G24", CellIsRule(operator="lessThan", formula=["0.8"], fill=grn))
d.conditional_formatting.add("F12:F24", CellIsRule(operator="lessThan", formula=["0"], font=Font(name=F, color="C00000", bold=True)))

# notes to use the dashboard
notes = ["How to use",
 "1. Budget tab: set your monthly income and a budget per category (rename categories as you like).",
 "2. Fixed Expenses tab: list rent, car instalment, etc. once - they count in every month automatically.",
 "3. Transactions tab: log each everyday purchase with date, category and amount.",
 "4. Come back here and pick the month at the top. Yellow cells = inputs, blue text = your numbers, green = linked.",
 "Green % = under 80% of budget, amber = 80-100%, red = over budget. Currency-neutral: use any currency."]
for i,t in enumerate(notes):
    c = d.cell(27+i,1,t); c.font = font(bold=(i==0), color="444444" if i else "000000", size=10 if i else 11)

# chart
ch = BarChart(); ch.type = "bar"; ch.style = 10; ch.title = "Budget vs spent"
ch.add_data(Reference(d, min_col=2, min_row=11, max_row=24), titles_from_data=True)
ch.add_data(Reference(d, min_col=5, min_row=11, max_row=24), titles_from_data=True)
ch.set_categories(Reference(d, min_col=1, min_row=12, max_row=24))
ch.height = 11; ch.width = 18
d.add_chart(ch, "I3")

for col,w in zip("ABCDEFG",[24,16,16,16,18,16,12]): d.column_dimensions[col].width = w
wb.save("Expense_Tracker_Template.xlsx")
print("Created Expense_Tracker_Template.xlsx")
