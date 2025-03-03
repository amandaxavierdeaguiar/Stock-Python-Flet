import flet as ft

def button_style():
    return ft.ButtonStyle(
            shape=ft.ContinuousRectangleBorder(radius=25),
            color={
                ft.MaterialState.DEFAULT: ft.colors.BLACK,
                ft.MaterialState.HOVERED: ft.colors.WHITE,
            },
            bgcolor={
                ft.MaterialState.DEFAULT: ft.colors.YELLOW,
                ft.MaterialState.HOVERED: ft.colors.AMBER_600,
            },
            elevation={"pressed": 0, "": 1},
            animation_duration=150,
        )
