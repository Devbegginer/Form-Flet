import flet as ft

def main(page):
    # Título da página
    page.title = "Contact form"

    # Campos do formulário
    nome_input = ft.TextField(label="Name", autofocus=True)
    email_input = ft.TextField(label="Email")
    mensagem_input = ft.TextField(label="Message", multiline=True)

    # Função para processar o envio do formulário
    def enviar_formulario(e):
        # Aqui você pode adicionar lógica para processar os dados (como enviar para um servidor)
        page.add(ft.Text(f"Form sent successfully!\nNome: {nome_input.value}\nEmail: {email_input.value}\nMessage: {mensagem_input.value}", color=ft.colors.GREEN))

    # Botão de envio
    enviar_button = ft.ElevatedButton("Sent", on_click=enviar_formulario)

    # Adicionando os componentes na página
    page.add(nome_input, email_input, mensagem_input, enviar_button)

# Rodando a aplicação Flet
ft.app(target=main)
