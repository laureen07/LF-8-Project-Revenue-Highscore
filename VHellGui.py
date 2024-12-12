from tkinter import *
import numpy as np
import pygame

def create_heart():
    # Anzahl der Fenster
    n_windows = 60
    # Herzform-Koordinaten
    t = np.linspace(0, 2 * np.pi, n_windows)
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

    # Koordinaten skalieren, um auf den Bildschirm zu passen
    x_scaled = (x * 25) + 650  # Verschiebung und Skalierung in x-Richtung
    y_scaled = (y * -25) + 300  # Verschiebung und Skalierung in y-Richtung (invertiert)

    for i in range(0,60): #60
            a = Toplevel()
            a.title('Merry X-Mas')
            a.configure(background='red')
            a.geometry(f"250x150+{int(x_scaled[i])}+{int(y_scaled[i])}")

def play_song():
    pygame.mixer.init()
    pygame.mixer.music.load('Songs/WeihnachtsSong1.mp3')
    pygame.mixer.music.play()
