from math import sqrt

from PIL import Image, ImageDraw


def iphone15():
    width = 1179
    height = 2556

    image = Image.new("RGB", (width, height), (0, 0, 0))
    draw = ImageDraw.Draw(image)

    dots_x = 23
    dots_y = 50

    for i in range(1, dots_x):
        for j in range(1, dots_y):
            x = i * width / dots_x
            y = j * height / dots_y

            rel_x = width / 2 - x
            rel_y = height / 2 - y

            off_x = 0
            off_y = 100
            rad_x = 1750
            rad_y = 1250

            # This is the ellipse formula. The goal is to center and offset the ellipse, then
            # calculate how far the point is from the center of the ellipse, using the increasing
            # distance as the dot fade color.
            dist = sqrt(((rel_x + off_x) / rad_x) ** 2 + ((rel_y + off_y) / rad_y) ** 2)

            dot_rad = 2
            dot_col = int(90 * max(0, 1 - dist))

            draw.circle((x, y), radius=dot_rad, fill=(dot_col, dot_col, dot_col))

    image.save("iphone15.png")


def main():
    iphone15()


if __name__ == "__main__":
    main()
