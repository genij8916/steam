import tkinter as tk
from tkinter import messagebox

def is_positive_int(s):
    try:
        v = int(s)
        return v >= 0
    except:
        return False

def validate_and_submit():
    name = entry_name.get().strip()
    age = entry_age.get().strip()
    exp = entry_exp.get().strip()
    reason = text_reason.get("1.0", tk.END).strip()
    salary = entry_salary.get().strip()
    position = entry_position.get().strip()

    # Перевірки
    if not name:
        messagebox.showerror("Помилка", "Введіть ім'я та прізвище.")
        return
    if not is_positive_int(age) or int(age) == 0:
        messagebox.showerror("Помилка", "Вік повинен бути додатним цілим числом.")
        return
    if not is_positive_int(exp):
        messagebox.showerror("Помилка", "Стаж повинен бути невід'ємним цілим числом (роки).")
        return
    if not reason:
        messagebox.showerror("Помилка", "Напишіть, чому ви звільнилися з попереднього місця роботи.")
        return
    if not salary:
        messagebox.showerror("Помилка", "Вкажіть бажану заробітну плату.")
        return
    # пробуємо перетворити зарплату в число (можна з копійками)
    try:
        sal_val = float(salary.replace(",", "."))
        if sal_val < 0:
            raise ValueError
    except:
        messagebox.showerror("Помилка", "Зарплата повинна бути числом (наприклад: 10000 або 100000).")
        return
    if not position:
        messagebox.showerror("Помилка", "Вкажіть, ким ви хочете працювати.")
        return

    # Якщо всі перевірки пройшли — відкриваємо вікно підтвердження
    show_accept_window(name, position, sal_val)

def show_accept_window(name, position, salary):
    win = tk.Toplevel(root)
    win.title("Результат")
    win.geometry("400x220")
    win.resizable(False, False)
    # Зелений фон або зелена панель
    panel = tk.Frame(win, bg="#d4f7d4")
    panel.pack(fill="both", expand=True)

    lbl = tk.Label(panel, text="Вас прийнято на роботу!", font=("Arial", 18, "bold"), bg="#d4f7d4")
    lbl.pack(pady=(20, 10))

    info = f"Ім'я: {name}\nПосада: {position}\nЗарплата: {salary}"
    lbl_info = tk.Label(panel, text=info, font=("Arial", 12), bg="#d4f7d4", justify="left")
    lbl_info.pack(pady=(0, 12))

    btn_ok = tk.Button(panel, text="Готово", command=win.destroy, width=12, bg="#4CAF50", fg="white")
    btn_ok.pack(pady=(0, 18))

# Основне вікно
root = tk.Tk()
root.title("Реєстрація на роботу")
root.geometry("600x520")
root.resizable(False, False)
padx = 12
pady = 8

frame = tk.Frame(root)
frame.pack(padx=padx, pady=pady, fill="both", expand=True)

# Поля
lbl_name = tk.Label(frame, text="1. Ім'я та прізвище:")
lbl_name.grid(row=0, column=0, sticky="w", pady=4)
entry_name = tk.Entry(frame, width=50)
entry_name.grid(row=0, column=1, pady=4, sticky="w")

lbl_age = tk.Label(frame, text="2. Скільки вам років:")
lbl_age.grid(row=1, column=0, sticky="w", pady=4)
entry_age = tk.Entry(frame, width=10)
entry_age.grid(row=1, column=1, sticky="w", pady=4)

lbl_exp = tk.Label(frame, text="3. Стаж роботи (роки):")
lbl_exp.grid(row=2, column=0, sticky="w", pady=4)
entry_exp = tk.Entry(frame, width=10)
entry_exp.grid(row=2, column=1, sticky="w", pady=4)

lbl_reason = tk.Label(frame, text="4. Чому звільнилися з минулого місця роботи:")
lbl_reason.grid(row=3, column=0, sticky="nw", pady=4)
text_reason = tk.Text(frame, width=38, height=5)
text_reason.grid(row=3, column=1, pady=4, sticky="w")

lbl_salary = tk.Label(frame, text="5. Бажана заробітна плата:")
lbl_salary.grid(row=4, column=0, sticky="w", pady=4)
entry_salary = tk.Entry(frame, width=20)
entry_salary.grid(row=4, column=1, sticky="w", pady=4)

lbl_position = tk.Label(frame, text="6. Ким ви хочете бути на нашій роботі:")
lbl_position.grid(row=5, column=0, sticky="w", pady=4)
entry_position = tk.Entry(frame, width=50)
entry_position.grid(row=5, column=1, pady=4, sticky="w")

# Простір
frame.grid_rowconfigure(6, minsize=20)

# Кнопка відправки — зелена
btn_submit = tk.Button(frame, text="Надіслати документи", command=validate_and_submit,
                       bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), padx=10, pady=6)
btn_submit.grid(row=7, column=0, columnspan=2, pady=12)

# Підказка внизу
hint = tk.Label(root, text="Заповніть всі поля та натисніть кнопку. Після успішної перевірки — відкриється повідомлення.",
                font=("Arial", 9), fg="gray")
hint.pack(side="bottom", pady=(0,10))

root.mainloop()
