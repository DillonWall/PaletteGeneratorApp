import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.button import Button
from kivy.core.window import Window


class MyContent(FloatLayout):
    def __init__(self, **kwargs):
        super(MyContent, self).__init__(**kwargs)

        left_padding = 0.1
        bottom_padding = 0.1
        clr_picker_width = 0.7
        clr_picker_height = 0.5
        gen_palette_btn_weight = 0.5
        gen_palette_btn_height = 0.2

        # ADD Color picker
        self.clr_picker = ColorPicker(
            size_hint=(clr_picker_width, clr_picker_height),
            pos_hint={"x": left_padding, "y": bottom_padding + gen_palette_btn_height + 0.1}
        )
        self.clr_picker.bind(
            on_color=self.clr_picker_on_color
        )
        self.add_widget(self.clr_picker)

        # ADD Generate palette button
        self.gen_palette_btn = Button(
            text="Generate Palette",
            size_hint=(gen_palette_btn_weight, gen_palette_btn_height),
            pos_hint={"x": left_padding, "y": bottom_padding}
        )
        self.gen_palette_btn.bind(on_press=self.gen_palette_on_press)
        self.add_widget(self.gen_palette_btn)

        # ADD Resulting palette rectangles
        line_thickness = 0.01
        left_side = 0.85
        top_side = 0.1
        box_width = 0.1

        with self.canvas.before:
            Color(1, 1, 1, 1)
            Rectangle(
                size=(Window.width * (box_width + (line_thickness * 2)),
                      Window.height * (((box_width + line_thickness) * 5) + line_thickness)),
                pos=(Window.width * (left_side - line_thickness),
                     Window.height * (top_side - line_thickness))
            )
            for i in range(5):
                Color(1, 0.5 + (i / 10), 0, 1)
                Rectangle(
                    size=(Window.width * box_width,
                          Window.height * box_width),
                    pos=(Window.width * left_side,
                         Window.height * (top_side + ((box_width + line_thickness) * i)))
                )

    # add canvas instructions that overrides the old rectangles with new ones
    # this should take in a list of 5 colors and draw over the old canvas.
    # Darkest on bottom, to lightest on top. Therefore, darkest color should be position [0] in the list

    # Can add a on_resize for the window that will update the position of the canvas items

    def clr_picker_on_color(self, instance, value):
        print("RGBA = ", str(self.clr_picker.color))
        print("HSV = ", str(self.clr_picker.hsv))
        print("HEX = ", str(self.clr_picker.hex_color))

    def gen_palette_on_press(self, instance):
        print('RGBA: ', str(self.clr_picker.color))


class PaletteGeneratorApp(App):
    def build(self):
        return MyContent()


if __name__ == "__main__":
    PaletteGeneratorApp().run()
