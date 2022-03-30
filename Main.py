import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Appen(GridLayout):
    def __init__(self,**kwargs):
        super(Appen, self).__init__()
        self.cols = 2
        self.add_widget(Label(text = 'Elev Navn'))
        self.e_name = TextInput()
        self.add_widget(self.e_name)

        self.add_widget(Label(text='Karakter'))
        self.e_karakter = TextInput()
        self.add_widget(self.e_karakter)

        self.press = Button(text = 'Click me')
        self.press.bind(on_press = self.click_me)
        self.add_widget(self.press)

    def click_me(self, instance):
        print("Elevens Navn Er:"+ self.e_name.text)
        print("Elevens Karakter:" + self.e_karakter.text)
        print("")

class ItsHurting(App):
    def build(self):
        return Appen()
if __name__ == "__main__":
    ItsHurting().run()