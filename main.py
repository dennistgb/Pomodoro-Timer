from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    window.after_cancel(timer)
    heading.config(text="Timer")
    check_marks.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 > 0:
        count_down(work_sec)
        heading.config(text="Work", fg=GREEN)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        heading.config(text="Break", fg=PINK)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        heading.config(text="Break", fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 0:
        count_sec = f"0{count_sec}"
    elif count_sec == 0:
        count_sec = "00"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✅"
        check_marks.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=False)
img = PhotoImage(file="tomato.png")
canvas.create_image(99.5, 112, image=img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
heading = Label(window, text= "Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
start = Button(text="START", highlightthickness=0, command=start_timer)
reset = Button(text="RESET", highlightthickness=0, command=reset_timer)


check_marks = Label(text="✅")
check_marks.grid(column=2, row=3)
check_marks.config(padx=10, pady=20, bg=YELLOW)

heading.grid(row=1, column=2)
start.grid(row=3, column=1)
reset.grid(row=3, column=3)
canvas.grid(row=2, column=2)

window.mainloop()
