from pystray import Icon as icon, Menu as menu, MenuItem as item
from PIL import Image, ImageDraw


state = False

def on_clicked(icon, item):
    global state
    state = not item.checked

def create_image(width, height, color1, color2):
    # Generate an image and draw a pattern
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2, 0, width, height // 2),
        fill=color2)
    dc.rectangle(
        (0, height // 2, width // 2, height),
        fill=color2)

    return image

icon('test', create_image(64, 64, 'black', 'white'), menu=menu(
    item(
        'Checkable',
        on_clicked,
        checked=lambda item: state))).run()

# icon('test', create_image(64, 64, 'black', 'white'), menu=menu(
#     item(
#         'With submenu',
#         menu(
#             item(
#                 'Show message',
#                 lambda icon, item: icon.notify('Hello World!')),
#             item(
#                 'Submenu item 2',
#                 lambda icon, item: icon.remove_notification()))))).run()