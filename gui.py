import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageDraw, ImageOps
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model('tom.keras')

window = tk.Tk()
window.title("Handwritten Digit Recognition")

canvas = Canvas(window, width=200, height=200, bg="white")
canvas.pack()

image = Image.new("L", (200, 200), color=255)
draw = ImageDraw.Draw(image)

def start_draw(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def draw_digit(event):
    global last_x, last_y
    x, y = event.x, event.y
    canvas.create_line((last_x, last_y, x, y), fill="black", width=8)
    draw.line((last_x, last_y, x, y), fill="black", width=8)
    last_x, last_y = x, y

canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw_digit)

def predict_digit():
    img = image.resize((28, 28))
    img = ImageOps.invert(img)
    img = np.array(img).reshape(1, 28, 28, 1).astype("float32") / 255.0
    prediction = model.predict(img)
    digit = np.argmax(prediction)
    label.config(text=f"Prediction: {digit}")

def clear_canvas():
    canvas.delete("all")
    draw.rectangle([0, 0, 200, 200], fill="white")

predict_button = tk.Button(window, text="Predict", command=predict_digit)
predict_button.pack()

clear_button = tk.Button(window, text="Clear", command=clear_canvas)
clear_button.pack()

label = tk.Label(window, text="Prediction: None", font=("Helvetica", 16))
label.pack()

window.mainloop()
