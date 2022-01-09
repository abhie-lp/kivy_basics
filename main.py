from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Line, Color, Rectangle, Ellipse
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.slider import Slider
from kivy.uix.switch import Switch
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.graphics import Line


class WidgetsExample(GridLayout):
    count = StringProperty('1')
    start_counter = BooleanProperty(False)
    slider_value_txt = StringProperty('69')
    textinput_txt = StringProperty("TextInput")

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

    def on_switch_active(self, switch_button: Switch):
        print("Switch clicked", switch_button.active)

    def on_slider_value(self, slider_widget: Slider):
        print("Slider", slider_widget.value)
        # self.slider_value_txt = str(int(slider_widget.value))

    def on_textinput_validate(self, textinput: TextInput):
        self.textinput_txt = textinput.text


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


class CanvasExample1(Widget):
    pass


class CanvasExample2(Widget):
    pass


class CanvasExample3(Widget):
    pass


class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super(CanvasExample4, self).__init__(**kwargs)
        with self.canvas:
            Line(points=(100, 100, 400, 500), width=2)
            Color(0, 1, 0)
            Line(circle=(200, 400, 80), width=2)
            Color(1, 0, 0)
            Line(rectangle=(300, 170, 300, 150))
            self.rect = Rectangle(pos=(300, 10), size=(300, 150))

    def on_button_a_click(self):
        print("Button A")
        x, y = self.rect.pos
        w, _ = self.rect.size
        inc = dp(10)
        diff = self.width - (x + w)
        if diff < inc:
            inc = diff
        self.rect.pos = (x + inc, y)


class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super(CanvasExample5, self).__init__(**kwargs)
        self.ball_size = dp(50)
        self.mov_x, self.mov_y = dp(3), dp(3)
        with self.canvas:
            self.ball = Ellipse(pos=self.center,
                                size=(self.ball_size, self.ball_size))
        Clock.schedule_interval(self.update, 1/24)

    def on_size(self, *args):
        print("on size:", self.width, self.height)
        self.ball.pos = (self.center_x - self.ball_size / 2,
                         self.center_y - self.ball_size / 2)

    def update(self, dt):
        print("update")
        x, y = self.ball.pos
        if x + self.ball_size > self.width:
            self.mov_x *= -1
        elif x < 0:
            self.mov_x *= -1

        if y + self.ball_size > self.height:
            self.mov_y *= -1
        elif y < 0:
            self.mov_y *= -1
        self.ball.pos = (x + self.mov_x, y + self.mov_y)


class CanvasExample6(Widget):
    pass


class CanvasExample7(BoxLayout):
    pass


if __name__ == '__main__':
    TheLabApp().run()
