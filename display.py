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

# Create grid layout
frame1.grid(row=0, column=0, padx=0, pady=20, columnspan=2)  # Span whole grid
frame2.grid(row=1, column=0, padx=0, pady=20)
frame3.grid(row=1, column=1, padx=0, pady=20)

# Filler label
label1 = ctk.CTkLabel(
    master=frame1,
    text="This is a label",
    font=("Helvetica", 20),
)
label1.pack(pady=10,padx=275)    # Padding from frame to text

# Current Temperature label
label2 = ctk.CTkLabel(
    master=frame2, 
    text="The current temperature is: " + currentTemp.returnCTempAsFStr() + " °F", 
    font=("Helvetica", 20)
)
label2.pack(pady=10, padx=50)   # Padding from frame top to text

# Low Temperature label
label3 = ctk.CTkLabel(
    master=frame3, 
    text="The low temperature is: " + lowTemp.returnCTempAsFStr() + " °F", 
    font=("Helvetica", 20)
)
label3.pack(pady=10, padx=50)   # Padding from frame top to text

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


display_location()
display_skyCond()
display_temp()
display_humidity()
display_wind()
#display_vis()