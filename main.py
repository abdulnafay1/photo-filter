import common

def grayscale(image_matrix):

    for row in range(len(image_matrix)):
        for col in range(len(image_matrix[row])):
            image_matrix[row][col] = [(image_matrix[row][col][0]+image_matrix[row][col][1]+image_matrix[row][col][2])/3,
            (image_matrix[row][col][0]+image_matrix[row][col][1]+image_matrix[row][col][2])/3,
            (image_matrix[row][col][0]+image_matrix[row][col][1]+image_matrix[row][col][2])/3]

    common.write_file("grayscale.jpeg",image_matrix)

def invert_colors(image_matrix):
    for row in range(len(image_matrix)):
        for col in range(len(image_matrix[row])):
            image_matrix[row][col] = [255 - image_matrix[row][col][0],
                                      255 - image_matrix[row][col][1],
                                      255 - image_matrix[row][col][2]]

    common.write_file("inverted.jpeg", image_matrix)


def red_stripe(image_matrix):
    factor = 100
    for row in range(len(image_matrix)):
        if row % factor < 51:
            for col in range(len(image_matrix[row])):
                image_matrix[row][col] = [255, image_matrix[row][col][1], image_matrix[row][col][2]]

    common.write_file("red_stripe.jpeg", image_matrix)


def flip(image_matrix):

    height = len(image_matrix)
    width = len(image_matrix[1])

    new = [[0] * width for i in range(height)]

    for row in range(len(image_matrix) - 1, -1, -1):
        for col in range(len(image_matrix[row])):
            new[len(image_matrix) - row -1][col] = image_matrix[row][col]

    common.write_file("inverted.jpeg", new)


def sepia(image_matrix):
    for row in range(len(image_matrix)):
        for col in range(len(image_matrix[row])):

            red_value = int((image_matrix[row][col][0] * 0.393) + (image_matrix[row][col][1] * 0.769) + (
                        image_matrix[row][col][2] * 0.189))
            green_value = int((image_matrix[row][col][0] * 0.349) + (image_matrix[row][col][1] * 0.686) + (
                        image_matrix[row][col][2] * 0.168))
            blue_value = int((image_matrix[row][col][0] * 0.272) + (image_matrix[row][col][1] * 0.534) + (
                        image_matrix[row][col][2] * 0.131))

            if red_value > 255 or red_value < 0:
                red_value = 255

            if green_value > 255 or green_value < 0:
                green_value = 255

            if blue_value > 255 or blue_value < 0:
                blue_value = 255

            image_matrix[row][col] = [red_value, green_value, blue_value]

    common.write_file("sepia.jpeg", image_matrix)


def blur(image_matrix):

    new = copy.deepcopy(image_matrix)

    for row in range(1, len(image_matrix)-1):
        for col in range(1, len(image_matrix[row])-1):
            new[row][col][0] = ((image_matrix[row-1][col][0] + image_matrix[row+1][col][0] + image_matrix[row][col+1][0] + image_matrix[row][col-1][0] + image_matrix[row][col][0] + image_matrix[row-1][col-1][0] + image_matrix[row+1][col+1][0] + image_matrix[row-1][col+1][0] + image_matrix[row+1][col-1][0] + image_matrix[row+1][col+1][0]) / 9)
            new[row][col][1] = ((image_matrix[row-1][col][1] + image_matrix[row+1][col][1] + image_matrix[row][col+1][1] + image_matrix[row][col-1][1] + image_matrix[row][col][1] + image_matrix[row-1][col-1][1] + image_matrix[row+1][col+1][1] + image_matrix[row-1][col+1][1] + image_matrix[row+1][col-1][1] + image_matrix[row+1][col+1][1]) / 9)
            new[row][col][2] = ((image_matrix[row-1][col][2] + image_matrix[row+1][col][2] + image_matrix[row][col+1][2] + image_matrix[row][col-1][2] + image_matrix[row][col][2] + image_matrix[row-1][col-1][2] + image_matrix[row+1][col+1][2] + image_matrix[row-1][col+1][2] + image_matrix[row+1][col-1][2] + image_matrix[row+1][col+1][2]) / 9)

    common.write_file("blurred.jpeg",new)

def threshold(image_matrix, red_min, red_max, green_min, green_max, blue_min, blue_max):
    for row in range(len(image_matrix)):
        for col in range(len(image_matrix[row])):
            pixel = image_matrix[row][col]
            red, green, blue = pixel

            if red < red_min or red > red_max:
                red = 0
            if green < green_min or green > green_max:
                green = 0
            if blue < blue_min or blue > blue_max:
                blue = 0

            image_matrix[row][col] = [red, green, blue]

    common.write_file("threshold.jpeg", image_matrix)

def mirror(image_matrix):

    new = image_matrix

    for row in range(len(image_matrix)):
        for col in range(len(image_matrix[row])):
            new[row][col] = image_matrix[row][len(image_matrix[row]) - col - 1]

    common.write_file("inverted.jpeg", new)

pic = common.read_file("imagee.jpg")
mirror(pic)

pic = common.read_file("logo.jpeg")
threshold(pic, 0,120,0,200,0,200)

pic = common.read_file("img.jpg")

blur(pic)

pic = common.read_file("imag.png")

sepia(pic)

pic = common.read_file("obaman.jpg")
flip(pic)

pic = common.read_file("img.jpg")

red_stripe(pic)

pic = common.read_file("test.png")

invert_colors(pic)

pic = common.read_file("logo.jpeg")

grayscale(pic)


