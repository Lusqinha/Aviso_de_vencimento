from kivy.lang import Builder
from kivymd.app import MDApp
from gerenciamento.vencimentos import EmissorDeAvisos


class MainApp(MDApp):
    KV_FILES = ['interface\kivy_files\main.kv']

    def enviar_vencimentos(self, path):
        emissor = EmissorDeAvisos(path)
        emissor.gerar_lista()
        emissor.enviar_mensagens()

    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file("interface\kivy_files\main.kv")


if __name__ == "__main__":
    MainApp().run()
