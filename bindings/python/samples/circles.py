#!/usr/bin/env python
from samplebase import SampleBase
import math
import time


class circles(SampleBase):
    def __init__(self, *args, **kwargs):
        super(circles, self).__init__(*args, **kwargs)

    def all_circles(self):

        canvas = self.matrix.CreateFrameCanvas()

        while True:

            # theta = 0
            # height = 32
            # width = 32

            # led_active = 8
            # radius = 4.3
            # step = (2 * math.pi) / led_active

            # #--------------------------------------------------------- blue circle-----------------------------------------------------------#
            # for i in range(led_active):
                
            #     x = (radius * math.cos(theta)) + (width / 2)
            #     y = (radius * math.sin(theta)) + (height / 2)
            #     canvas.SetPixel(x, y, 0, 0, 255)
                
            #     theta += step
            
            # led_active = 8
            # radius = 8
            # step = (2 * math.pi) / led_active

            # #----------------------------------------------------------- green circle---------------------------------------------------------#
            # for i in range(led_active):
                
            #     x = (radius * math.cos(theta)) + (width / 2)
            #     y = (radius * math.sin(theta)) + (height / 2)
            #     canvas.SetPixel(x, y, 0, 255, 0)
                
            #     theta += step

            
            # led_active = 12
            # radius = 10
            # step = (2 * math.pi) / led_active

            # #------------------------------------------------------------ red circle----------------------------------------------------------#
            # for i in range(led_active):
                
            #     x = (radius * math.cos(theta)) + (width / 2)
            #     y = (radius * math.sin(theta)) + (height / 2)
            #     canvas.SetPixel(x, y, 255, 0, 0)
                
            #     theta += step

            # canvas.SetPixel(16, 16, 255, 255, 255)
            # canvas = self.matrix.SwapOnVSync(canvas)

            canvas.SetPixel(16, 16, 255, 0, 0)
            # # canvas.SetPixel(16, 17, 255, 255, 255)
            # # canvas.SetPixel(20, 20, 255, 255, 255)
            # # canvas.SetPixel(16, 19, 255, 255, 255)
            # # canvas.SetPixel(19, 20, 255, 255, 255)
            canvas = self.matrix.SwapOnVSync(canvas)

    def sequential(self, led_active, radius):

        # Initialise
        canvas = self.matrix.CreateFrameCanvas()
        theta = 0
        height = 32
        width = 32
        step = (2 * math.pi) / led_active

        # Setting colour values
        if(led_active == 12 and radius == 10):
            r = 255; g = 0; b = 0
        elif(led_active == 8 and radius == 8):
            r = 0; g = 255; b = 0
        elif(led_active == 8 and radius == 4.3):
            r = 0; g = 0; b = 255

        for i in range(led_active):
            
            # Calculate x, y coordinates from the center of the matrix
            x = (radius * math.cos(theta)) + (width / 2)
            y = (radius * math.sin(theta)) + (height / 2)

            # Set coordinates and colour, refresh after assignment
            canvas.SetPixel(x, y, r, g, b)
            canvas = self.matrix.SwapOnVSync(canvas)

            # Delay before clearing matrix
            time.sleep(1)
            canvas.Clear()
            
            # Increment angle
            theta += step
            
    def run(self):

        while True:
            # self.sequential(12, 10)
            # self.sequential(8, 8)
            # self.sequential(8, 4.3)

            self.all_circles()

# Main function
if __name__ == "__main__":

    circles = circles()
    if (not circles.process()):
        circles.print_help()
