import math
import time
from tkinter import *


class Stopwatch(Frame):
    def __init__(self, root, width, height):
        super().__init__()
        self.start_time = 0
        self.time = 0
        self.time_counted = 0
        self.started = False
        self.milliseconds_line_len = (width + height) / 6
        self.seconds_line_len = (width + height) / 8
        self.minutes_line_len = (width + height) / 12
        self.x = width / 2
        self.y = height / 2
        self.canvas = Canvas(self)
        self.master.title("Stopwatch")
        self.pack(fill=BOTH, expand=1)
        self.milliseconds_line = self.canvas.create_line(self.x, self.y, self.x, self.y - self.milliseconds_line_len)
        self.seconds_line = self.canvas.create_line(self.x, self.y, self.x, self.y - self.seconds_line_len)
        self.minutes_line = self.canvas.create_line(self.x, self.y, self.x, self.y - self.minutes_line_len)
        self.button_frame = Frame(root)
        self.button_frame.pack(fill=BOTH, side=BOTTOM)
        self.reset_button = Button(self.button_frame, text="Reset", command=self.reset)
        self.button = Button(self.button_frame, text="Start", command=self.start)
        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=1)
        self.reset_button.grid(row=0, column=0, sticky=W + E)
        self.button.grid(row=0, column=1, sticky=W + E)
        self.init_clock_face()

    def init_clock_face(self):
        self.canvas.create_oval(self.x - self.milliseconds_line_len - 30, self.y + self.milliseconds_line_len + 30,
                                self.x + self.milliseconds_line_len + 30,
                                self.y - self.milliseconds_line_len - 30)
        for i in range(0, 60, 5):
            angle_in_radians = (360 * ((i + 45) % 60 / 60)) * math.pi / 180
            self.canvas.create_text(round(self.x + (self.milliseconds_line_len + 20) * math.cos(angle_in_radians)),
                                    round(self.y + (self.milliseconds_line_len + 20) * math.sin(angle_in_radians)),
                                    fill="black",
                                    text=str(i))
        self.canvas.pack(fill=BOTH, expand=1)

    def clock_update(self):
        if self.started:
            self.time = round((time.time() - self.start_time) * 1000) + self.time_counted
            milliseconds_angle_in_radians = (360 * ((self.time + 750) % 1000 / 1000)) * math.pi / 180
            self.canvas.delete(self.milliseconds_line, self.seconds_line, self.minutes_line)
            self.milliseconds_line = self.canvas.create_line(self.x, self.y,
                                                             round(self.x + self.milliseconds_line_len * math.cos(
                                                                 milliseconds_angle_in_radians)),
                                                             round(self.y + self.milliseconds_line_len * math.sin(
                                                                 milliseconds_angle_in_radians)))
            seconds_angle_in_radians = (360 * ((self.time / 1000 + 45) % 60 / 60)) * math.pi / 180
            self.seconds_line = self.canvas.create_line(self.x, self.y,
                                                        round(self.x + self.seconds_line_len * math.cos(
                                                            seconds_angle_in_radians)),
                                                        round(self.y + self.seconds_line_len * math.sin(
                                                            seconds_angle_in_radians)))
            minutes_angle_in_radians = (360 * ((self.time / 60000 + 45) % 60 / 60)) * math.pi / 180
            self.minutes_line = self.canvas.create_line(self.x, self.y,
                                                        round(self.x + self.minutes_line_len * math.cos(
                                                            minutes_angle_in_radians)),
                                                        round(self.y + self.minutes_line_len * math.sin(
                                                            minutes_angle_in_radians)))
            self.after(1, self.clock_update)

    def start(self):
        if not self.started:
            self.start_time = time.time()
            self.started = True
            self.button.destroy()
            self.button = Button(self.button_frame, text="Stop", command=self.stop)
            self.button.grid(row=0, column=1, sticky=W + E)
            self.clock_update()

    def stop(self):
        self.started = False
        self.time_counted = self.time
        self.button.destroy()
        self.button = Button(self.button_frame, text="Start", command=self.start)
        self.button.grid(row=0, column=1, sticky=W + E)

    def reset(self):
        self.started = False
        self.time_counted = 0
        self.canvas.delete(self.milliseconds_line, self.seconds_line, self.minutes_line)
        self.milliseconds_line = self.canvas.create_line(self.x, self.y, self.x, self.y - self.milliseconds_line_len)
        self.seconds_line = self.canvas.create_line(self.x, self.y, self.x, self.y - self.seconds_line_len)
        self.minutes_line = self.canvas.create_line(self.x, self.y, self.x, self.y - self.minutes_line_len)
        self.button.destroy()
        self.button = Button(self.button_frame, text="Start", command=self.start)
        self.button.grid(row=0, column=1, sticky=W + E)


def main():
    width = 500
    height = 500

    root = Tk()
    stopwatch = Stopwatch(root, width, height)
    root.geometry(str(width) + "x" + str(height))
    root.mainloop()


if __name__ == '__main__':
    main()
