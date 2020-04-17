from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.button import Button

import cv2

class CamApp(App):

    def build(self):
        btn = Button(text="DETECT DROWSINESS",
                     font_size="12sp",
                     background_color=(1, 1, 1, 1),
                     color=(1, 1, 1, 1),
                     size=(20, 32),
                     size_hint=(.2, .1),
                     pos=(300, 270))

        # bind() use to bind the button to function callback
        btn.bind(on_press=self.update)
        return btn

    def update(self, event):
            # display image from cam in opencv window
            capture = cv2.VideoCapture(0)

            while True:
                ret, frame = capture.read()
                cv2.namedWindow('CV2 Image', cv2.WND_PROP_FULLSCREEN)
                cv2.imshow("CV2 Image", frame)

                cv2.setWindowProperty('CV2 Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                # convert it to texture
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cv2.destroyWindow('CV2 Image')



if __name__ == '__main__':
    CamApp().run()
