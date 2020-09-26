import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class CalcGrid (GridLayout):
    def equal(self, calculation):
        
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "error"

class CalcApp(App):
    def build(self):
        return CalcGrid()

calculatorApp = CalcApp()
calculatorApp.run()