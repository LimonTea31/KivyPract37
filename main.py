from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.boxlayout import BoxLayout

class MyPaintWidget(Widget):
    line_width = 1

    def on_touch_down(self, touch):

        with self.canvas:
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=self.line_width)

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class MyPaintApp(App):

    def build(self):
        parent = BoxLayout(orientation='vertical')
        self.painter = MyPaintWidget()

        button_layout = BoxLayout()
        clearbtn = Button(text='Clear')
        clearbtn.bind(on_release=self.clear_canvas)
        colorbtn = Button(text='Change Color')
        colorbtn.bind(on_release=self.change_color)
        widthbtn = Button(text='Change Line Width')
        widthbtn.bind(on_release=self.change_line_width)
        reduce_width_btn = Button(text='Reduce Line Width')
        reduce_width_btn.bind(on_release=self.reduce_line_width)

        button_layout.add_widget(clearbtn)
        button_layout.add_widget(colorbtn)
        button_layout.add_widget(widthbtn)
        button_layout.add_widget(reduce_width_btn)

        parent.add_widget(self.painter)
        parent.add_widget(button_layout)

        return parent

    def clear_canvas(self, obj):
        self.painter.canvas.clear()
    def change_color(self, obj):
        color = (random(), 1, 1)
        with self.painter.canvas:
            Color(*color, mode='hsv')


    def change_line_width(self, obj):
        self.painter.line_width += 1

    def reduce_line_width(self, obj):
        if self.painter.line_width > 1:
            self.painter.line_width -= 1

if __name__ == '__main__':
    MyPaintApp().run()
