from kivy.app import App
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super(StackLayoutExample, self).__init__(**kwargs)
        size = dp(120)
        for i in range(200):
            self.add_widget(Button(
                text=f'Button {i}', size_hint=(None, None),
                size=(size, size)
            ))
        # for i in range(10, 20):
        #     size = size_constant + i * 2
        #     self.add_widget(Button(
        #         text=f'BUTTON {i}', size_hint=(None, None), size=(size, size)
        #     ))


class GridLayoutExample(GridLayout):
    pass


class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass


if __name__ == '__main__':
    TheLabApp().run()
