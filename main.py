'''Measures the
time between two taps on the screen and estimates the tap rate in Hz.

'''
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
import time
  

class TouchRateCalc(Widget):
    
    inter_touch_interval = NumericProperty(0)
    start_t = time.time()
    tap_rate = NumericProperty(0)
    max_tap_rate = NumericProperty(0)
    
    def on_touch_down(self, touch):
        self.touch_t = time.time()
        self.inter_touch_interval = self.touch_t - self.start_t
        self.start_t = time.time()
        self.tap_rate = round(1.0/self.inter_touch_interval,2)
        self.update_maxtap_rate(self.tap_rate)
    
    def update_maxtap_rate(self, current_rate):
        if current_rate >= self.max_tap_rate:
            self.max_tap_rate = float(current_rate)
       

class TouchRateApp(App):
    def build(self): 

        return TouchRateCalc()


if __name__ == '__main__':
    TouchRateApp().run()