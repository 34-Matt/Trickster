from PIL import Image, ImageDraw

def drawProgressBar2(progress):
    out = Image.new("RGBA", (120, 50), (255, 255, 255, 0))
    d = ImageDraw.Draw(out)
    x = 10
    y = 10
    w = 100
    h = 30
    bg="red"
    fg="green"

    # draw background
    d.ellipse((x+w, y, x+h+w, y+h), fill=bg)
    d.ellipse((x, y, x+h, y+h), fill=bg)
    d.rectangle((x+(h/2), y, x+w+(h/2), y+h), fill=bg)

    # draw progress bar
    w *= progress
    d.ellipse((x+w, y, x+h+w, y+h),fill=fg)
    d.ellipse((x, y, x+h, y+h),fill=fg)
    d.rectangle((x+(h/2), y, x+w+(h/2), y+h),fill=fg)

    return out, d
