import flet as ft
import json


def main(page: ft.Page):
    page.title = "Анкета"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = 50

    # Поля ввода
    name = ft.TextField(label="Имя", width=300)
    email = ft.TextField(label="Email", width=300)
    age = ft.TextField(label="Возраст", width=300)

    # Радиокнопки
    gender = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="male", label="Мужской"),
            ft.Radio(value="female", label="Женский"),
        ], alignment=ft.MainAxisAlignment.CENTER)
    )

    # Чекбоксы
    sports = ft.Checkbox(label="Спорт")
    music = ft.Checkbox(label="Музыка")
    agree = ft.Checkbox(label="Согласен на обработку данных")

    status = ft.Text("")

    def save_data(e):
        if not name.value or not email.value or not age.value:
            status.value = "Заполните все поля!"
            status.color = "red"
        elif not agree.value:
            status.value = "Подтвердите согласие!"
            status.color = "red"
        else:
            data = {"name": name.value, "email": email.value, "age": age.value,
                    "gender": gender.value, "sports": sports.value, "music": music.value}
            with open("data.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            status.value = "Сохранено!"
            status.color = "green"
        page.update()

    btn = ft.ElevatedButton("Сохранить", on_click=save_data)

    # Всё в одной колонке с центрированием
    page.add(
        ft.Column(
            [
                ft.Text("Анкета", size=30, weight="bold"),
                name,
                email,
                age,
                ft.Text("Пол:"),
                gender,
                ft.Text("Хобби:"),
                sports,
                music,
                agree,
                btn,
                status,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
        )
    )


ft.app(target=main)