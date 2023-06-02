import base64
import os

from app.logs.app_logger import Logger


logger = Logger(__name__)

# get the absolute path of the current script
abs_path = os.path.abspath(__file__)


def get_picture(name):

    # go up two directories to get to the root directory of your project
    root_path = os.path.dirname(abs_path)

    # construct the path to your image file
    img_path = os.path.join(root_path, "pictures", name + ".png")

    # open the file and read its contents
    with open(img_path, "rb") as f:
        image = f.read()

    # encode the image as base64 and return a data URI
    return 'data:image/png;base64,' + base64.b64encode(image).decode('utf-8')
