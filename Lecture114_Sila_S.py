from tkinter import *
from tkinter import ttk
from datetime import date
from currency_converter import CurrencyConverter
import statistics
import calendar


def get_yearly_rate(year):
    converter = CurrencyConverter(fallback_on_missing_rate=True, fallback_on_wrong_date=True)
    year_value = year
    rate_value = []
    for i in range(12):
        if i < 9:
            month = f'{year_value}-0{i + 1}-15'
        else:
            month = f'{year_value}-{i + 1}-15'
        ref_date = date.fromisoformat(month)
        converted_value = converter.convert(1, currency_start_value.get(),
                                            currency_target_value.get(), ref_date)
        rate_value.append(round(converted_value, 2))
    return rate_value


def exchange_rate_score(set_of_rate):
    rate_score = 0
    for i in range(11):
        rate_i = set_of_rate[i]
        rate_f = set_of_rate[i + 1]
        if rate_f > rate_i:
            rate_score = rate_score + 1
        else:
            rate_score = rate_score - 1
    return rate_score


def insert_values(set_of_value):
    for a in range(6):
        rate[a].config(text=set_of_value[a])
        rate[a+6].config(text=set_of_value[a+6])
    max_value_entry.delete(0, "end")
    max_value_entry.insert(0, round(max(set_of_value), 2))
    min_value_entry.delete(0, "end")
    min_value_entry.insert(0, round(min(set_of_value), 2))
    avg_value_entry.delete(0, "end")
    avg_value_entry.insert(0, round(statistics.mean(set_of_value), 2))


def show_values():
    rate_set = get_yearly_rate(int(year_selected.get()))
    clear_values()
    insert_values(rate_set)
    year_selected_label.config(text=year_selected.get())


def clear_values():
    for a in range(6):
        rate[a].config(text="")
        rate[a + 6].config(text="")


master = Tk()
master.title("Yearly Exchange Rate.")
master.geometry("320x520+500+200")

# Top Frame

top_frame = Frame(master)
top_frame.grid(row=0, column=0, pady=5)

currency_start_value = StringVar(value="---")
currency_start = ttk.Combobox(top_frame, textvariable=currency_start_value, font=("Angsana New", 20), width=5)
currency_start["value"] = ["THB", "USD", "EUR", "JPY", "GBP"]
currency_start.grid(row=0, column=0)

to_label = Label(top_frame, text="to", font=("Angsana New", 20))
to_label.grid(row=0, column=1)

currency_target_value = StringVar(value="---")
currency_target = ttk.Combobox(top_frame, textvariable=currency_target_value, font=("Angsana New", 20), width=5)
currency_target["value"] = ["THB", "USD", "EUR", "JPY", "GBP"]
currency_target.grid(row=0, column=2)

year_selected = IntVar(value="---เลือกปี---")
year_selecting = ttk.Combobox(top_frame, textvariable=year_selected, font=("Angsana New", 20), width=10)
year_values = []
for values in range(2000, 2021):
    year_values.append(values)
year_selecting['values'] = year_values
year_selecting.grid(row=0, column=3, padx=2, pady=10)

submit_button = Button(top_frame, text="ดูข้อมูล", font=("Angsana New", 20), command=show_values)
submit_button.grid(row=0, column=4, padx=2, pady=10, sticky=E)

# end of Top Frame

# Middle Frame

middle_frame = Frame(master)
middle_frame.grid(row=1, column=0, pady=5)

max_values_label = Label(middle_frame, text="อัตราแลกเปลี่ยนสูงสุด : ", font=("Angsana New", 20, "bold"))
max_values_label.grid(row=0, column=0, sticky=E)

max_value = StringVar(value="-maximum-")
max_value_entry = Entry(middle_frame, textvariable=max_value, font=("Angsana New", 20))
max_value_entry.grid(row=0, column=1, sticky=W)

min_values_label = Label(middle_frame, text="อัตราแลกเปลี่ยนต่ำสุด : ", font=("Angsana New", 20, "bold"))
min_values_label.grid(row=1, column=0, sticky=E)

min_value = StringVar(value="-minimum-")
min_value_entry = Entry(middle_frame, textvariable=min_value, font=("Angsana New", 20))
min_value_entry.grid(row=1, column=1, sticky=W)

avg_values_label = Label(middle_frame, text="อัตราแลกเปลี่ยนเฉลี่ย : ", font=("Angsana New", 20, "bold"))
avg_values_label.grid(row=2, column=0, sticky=E)

avg_value = StringVar(value="-average-")
avg_value_entry = Entry(middle_frame, textvariable=max_value, font=("Angsana New", 20))
avg_value_entry.grid(row=2, column=1, sticky=W)

# end of Middle Frame

# Bottom Frame

bottom_frame = Frame(master)
bottom_frame.grid(row=2, column=0, pady=5)

year_label = Label(bottom_frame, text="ข้อมูลของปี : ", font=("Angsana New", 20, "bold"))
year_label.grid(row=0, column=0, sticky=E)

year_selected_label = Label(bottom_frame, text="----", font=("Angsana New", 20))
year_selected_label.grid(row=0, column=1, sticky=W)

# end of Buttom Frame

# Table

table_frame = Frame(master)
table_frame.grid(row=3, column=0, pady=5)

label_month_1 = Label(table_frame, text="Month", font=("Angsana New", 20, "bold"))
label_month_1.grid(row=0, column=0, padx=10)

label_rate_1 = Label(table_frame, text="Rate", font=("Angsana New", 20, "bold"))
label_rate_1.grid(row=0, column=1, padx=10)

label_month_2 = Label(table_frame, text="Month", font=("Angsana New", 20, "bold"))
label_month_2.grid(row=0, column=2, padx=10)

label_rate_2 = Label(table_frame, text="Rate", font=("Angsana New", 20, "bold"))
label_rate_2.grid(row=0, column=3, padx=10)

month = []
for m in range(12):
    month.append(calendar.month_name[m+1])

for a in range(6):
    month_label = Label(table_frame, text=f"{month[a]} :")
    month_label.grid(row=a+1, column=0, sticky=E, padx=10, pady=10)

for b in range(6):
    month_label = Label(table_frame, text=f"{month[b+6]} :")
    month_label.grid(row=b+1, column=2, sticky=E, padx=10, pady=10)

rate = dict()
for a in range(6):
    rate[a] = Label(table_frame, text="",
                    font=("Angsana New", 20))
    rate[a].grid(row=a+1, column=1, sticky=W)
    rate[a+6] = Label(table_frame, text="",
                      font=("Angsana New", 20))
    rate[a+6].grid(row=a+1, column=3, sticky=W)

# end of Table

master.mainloop()
