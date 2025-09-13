from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

KV = '''
<CalcLayout>:
    orientation: 'vertical'
    padding: 16
    spacing: 10

    BoxLayout:
        size_hint_y: None
        height: '48dp'
        TextInput:
            id: num1
            input_filter: 'float'
            hint_text: 'First number'
            multiline: False
        TextInput:
            id: num2
            input_filter: 'float'
            hint_text: 'Second number'
            multiline: False

    BoxLayout:
        size_hint_y: None
        height: '48dp'
        spacing: 8
        Button:
            text: '+'
            on_press: root.calculate('+')
        Button:
            text: '-'
            on_press: root.calculate('-')
        Button:
            text: '×'
            on_press: root.calculate('*')
        Button:
            text: '÷'
            on_press: root.calculate('/')

    Label:
        id: result
        text: 'Result:'
        size_hint_y: None
        height: '40dp'
        font_size: '18sp'

    Button:
        text: 'Clear'
        size_hint_y: None
        height: '40dp'
        on_press:
            num1.text = ''
            num2.text = ''
            result.text = 'Result:'
'''

class CalcLayout(BoxLayout):
    def calculate(self, op):
        try:
            a = float(self.ids.num1.text)
            b = float(self.ids.num2.text)
        except:
            self.ids.result.text = 'Enter valid numbers'
            return

        if op == '+':
            res = a + b
        elif op == '-':
            res = a - b
        elif op == '*':
            res = a * b
        elif op == '/':
            if b == 0:
                self.ids.result.text = "Can't divide by zero"
                return
            res = a / b
        else:
            self.ids.result.text = 'Unknown op'
            return

        if float(res).is_integer():
            res = int(res)
        self.ids.result.text = 'Result: ' + str(res)

class CalculatorApp(App):
    def build(self):
        return Builder.load_string(KV)

if __name__ == '__main__':
    CalculatorApp().run()
