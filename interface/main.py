from kivy.lang import Builder
from kivymd.app import MDApp
from gerenciamento.vencimentos import EmissorDeAvisos
from datetime import datetime




class MainApp(MDApp):
    KV_FILES = ['interface\kivy_files\main.kv']
    def enviar_vencimentos(self, path):
        path_is_valid = False
        self.root.ids.error.text = ""
        try:
            emissor = EmissorDeAvisos(str(path))
            emissor.gerar_lista()
            emissor.enviar_mensagens()
            path_is_valid = True
        except Exception as e:
            print(e)
            if str(e).startswith("[Errno 2]"):
                if not str(e).endswith("'../log/log.txt'"):
                    self.root.ids.error.theme_text_color = "Error"
                    self.root.ids.error.text = "Erro: Não foi possível encontrar o arquivo especificado"
                else:
                    self.root.ids.error.theme_text_color = "Hint"
                    self.root.ids.error.text = "Aviso: Não foi possível encontrar o arquivo de log"
        if path_is_valid:
            self.root.ids.error.theme_text_color = "Secondary"
            self.root.ids.error.text = "Vencimentos enviados com sucesso"

    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file("interface\kivy_files\main.kv")


if __name__ == "__main__":
    MainApp().run()
