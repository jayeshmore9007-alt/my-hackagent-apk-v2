from kivy.app import App
from kivy.uix.label import Label

class HackAgentApp(App):
    def build(self):
        return Label(text="HackAgent APK Ready!")

if __name__ == "__main__":
    HackAgentApp().run()
