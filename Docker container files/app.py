from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    'https://iso.500px.com/wp-content/uploads/2016/04/stock-photo-150595123-1500x1000.jpg',
    "https://assets.hongkiat.com/uploads/100-absolutely-beautiful-nature-wallpapers-for-your-desktop/blue-sea-sunset.jpg",
    "https://www.lovethispic.com/uploaded_images/153035-Beautiful-Winter-Night.jpg",
    "https://image.shutterstock.com/image-photo/summer-background-flowers-nature-beautiful-260nw-1038824167.jpg",
    "https://images.alphacoders.com/789/789452.jpg",
    "https://images8.alphacoders.com/807/807641.png",
    "https://images6.alphacoders.com/897/897151.jpg",
    "https://images2.alphacoders.com/100/1008096.png",
    "https://images7.alphacoders.com/100/1003512.jpg",
    "https://c4.wallpaperflare.com/wallpaper/180/757/252/computer-desktop-full-screen-nature-pics-1920x1200-wallpaper-preview.jpg", 
    "https://c4.wallpaperflare.com/wallpaper/626/589/82/greens-leaves-trees-branches-wallpaper-preview.jpg"
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
