import requests
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO

def get_random_dog_image():
    try:
        response = requests.get('https://dog.ceo/api/breeds/image/random')
        response.raise_for_status()
        data = response.json()
        return data['message']
    except requests.RequestException as e:
        messagebox.showerror("Ошибка", f"Ошибка при запросе к API: {e}")
        return None

def show_image():
    image_url = get_random_dog_image()

    if image_url:
        try:
            response = requests.get(image_url, stream=True)
            response.raise_for_status()
            img_data = BytesIO(response.content)
            img = Image.open(img_data)
            img.thumbnail((300, 300))
            img = ImageTk.PhotoImage(img)
            label.config(image=img)
            label.image = img

        except requests.RequestException as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить изображение: {e}")

    progress.stop()

def prog():
    progress['value'] = 0
    progress.start(30)
    window.after(3000, show_image)

window = Tk()
window.title("Случайное изображение пёсика")

label = ttk.Label()
label.pack(padx=10, pady=10)

button = ttk.Button(text="Показать случайного пёсика", command=prog)
button.pack(padx=10, pady=10)

progress = ttk.Progressbar(mode='determinate', length=300)
progress.pack(padx=10, pady=10)

window.mainloop()
