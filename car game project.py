import tkinter
from PIL import Image, ImageTk
import random
import csv

try:
    with open("highscore.csv", "r") as file:
        reader = csv.reader(file)
        data = list(reader)
        if data:
            lscore = [int(data[0][0])]
        else:
            lscore = [0]
except FileNotFoundError:
    lscore = [0]

root = tkinter.Tk()
root.geometry("1080x2400")
running = True
score = 0

canvas = tkinter.Canvas(root, width=1080, height=2400, bg='black')
canvas.pack(anchor=tkinter.CENTER, expand=True)

pyimg = tkinter.PhotoImage(file='/storage/emulated/0/Download/Racetrack.png')
canvas.create_image(540, 1098, image=pyimg)

img = Image.open("/storage/emulated/0/Download/jpg2png/20250805_203120.png")
rimg = img.resize((100, 200))
timg = ImageTk.PhotoImage(rimg)
player = canvas.create_image(540, 2096, image=timg)

enemy_img = Image.open("/storage/emulated/0/Download/jpg2png (1)/20250805_204937.png")
enemy_img = enemy_img.resize((100, 200))

lanes = [300, 540, 780,900,150]
start_y = [0, 500, 1000]
enemy_ids = []
enemy_images = []

for i in range(3):
    tk_enemy = ImageTk.PhotoImage(enemy_img)
    enemy_images.append(tk_enemy)
    enemy_id = canvas.create_image(lanes[i], start_y[i], image=tk_enemy)
    enemy_ids.append(enemy_id)

def left(event):
    coords = canvas.coords(player)
    if len(coords) == 2:
        x, y = coords
        if x > 100:
            canvas.move(player, -50, 0)

def right(event):
    coords = canvas.coords(player)
    if len(coords) == 2:
        x, y = coords
        if x < 980:
            canvas.move(player, 50, 0)

root.bind('<Left>', left)
root.bind('<Right>', right)

def move_enemies():
    global running
    if not running:
        return
    for enemy in enemy_ids:
        canvas.move(enemy, 0, 20)
        x, y = canvas.coords(enemy)
        if y >= 2400:
            Score()
            newlanes = random.choice(lanes)
            canvas.coords(enemy, newlanes, -100)
    collision()
    root.after(50, move_enemies)

def save_highscore():
    with open("highscore.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([lscore[0]])

def collision():
    p1 = canvas.bbox(player)
    for enemy in enemy_ids:
        e1 = canvas.bbox(enemy)
        if (p1[0] < e1[2] and p1[2] > e1[0] and 
            p1[1] < e1[3] and p1[3] > e1[1]):
            gameover()
            return

score_text = canvas.create_text(540, 100, text='score:0', fill='white', font=('Arial', 30))
hscore = canvas.create_text(540, 200, text=f'highest_score:{lscore[0]}', fill='white', font=('Arial', 20))

def Score():
    global score
    score += 1
    canvas.itemconfig(score_text, text=f'score:{score}')

def highestscore():
    global score
    if score > lscore[0]:
        lscore[0] = score
        save_highscore()
    canvas.itemconfig(hscore, text=f'highest_score:{lscore[0]}')

def gameover():
    global running
    running = False
    highestscore()
    canvas.config(bg='white')
    canvas.create_text(540, 1200, text='gameover', fill='black', font=('Arial', 20))
    canvas.delete(player)

move_enemies()
root.mainloop()