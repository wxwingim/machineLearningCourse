# var 8
import os

from PIL import Image


def main():
    image = Image.open('/Volumes/data/workspace/Python/machineLearningCource/pract8/composition7.jpg')
    image.show()

    image_rot = image.rotate(180)
    image_rot.show()

if __name__ == '__main__':
    main()