from kivymd.tools.hotreload.app import MDApp
from kivy.lang import Builder
from gerenciamento.vencimentos import EmissorDeAvisos


class HotReload(MDApp):
    KV_FILES = ['interface\kivy_files\main.kv']
    DEBUG = True

    def enviar_vencimentos(self, path):
        emissor = EmissorDeAvisos(path)
        emissor.gerar_lista()
        emissor.enviar_mensagens()

    def build_app(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Dark"

        return Builder.load_file('interface\kivy_files\main.kv')


HotReload().run()
