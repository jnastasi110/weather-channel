from weather_channel import *
import customtkinter as ctk

reload()

# Set appearance mode and default color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Create the main window
app = ctk.CTk()
app.title("Weather Channel")
app.geometry("800x400")
app.grid_columnconfigure((0,1), weight=1)    # Centers the grid

def close_window(event=None):
        app.destroy()

app.wm_attributes('-fullscreen', True)
app.bind("<Escape>", close_window)

# Create frame
frame1 = ctk.CTkFrame(
    master=app,
    width=100,
    height=100,
    corner_radius=50,
    border_width=3
)
frame2 = ctk.CTkFrame(
    master=app,
    width=100,
    height=100,
    corner_radius=50,
    border_width=3
)
frame3 = ctk.CTkFrame(
    master=app,
    width=100,
    height=100,
    corner_radius=50,
    border_width=3
)
frame4 = ctk.CTkFrame(
    master=app,
    width=100,
    height=100,
    corner_radius=50,
    border_width=3
)
frame5 = ctk.CTkFrame(
    master=app,
    width=100,
    height=100,
    corner_radius=50,
    border_width=3
)
frame6 = ctk.CTkFrame(
    master=app,
    width=100,
    height=100,
    corner_radius=50,
    border_width=3
)
frame7 = ctk.CTkFrame(
    master=app,
    width=100,
    height=100,
    corner_radius=50,
    border_width=3
)
frame8 = ctk.CTkFrame(
    master=app,
    width=100,
    height=100,
    corner_radius=50,
    border_width=3
)

# Create grid layout
frame1.grid(row=0, column=0, padx=0, pady=20, columnspan=2)  # Span whole grid
frame2.grid(row=1, column=0, padx=0, pady=20)
frame3.grid(row=1, column=1, padx=0, pady=20)
frame4.grid(row=2, column=0, padx=0, pady=20)
frame5.grid(row=2, column=1, padx=0, pady=20)
frame6.grid(row=3, column=0, padx=0, pady=20)
frame7.grid(row=3, column=1, padx=0, pady=20)
frame8.grid(row=4, column=0, padx=0, pady=20, columnspan=2)

# Filler label
label1 = ctk.CTkLabel(
    master=frame1,
    text="Location: " + latCurrent.returnCoordAsStr() + ", " + longCurrent.returnCoordAsStr(),
    font=("Helvetica", 50),
)
label1.pack(pady=10,padx=275)    # Padding from frame to text

# Current Temperature label
label2 = ctk.CTkLabel(
    master=frame2, 
    text="Current: " + currentTemp.returnCTempAsFStr() + " °F", 
    font=("Helvetica", 20)
)
label2.pack(pady=10, padx=50)   # Padding from frame top to text

# Low Temperature label
label3 = ctk.CTkLabel(
    master=frame3, 
    text="Feels Like: " + feelsLike.returnCTempAsFStr() + " °F", 
    font=("Helvetica", 20)
)
label3.pack(pady=10, padx=50)   # Padding from frame top to text

label4 = ctk.CTkLabel(
    master=frame4,
    text="Low: " + lowTemp.returnCTempAsFStr() + " °F",
    font=("Helvetica", 20),
)
label4.pack(pady=10,padx=275) 

label5 = ctk.CTkLabel(
    master=frame5,
    text="High: " + highTemp.returnCTempAsFStr() + " °F",
    font=("Helvetica", 20),
)
label5.pack(pady=10,padx=275) 

label6 = ctk.CTkLabel(
    master=frame6,
    text="Humidity: " + str(round(humidity.value1)) + "%",
    font=("Helvetica", 20),
)
label6.pack(pady=10,padx=275) 

label7 = ctk.CTkLabel(
    master=frame7,
    text="Wind: " + str(windDirection.value1) + " at " + str(round(windSpeed.value1 / 1.609)) + " mph gusting " + str(round(windGust.value1 / 1.609)) + " mph",
    font=("Helvetica", 20),
)
label7.pack(pady=10,padx=175) 

label8 = ctk.CTkLabel(
    master=frame8,
    text="Sky cover: " + skyCond.convertSkyCond(),
    font=("Helvetica", 20),
)
label8.pack(pady=10,padx=175)

# Run the application
app.mainloop()

##################################################

def display_location():
  print(latCurrent.returnCoordAsStr() + ", " + longCurrent.returnCoordAsStr())

def display_skyCond():
  print(skyCond.convertSkyCond())

def display_temp():
  print("Temperature: " + currentTemp.returnCTempAsFStr() + " °F")
  print("Low : " + lowTemp.returnCTempAsFStr() + " °F")
  print("High: " + highTemp.returnCTempAsFStr() + " °F")
  print("Feels like: " + feelsLike.returnCTempAsFStr() + " °F")

def display_humidity():
  print("Humidity: " + str(round(humidity.value1)) + "%")

def display_wind():
  print("Wind: " + str(windDirection.value1) + " at " + str(round(windSpeed.value1 / 1.609)) + " mph gusting " + str(round(windGust.value1 / 1.609)) + " mph")


#display_location()
#display_skyCond()
#display_temp()
#display_humidity()
#display_wind()
#display_vis()