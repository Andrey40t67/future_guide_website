import tkinter as tk
from tkinter import ttk, messagebox

# Функция для проверки кода доступа
def check_code():
    if entry_code.get() == "2914":
        show_main_interface()
    else:
        messagebox.showerror("Ошибка", "Неверный код. Попробуйте снова.")

# Функция для генерации прогноза на будущее
def generate_future(year):
    year = int(year)
    if year == 2024:
        return "2024: Год активного развития ИИ и устойчивой энергетики. Внедрение зелёных технологий в городах."
    elif year == 2025:
        return "2025: Начало массового перехода на электромобили и развитие инфраструктуры для них."
    elif year == 2026:
        return "2026: Виртуальная реальность становится частью повседневной жизни, работа и обучение переходят в VR."
    elif year == 2027:
        return "2027: Введение роботизированных помощников в каждом доме. Автоматизация большинства домашних задач."
    elif year == 2028:
        return "2028: Начало исследования и колонизации Луны. Первые поселения на лунной поверхности."
    elif year == 2029:
        return "2029: Биотехнологии позволяют лечить генетические болезни. Распространение персонализированной медицины."
    elif year == 2030:
        return "2030: Мировая экономика начинает переход на цифровую валюту. Криптовалюты становятся основными."
    elif year == 2031:
        return "2031: Появление высокоскоростных гиперлупов, связывающих мегаполисы по всему миру."
    elif year == 2032:
        return "2032: Первая полноценная база на Марсе, колонисты начинают исследовать Красную планету."
    elif year == 2033:
        return "2033: Разработка генетических технологий позволяет увеличить продолжительность жизни до 120 лет."
    elif year == 2034:
        return "2034: Синтетическая еда и водоросли становятся основными источниками питания."
    elif year == 2035:
        return "2035: Начало массового использования квантовых компьютеров в бизнесе и науке."
    elif year == 2036:
        return "2036: Построены первые города-парки, полностью автономные и экологически чистые."
    elif year == 2037:
        return "2037: ИИ создаёт первые произведения искусства, которые признаются мировыми шедеврами."
    elif year == 2038:
        return "2038: Первая успешная телепортация элементарных частиц на значительное расстояние."
    elif year == 2039:
        return "2039: Полное исчезновение бензиновых автомобилей, транспорт полностью электрифицирован."
    elif year == 2040:
        return "2040: Первые межзвёздные полёты на ближайшие экзопланеты с возможностью колонизации."
    # Добавляем аналогичные прогнозы для каждого года вплоть до 3000 года
    elif year == 3000:
        return "3000: Человечество полностью перешло на цифровое сознание, живёт в симбиозе с ИИ. Космическое расширение в другие галактики."
    else:
        return f"{year}: Год значительных изменений в науке, технологиях и обществе."

# Функция для отображения прогноза
def show_future():
    year = year_combobox.get()
    if year.isdigit() and 2024 <= int(year) <= 3000:
        future_text.set(generate_future(year))
    else:
        messagebox.showerror("Ошибка", "Пожалуйста, выберите год от 2024 до 3000.")

# Функция для отображения основного интерфейса
def show_main_interface():
    for widget in app.winfo_children():
        widget.destroy()
    
    # Заголовок
    header = tk.Label(app, text="Выберите год для прогноза", font=("Helvetica", 24, "bold"), bg="#e6f7ff", fg="#333")
    header.pack(pady=30)

    # Выпадающий список для выбора года
    year_label = tk.Label(app, text="Год (2024-3000):", font=("Helvetica", 18), bg="#e6f7ff", fg="#333")
    year_label.pack(pady=10)

    # Генерация списка годов от 2024 до 3000
    years = [str(year) for year in range(2024, 3001)]
    global year_combobox
    year_combobox = ttk.Combobox(app, values=years, font=("Helvetica", 18), width=15)
    year_combobox.pack(pady=10)

    # Кнопка для отображения информации
    show_button = tk.Button(app, text="Показать будущее", command=show_future, font=("Helvetica", 18), bg="#3399ff", fg="#fff", relief="solid", bd=2)
    show_button.pack(pady=20)

    # Текстовое поле для отображения информации о будущем
    global future_text
    future_text = tk.StringVar()
    future_label = tk.Label(app, textvariable=future_text, wraplength=1000, font=("Helvetica", 18), bg="#e6f7ff", fg="#333", justify="left")
    future_label.pack(pady=30)

# Создание основного окна приложения
app = tk.Tk()
app.title("Виртуальный гид по будущему")
app.geometry("1024x768")
app.attributes("-fullscreen", True)
app.configure(bg="#e6f7ff")

# Окно ввода кода доступа
entry_code = tk.Entry(app, font=("Helvetica", 24), show="*", width=10)
entry_code.pack(pady=200)

# Кнопка для проверки кода
check_button = tk.Button(app, text="Войти", command=check_code, font=("Helvetica", 24), bg="#3399ff", fg="#fff", relief="solid", bd=2)
check_button.pack(pady=20)

app.mainloop()
