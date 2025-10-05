from math import sqrt

from PIL import Image, ImageDraw


def main():
    w = 1179
    h = 2556

    im = Image.new("RGB", (w, h), (0, 0, 0))
    d = ImageDraw.Draw(im)

    cx = 23
    cy = 50
    for i in range(1, cx):
        for j in range(1, cy):
            x = i * w / cx
            y = j * h / cy
            r = 2

            rel_x = w / 2 - x
            rel_y = h / 2 - y
            off_x = 0
            off_y = 100

            dist = sqrt(((rel_x + off_x) / 1750) ** 2 + ((rel_y + off_y) / 1250) ** 2)
            c = int(90 * max(0, 1 - dist))

            d.circle((x, y), radius=r, fill=(c, c, c))

    im.save("out.png")


if __name__ == "__main__":
    main()
