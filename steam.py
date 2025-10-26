import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

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
    reason = text_reason.get("1.0", "end").strip()
    salary = entry_salary.get().strip()
    position = entry_position.get().strip()

    # Перевірки
    if not name:
        ctk.CTkMessageBox.show_error("Помилка", "Введіть ім'я та прізвище.")
        return
    if not is_positive_int(age) or int(age) == 0:
        ctk.CTkMessageBox.show_error("Помилка", "Вік повинен бути додатним цілим числом.")
        return
    if not is_positive_int(exp):
        ctk.CTkMessageBox.show_error("Помилка", "Стаж повинен бути невід'ємним цілим числом (роки).")
        return
    if not reason:
        ctk.CTkMessageBox.show_error("Помилка", "Напишіть, чому ви звільнилися з попереднього місця роботи.")
        return
    if not salary:
        ctk.CTkMessageBox.show_error("Помилка", "Вкажіть бажану заробітну плату.")
        return
    try:
        sal_val = float(salary.replace(",", "."))
        if sal_val < 0:
            raise ValueError
    except:
        ctk.CTkMessageBox.show_error("Помилка", "Зарплата повинна бути числом (наприклад: 1000 або 1200.50).")
        return
    if not position:
        ctk.CTkMessageBox.show_error("Помилка", "Вкажіть, ким ви хочете працювати.")
        return

    show_accept_window(name, position, sal_val)

def show_accept_window(name, position, salary):
    win = ctk.CTkToplevel(root)
    win.title("Результат")
    win.geometry("400x220")
    win.resizable(False, False)

    panel = ctk.CTkFrame(win, fg_color="#d4f7d4")
    panel.pack(fill="both", expand=True, padx=10, pady=10)

    lbl = ctk.CTkLabel(panel, text="Вас прийнято на роботу!", font=("Arial", 18, "bold"), fg_color="#d4f7d4")
    lbl.pack(pady=(20, 10))

    info = f"Ім'я: {name}\nПосада: {position}\nЗарплата: {salary}"
    lbl_info = ctk.CTkLabel(panel, text=info, font=("Arial", 12), fg_color="#d4f7d4", justify="left")
    lbl_info.pack(pady=(0, 12))

    btn_ok = ctk.CTkButton(panel, text="Готово", command=win.destroy, width=120, fg_color="#4CAF50", text_color="white")
    btn_ok.pack(pady=(0, 18))

# Основне вікно
root = ctk.CTk()
root.title("Реєстрація на роботу")
root.geometry("750x600")
root.resizable(False, False)
padx = 12
pady = 8

frame = ctk.CTkFrame(root)
frame.pack(padx=padx, pady=pady, fill="both", expand=True)

# Поля
lbl_name = ctk.CTkLabel(frame, text="1. Ім'я та прізвище:")
lbl_name.grid(row=0, column=0, sticky="w", pady=4)
entry_name = ctk.CTkEntry(frame, width=400)
entry_name.grid(row=0, column=1, pady=4, sticky="w")

lbl_age = ctk.CTkLabel(frame, text="2. Скільки вам років:")
lbl_age.grid(row=1, column=0, sticky="w", pady=4)
entry_age = ctk.CTkEntry(frame, width=100)
entry_age.grid(row=1, column=1, sticky="w", pady=4)

lbl_exp = ctk.CTkLabel(frame, text="3. Стаж роботи (роки):")
lbl_exp.grid(row=2, column=0, sticky="w", pady=4)
entry_exp = ctk.CTkEntry(frame, width=100)
entry_exp.grid(row=2, column=1, sticky="w", pady=4)

lbl_reason = ctk.CTkLabel(frame, text="4. Чому звільнилися з минулого місця роботи:")
lbl_reason.grid(row=3, column=0, sticky="nw", pady=4)
text_reason = ctk.CTkTextbox(frame, width=300, height=100)
text_reason.grid(row=3, column=1, pady=4, sticky="w")

lbl_salary = ctk.CTkLabel(frame, text="5. Бажана заробітна плата:")
lbl_salary.grid(row=4, column=0, sticky="w", pady=4)
entry_salary = ctk.CTkEntry(frame, width=200)
entry_salary.grid(row=4, column=1, sticky="w", pady=4)

lbl_position = ctk.CTkLabel(frame, text="6. Ким ви хочете бути на нашій роботі:")
lbl_position.grid(row=5, column=0, sticky="w", pady=4)
entry_position = ctk.CTkEntry(frame, width=400)
entry_position.grid(row=5, column=1, pady=4, sticky="w")

# Простір
frame.grid_rowconfigure(6, minsize=20)

# Кнопка відправки — зелена
btn_submit = ctk.CTkButton(frame, text="Надіслати документи", command=validate_and_submit,
                            fg_color="#4CAF50", text_color="white", font=("Arial", 12, "bold"), width=200)
btn_submit.grid(row=7, column=0, columnspan=2, pady=12)

# Підказка внизу
hint = ctk.CTkLabel(root, text="Заповніть всі поля та натисніть кнопку. Після успішної перевірки — відкриється повідомлення.",
                     font=("Arial", 9), text_color="gray")
hint.pack(side="bottom", pady=(0,10))

root.mainloop()
