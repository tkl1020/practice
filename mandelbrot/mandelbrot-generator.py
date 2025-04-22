import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Define Mandelbrot generator
def mandelbrot(width, height, zoom, x_offset, y_offset, max_iter):
    xmin = -2.0 / zoom + x_offset
    xmax = 1.0 / zoom + x_offset
    ymin = -1.5 / zoom + y_offset
    ymax = 1.5 / zoom + y_offset

    image = np.zeros((height, width))

    for row in range(height):
        for col in range(width):
            x = xmin + (xmax - xmin) * col / width
            y = ymin + (ymax - ymin) * row / height
            c = complex(x, y)

            z = 0
            iterations = 0

            while abs(z) <= 2 and iterations < max_iter:
                z = z * z + c
                iterations += 1

            image[row, col] = iterations
    return image

# Image dimensions
width, height = 600, 600

# Initial parameters
zoom_init = 1
x_offset_init = 0
y_offset_init = 0
max_iter_init = 50

# Create initial Mandelbrot image
image_data = mandelbrot(width, height, zoom_init, x_offset_init, y_offset_init, max_iter_init)

# Set up figure
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.35)
fractal = ax.imshow(image_data, cmap='inferno', extent=(-2, 1, -1.5, 1.5))
ax.set_title("Mandelbrot Explorer")

# Sliders
ax_zoom = plt.axes([0.1, 0.25, 0.8, 0.03])
ax_x = plt.axes([0.1, 0.20, 0.8, 0.03])
ax_y = plt.axes([0.1, 0.15, 0.8, 0.03])
ax_iter = plt.axes([0.1, 0.10, 0.8, 0.03])

s_zoom = Slider(ax_zoom, 'Zoom', 1, 100, valinit=zoom_init)
s_x = Slider(ax_x, 'X Offset', -2.0, 2.0, valinit=x_offset_init)
s_y = Slider(ax_y, 'Y Offset', -2.0, 2.0, valinit=y_offset_init)
s_iter = Slider(ax_iter, 'Iterations', 10, 200, valinit=max_iter_init, valstep=1)

# Update function
def update(val):
    zoom = s_zoom.val
    x_offset = s_x.val
    y_offset = s_y.val
    max_iter = s_iter.val

    new_data = mandelbrot(width, height, zoom, x_offset, y_offset, int(max_iter))
    fractal.set_data(new_data)
    fig.canvas.draw_idle()

# Connect sliders to update function
s_zoom.on_changed(update)
s_x.on_changed(update)
s_y.on_changed(update)
s_iter.on_changed(update)

plt.show()
