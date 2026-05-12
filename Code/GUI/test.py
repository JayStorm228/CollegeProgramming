import tkinter as tk

colors = {
    "black": "#000000",
    "white": "#FFFFFF",
    "gray": "#666666",
    "red": "#E74C3C",
    "orange": "#E67E22",
    "yellow": "#F1C40F",
    "green": "#2ECC71",
    "white-blue": "#3498DB",
    "blue": "#2980B9",
}
# - **Базовое задание***: Создай форму с чекбоксом `«Я согласен с условиями»` и кнопкой `«Регистрация»`. Изначально кнопка должна быть в состоянии `disabled`.
# - **Challenge (UX)**: Реализуй логику: при установке галочки в чекбоксе кнопка переходит в `normal`, а при снятии — возвращается в `disabled`.
# Подсказка: используй параметр `command` у чекбокса для вызова метода проверки состояния.


class InteractionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GUI Architect: Урок 4")
        self.geometry("300x200")
        self._setup_ui()

    # Setup
    def _setup_ui(self):
        self._setup_Heading()
        self._setup_ConditionsCheckBox()
        self._setup_Registration_Button()

    def _setup_Heading(self):
        self.info_label = tk.Label(
            self, text="Регистрация Пользователя", font=("Verdana", 12), pady=20
        )
        self.info_label.pack()

    def _setup_ConditionsCheckBox(self):
        self.RegistrationFrame = tk.Frame(self, bg="#666666")
        self.RegistrationFrame.pack(fill="both", expand=True)
        self.ConditionsCheckBox = tk.Button(
            self.RegistrationFrame,
            bg=colors["white"],
            fg=colors["black"],
            text="I agree with terms",
            command=self._handle_CheckBox,
        )
        self.ConditionsCheckBox.pack(pady=5)

    def _setup_Registration_Button(self):
        self.RegistrationButton = tk.Button(
            self.RegistrationFrame,
            bg=colors["white"],
            fg=colors["black"],
            text="Зарегестрироваться",
            state="disabled",
            command=self._handle_Registration,
        )
        self.RegistrationButton.pack(pady=5)

    # Handlers
    def _handle_CheckBox(self):

        self.ConditionsCheckBox.configure(
            state="disabled",
            text="Agreed",
            fg=colors["green"],
        )
        self.RegistrationButton.configure(state="active")

    def _handle_Registration(self):

        self.RegistrationButton.configure(
            state="disabled", text="Successfully registered!", fg=colors["green"]
        )


if __name__ == "__main__":
    app = InteractionApp()
    app.mainloop()
