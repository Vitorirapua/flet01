import flet as ft

def main(page: ft.Page):
    page.title = "Conversor de Temperatura"
    page.appbar = ft.AppBar(
        title=ft.Text("Conversor de Temperatura", color=ft.colors.WHITE),
        center_title=True,
        bgcolor=ft.colors.BLACK
    )
    page.bgcolor = ft.colors.LIGHT_BLUE_50

    def celsius_para_fahrenheit_kelvin(e):
        try:
            celsius_output.value = ""
            fahrenheit_output.value = ""
            kelvin_output.value = ""
            
            celsius = float(celsius_input.value)
            fahrenheit = (celsius * 9/5) + 32
            kelvin = celsius + 273.15
            fahrenheit_output.value = f"{fahrenheit:.2f} °F"
            kelvin_output.value = f"{kelvin:.2f} K"
            
            celsius_input.value = ""
            page.update()
        except ValueError:
            celsius_output.value = "Entrada inválida. Por favor, insira um número."
            page.update()

    def fahrenheit_para_celsius_kelvin(e):
        try:
            celsius_output.value = ""
            fahrenheit_output.value = ""
            kelvin_output.value = ""
            
            fahrenheit = float(fahrenheit_input.value)
            celsius = (fahrenheit - 32) * 5/9
            kelvin = (fahrenheit - 32) * 5/9 + 273.15
            celsius_output.value = f"{celsius:.2f} °C"
            kelvin_output.value = f"{kelvin:.2f} K"
            
            fahrenheit_input.value = ""
            page.update()
        except ValueError:
            fahrenheit_output.value = "Entrada inválida. Por favor, insira um número."
            page.update()

    def kelvin_para_celsius_fahrenheit(e):
        try:
            celsius_output.value = ""
            fahrenheit_output.value = ""
            kelvin_output.value = ""
            
            kelvin = float(kelvin_input.value)
            celsius = kelvin - 273.15
            fahrenheit = (kelvin - 273.15) * 9/5 + 32
            celsius_output.value = f"{celsius:.2f} °C"
            fahrenheit_output.value = f"{fahrenheit:.2f} °F"
            
            kelvin_input.value = ""
            page.update()
        except ValueError:
            kelvin_output.value = "Entrada inválida. Por favor, insira um número."
            page.update()

    def limpar_respostas(e):
        celsius_input.value = ""
        fahrenheit_input.value = ""
        kelvin_input.value = ""
        celsius_output.value = ""
        fahrenheit_output.value = ""
        kelvin_output.value = ""
        page.update()

    celsius_input = ft.TextField(label="Celsius", width=200, bgcolor=ft.colors.WHITE, border_color=ft.colors.BLUE)
    fahrenheit_input = ft.TextField(label="Fahrenheit", width=200, bgcolor=ft.colors.WHITE, border_color=ft.colors.BLUE)
    kelvin_input = ft.TextField(label="Kelvin", width=200, bgcolor=ft.colors.WHITE, border_color=ft.colors.BLUE)
    celsius_output = ft.Text(value="", size=20, color=ft.colors.RED)
    fahrenheit_output = ft.Text(value="", size=20, color=ft.colors.RED)
    kelvin_output = ft.Text(value="", size=20, color=ft.colors.RED)

    page.add(
        ft.Column([
            ft.Row([
                celsius_input,
                ft.ElevatedButton("Converter para Fahrenheit e Kelvin", on_click=celsius_para_fahrenheit_kelvin, bgcolor=ft.colors.BLUE, color=ft.colors.WHITE),
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
            ft.Row([
                fahrenheit_input,
                ft.ElevatedButton("Converter para Celsius e Kelvin", on_click=fahrenheit_para_celsius_kelvin, bgcolor=ft.colors.BLUE, color=ft.colors.WHITE),
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
            ft.Row([
                kelvin_input,
                ft.ElevatedButton("Converter para Celsius e Fahrenheit", on_click=kelvin_para_celsius_fahrenheit, bgcolor=ft.colors.BLUE, color=ft.colors.WHITE),
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
            ft.Row([
                celsius_output,
                fahrenheit_output,
                kelvin_output
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
        ft.Row([
            ft.ElevatedButton("Limpar Respostas", on_click=limpar_respostas, bgcolor=ft.colors.RED, color=ft.colors.WHITE),
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=10)
    )

ft.app(target=main)