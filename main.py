from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton


class WidgetsExample(GridLayout):
    count = StringProperty('1')
    start_counter = BooleanProperty(False)

    def on_button_click(self):
        print('Button pressed.!!')
        if self.start_counter:
            self.count = str(int(self.count) + 1)

    def on_toggle_button_state(self, toggle_button: ToggleButton):
        print("Toggle clicked", toggle_button.state)
        if toggle_button.state == 'normal':
            toggle_button.text = 'OFF'
            self.start_counter = False
        else:
            toggle_button.text = 'ON'
            self.start_counter = True


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
