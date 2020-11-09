import math
import time
from tkinter import *


class Stopwatch(Frame):
    def __init__(self, root):
        super().__init__()
        self.height = 400
        self.width = 400
        self.start_time = 0
        self.time = 0
        self.time_counted = 0
        self.highest = 0
        self.lowest = 0
        self.started = False
        self.recent_scores = [0, 0, 0, 0, 0]
        self.milliseconds_line_len = self.height / 3
        self.seconds_line_len = self.height / 4
        self.minutes_line_len = self.height / 6
        self.x = self.width / 2
        self.y = self.height / 2
        self.canvas = Canvas(self)
        self.master.title("Stopwatch")
        self.pack(fill=BOTH, expand=1)
        self.best_score_text = self.canvas.create_text(self.width - 200, 100)
        self.worst_score_text = self.canvas.create_text(self.width - 200, 200)
        self.recent1 = self.canvas.create_text(self.x * 3, self.height + 120)
        self.recent2 = self.canvas.create_text(self.x * 3, self.height + 140)
        self.recent3 = self.canvas.create_text(self.x * 3, self.height + 160)
        self.recent4 = self.canvas.create_text(self.x * 3, self.height + 180)
        self.recent5 = self.canvas.create_text(self.x * 3, self.height + 200)
        self.stopwatch_text = self.canvas.create_text(self.width * 2, 50)
        self.clock_text = self.canvas.create_text(self.width * 2, self.height * 2 + 50)
        self.stopwatch_milliseconds_line = self.canvas.create_line(self.x, self.y, self.x,
                                                                   self.y - self.milliseconds_line_len)
        self.stopwatch_seconds_line = self.canvas.create_line(self.x, self.y, self.x, self.y - self.seconds_line_len)
        self.stopwatch_minutes_line = self.canvas.create_line(self.x, self.y, self.x, self.y - self.minutes_line_len)
        self.clock_seconds_line = self.canvas.create_line(self.x * 3, self.y, self.x * 3,
                                                          self.y - self.milliseconds_line_len)
        self.clock_minutes_line = self.canvas.create_line(self.x * 3, self.y, self.x * 3,
                                                          self.y - self.seconds_line_len)
        self.clock_hours_line = self.canvas.create_line(self.x * 3, self.y, self.x * 3, self.y - self.minutes_line_len)
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
        self.canvas.create_oval(self.x * 3 - self.milliseconds_line_len - 30, self.y + self.milliseconds_line_len + 30,
                                self.x * 3 + self.milliseconds_line_len + 30,
                                self.y - self.milliseconds_line_len - 30)
        for i in range(0, 60, 5):
            angle_in_radians = (360 * ((i + 45) % 60 / 60)) * math.pi / 180
            self.canvas.create_text(round(self.x + (self.milliseconds_line_len + 20) * math.cos(angle_in_radians)),
                                    round(self.y + (self.milliseconds_line_len + 20) * math.sin(angle_in_radians)),
                                    fill="black",
                                    text=str(i))
        for i in range(0, 12):
            angle_in_radians = 360 * ((i + 10) / 12) * math.pi / 180
            self.canvas.create_text(round(self.x * 3 + (self.milliseconds_line_len + 20) * math.cos(angle_in_radians)),
                                    round(self.y + (self.milliseconds_line_len + 20) * math.sin(angle_in_radians)),
                                    fill="black",
                                    text=str(i + 1))

        self.canvas.create_text(self.x * 2, self.height + 100, fill="black", text="Best score:")
        self.canvas.create_text(self.x * 2, self.height + 150, fill="black", text="Worst score:")
        self.canvas.create_text(self.x * 3, self.height + 100, fill="black", text="Recent score:")

        self.canvas.pack(fill=BOTH, expand=1)
        self.clock_update()

    def clock_update(self):
        self.canvas.delete(self.clock_seconds_line, self.clock_minutes_line,
                           self.clock_hours_line, self.clock_text)
        seconds_angle_in_radians = 360 * ((time.time() + 45) % 60 / 60) * math.pi / 180
        self.clock_seconds_line = self.canvas.create_line(self.x * 3, self.y,
                                                          round(self.x * 3 + self.milliseconds_line_len * math.cos(
                                                              seconds_angle_in_radians)),
                                                          round(self.y + self.milliseconds_line_len * math.sin(
                                                              seconds_angle_in_radians)))
        minutes_angle_in_radians = (360 * (((time.time() + 2700) % 3600) / 3600)) * math.pi / 180
        self.clock_minutes_line = self.canvas.create_line(self.x * 3, self.y,
                                                          round(self.x * 3 + self.seconds_line_len * math.cos(
                                                              minutes_angle_in_radians)),
                                                          round(self.y + self.seconds_line_len * math.sin(
                                                              minutes_angle_in_radians)))
        hours_angle_in_radians = (360 * (((time.time() + 36000) % 43200) / 43200)) * math.pi / 180
        self.clock_hours_line = self.canvas.create_line(self.x * 3, self.y,
                                                        round(self.x * 3 + self.minutes_line_len * math.cos(
                                                            hours_angle_in_radians)),
                                                        round(self.y + self.minutes_line_len * math.sin(
                                                            hours_angle_in_radians)))
        self.clock_text = self.canvas.create_text(self.height * 1.5, self.width + 50, fill="black",
                                                  text=time.strftime('%H:%M:%S %p'))
        self.after(1000, self.clock_update)

    def stopwatch_update(self):
        if self.started:
            self.time = round((time.time() - self.start_time) * 1000) + self.time_counted
            milliseconds_angle_in_radians = (360 * ((self.time + 750) % 1000 / 1000)) * math.pi / 180
            self.canvas.delete(self.stopwatch_milliseconds_line, self.stopwatch_seconds_line,
                               self.stopwatch_minutes_line, self.stopwatch_text)
            self.stopwatch_milliseconds_line = self.canvas.create_line(self.x, self.y,
                                                                       round(
                                                                           self.x + self.milliseconds_line_len * math.cos(
                                                                               milliseconds_angle_in_radians)),
                                                                       round(
                                                                           self.y + self.milliseconds_line_len * math.sin(
                                                                               milliseconds_angle_in_radians)))
            seconds_angle_in_radians = (360 * ((self.time / 1000 + 45) % 60 / 60)) * math.pi / 180
            self.stopwatch_seconds_line = self.canvas.create_line(self.x, self.y,
                                                                  round(self.x + self.seconds_line_len * math.cos(
                                                                      seconds_angle_in_radians)),
                                                                  round(self.y + self.seconds_line_len * math.sin(
                                                                      seconds_angle_in_radians)))
            minutes_angle_in_radians = (360 * ((self.time / 60000 + 45) % 60 / 60)) * math.pi / 180
            self.stopwatch_minutes_line = self.canvas.create_line(self.x, self.y,
                                                                  round(self.x + self.minutes_line_len * math.cos(
                                                                      minutes_angle_in_radians)),
                                                                  round(self.y + self.minutes_line_len * math.sin(
                                                                      minutes_angle_in_radians)))

            self.stopwatch_text = self.canvas.create_text(self.width * 0.5, self.height + 50, fill="black",
                                                          text=str(self.time // 1000 // 60) + " m " + str(
                                                              self.time // 1000 % 60) + " s " + str(
                                                              self.time % 1000) + " ms")

            self.after(1, self.stopwatch_update)

    def start(self):
        if not self.started:
            self.start_time = time.time()
            self.started = True
            self.button.destroy()
            self.button = Button(self.button_frame, text="Stop", command=self.stop)
            self.button.grid(row=0, column=1, sticky=W + E)
            self.stopwatch_update()

    def stop(self):
        self.started = False
        self.time_counted = self.time
        self.button.destroy()
        self.button = Button(self.button_frame, text="Start", command=self.start)
        self.button.grid(row=0, column=1, sticky=W + E)

    def reset(self):
        self.started = False
        if self.time > self.highest:
            self.highest = self.time
        elif self.lowest == 0:
            self.lowest = self.time
        elif self.lowest > self.time > 0:
            self.lowest = self.time

        if self.time != 0:
            self.recent_scores.append(self.time)
            del self.recent_scores[0]

        self.canvas.itemconfig(self.recent1, text=str(self.recent_scores[4] // 1000 // 60) + " m " + str(
                                                              self.recent_scores[4] // 1000 % 60) + " s " + str(
                                                              self.recent_scores[4] % 1000) + " ms")
        self.canvas.itemconfig(self.recent2, text=str(self.recent_scores[3] // 1000 // 60) + " m " + str(
                                                              self.recent_scores[3] // 1000 % 60) + " s " + str(
                                                              self.recent_scores[3] % 1000) + " ms")
        self.canvas.itemconfig(self.recent3, text=str(self.recent_scores[2] // 1000 // 60) + " m " + str(
                                                              self.recent_scores[2] // 1000 % 60) + " s " + str(
                                                              self.recent_scores[2] % 1000) + " ms")
        self.canvas.itemconfig(self.recent4, text=str(self.recent_scores[1] // 1000 // 60) + " m " + str(
                                                              self.recent_scores[1] // 1000 % 60) + " s " + str(
                                                              self.recent_scores[1] % 1000) + " ms")
        self.canvas.itemconfig(self.recent5, text=str(self.recent_scores[0] // 1000 // 60) + " m " + str(
                                                              self.recent_scores[0] // 1000 % 60) + " s " + str(
                                                              self.recent_scores[0] % 1000) + " ms")

        self.time_counted = 0
        self.time = 0

        self.canvas.delete(self.stopwatch_milliseconds_line, self.stopwatch_seconds_line, self.stopwatch_minutes_line,
                           self.best_score_text,
                           self.worst_score_text, self.stopwatch_text)
        self.stopwatch_milliseconds_line = self.canvas.create_line(self.x, self.y, self.x,
                                                                   self.y - self.milliseconds_line_len)
        self.stopwatch_seconds_line = self.canvas.create_line(self.x, self.y, self.x, self.y - self.seconds_line_len)
        self.stopwatch_minutes_line = self.canvas.create_line(self.x, self.y, self.x, self.y - self.minutes_line_len)
        self.best_score_text = self.canvas.create_text(self.x * 2, self.height + 120, fill="black",
                                                       text=str(self.lowest / 1000))
        self.worst_score_text = self.canvas.create_text(self.x * 2, self.height + 170, fill="black",
                                                        text=str(self.highest / 1000))
        self.stopwatch_text = self.canvas.create_text(self.width * 0.5, self.height + 50, fill="black",
                                                      text="0 m 0 s 0 ms")
        self.button.destroy()
        self.button = Button(self.button_frame, text="Start", command=self.start)
        self.button.grid(row=0, column=1, sticky=W + E)


def main():
    width = 800
    height = 700

    root = Tk()
    stopwatch = Stopwatch(root)
    root.geometry(str(width) + "x" + str(height))
    root.mainloop()


if __name__ == '__main__':
    main()
