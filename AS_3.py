# Program Name: Assignment3.py
# Course: IT3883 SEC 01
# Student Name: Ria Reddy
# Due Date: 10/10/26
# Purpose: GUI for converting miles/gallon to kilometers/liter.




import tkinter as tk

#BASIC WINDOW
window = tk.Tk()
window.title("MPG to KM/L Converter")
window.geometry("350x200")



# USER INPUT BOX
mpg_label = tk.Label(window, text="Enter miles per gallon:")
mpg_label.pack(pady=10)

mpg_entry = tk.Entry(window)
mpg_entry.pack()




# DISPLAY
result_label = tk.Label(window, text="Result:")

#FORMAT CLEANLY
result_label.pack(pady=10)

# CALCULATION LOGIC
def convert_mpg(event):
    try:
        mpg = float(mpg_entry.get())
        result = mpg * 0.425143707

        #JUST ROUNDING FOR READABILITY/FUNCTIONALITY
        result_label.config(text=str(round(result, 2)) + " km/L")

    # AS3 REQ: Handling input other than number shouldn't make it crash
    except ValueError:
        result_label.config(text="Enter a number.")

#IMMEDIATE RESULT. AS3 REQ: Shouldn't need to press button
mpg_entry.bind("<KeyRelease>", convert_mpg)




# RUN! :D
window.mainloop()



