import image

# Open the image
img = image.Image("computer.jpg")
nWidth = img.getWidth()
nHeight = img.getHeight()

# Create a window to hold the image
win = image.ImageWin(nWidth, nHeight)

img.draw(win)
win.exitonclick()