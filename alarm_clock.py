#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

from colored import stylize, fg
import tkinter, math, time, beepy

# decoration
print(stylize("\n---- | Alarm Clock with tkinter | ----\n", fg("red")))

# functions
def countdown(count):
    seconds = math.floor(count % 60)
    minutes = math.floor((count / 60) % 60)
    hours = math.floor((count / 3600))
    label["text"] = f"Hours: {str(hours)} Minutes: {str(minutes)} Seconds: {str(seconds)}"

    if count >= 0:
        main.after(1000, countdown, count - 1)
    else:
        for _ in range(3):
            beepy.beep(sound=1)
        label["text"] = "Time is up!"

def updateButton():
    hours, minutes, seconds = hoursE.get(), minuteE.get(), secondE.get()
    if hours.isdigit() and minutes.isdigit() and seconds.isdigit():
        time = int(hours) * 3600 + int(minutes) * 60 + int(seconds)
        countdown(time)

# tkinter window
main = tkinter.Tk()
main.title("Alarm Clock")
main.geometry("325x150")

hoursT = tkinter.Label(main, text="Hours:")
hoursE = tkinter.Entry(main)
minuteT = tkinter.Label(main, text="Minutes:")
minuteE = tkinter.Entry(main)
secondT = tkinter.Label(main, text="Seconds:")
secondE = tkinter.Entry(main)

hoursT.grid(row=1,column=1)
hoursE.grid(row=1,column=2)
minuteT.grid(row=2,column=1)
minuteE.grid(row=2,column=2)
secondT.grid(row=3,column=1)
secondE.grid(row=3,column=2)

label = tkinter.Label(main)
label.grid(row=5,column=2)

button = tkinter.Button(main, text="Start Timer", command=updateButton)
button.grid(row=4, column=2)

main.mainloop()
