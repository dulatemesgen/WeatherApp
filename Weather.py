"""
Author: Dula Temesgen
Program: Tkinter GUI weather application

Enter the zip code or city of the place you want to find the weather for followed by the two digit country code
for example Des Moines Iowa would be Des Moines, US or 50321, US.
"""



import tkinter as tk
from tkinter import font
import requests

HEIGHT = 500
WIDTH = 600

def test_function(entry):
    print("This is the entry:", entry)
#8e9ce59012f49914d3746623c1daedaa
#api.openweathermap.org/data/2.5/forecast?q={city name},{state code},{country code}&appid={API key}

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperature (℉): %s' % (name, desc, temp)
    except:
        final_str = 'There Was a problem with your input'
    return final_str

def get_weather(city):
    weather_key = '8e9ce59012f49914d3746623c1daedaa'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)

    

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='weather.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)


frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('modern', 30))
label.place( relwidth=1, relheight=1)



root.mainloop()


