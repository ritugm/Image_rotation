import math

def rotate_image(data, width, height, angle):
    # convert the 1D data to 2D matrix
    matrix = [data[i:i+width] for i in range(0, len(data), width)]
    
    # calculate the new dimensions based on the rotation angle
    if angle == 0 or angle == 180:
        new_width, new_height = width, height
    elif angle == 90 or angle == 270:
        new_width, new_height = height, width
    else:
        diagonal = math.sqrt(width**2 + height**2)
        new_width = int(diagonal * math.cos(math.radians(angle)))
        new_height = int(diagonal * math.sin(math.radians(angle)))
    
    # create a new matrix filled with zeros
    new_matrix = [[0 for _ in range(new_width)] for _ in range(new_height)]
    
    # calculate the center of the new matrix
    cx, cy = new_width/2, new_height/2
    
    # rotate each pixel in the old matrix and place it in the new matrix
    for y in range(height):
        for x in range(width):
            pixel = matrix[y][x]
            if pixel == 1:
                # calculate the new coordinates of the pixel
                if angle == 0:
                    nx, ny = x, y
                elif angle == 90:
                    nx, ny = y, width-x-1
                elif angle == 180:
                    nx, ny = width-x-1, height-y-1
                elif angle == 270:
                    nx, ny = height-y-1, x
                else:
                    nx = int((x - cx) * math.cos(math.radians(angle)) - (y - cy) * math.sin(math.radians(angle)) + cx)
                    ny = int((x - cx) * math.sin(math.radians(angle)) + (y - cy) * math.cos(math.radians(angle)) + cy)
                # set the pixel in the new matrix
                new_matrix[ny][nx] = 1
    
    # convert the new matrix back to 1D data
    rotated_data = [pixel for row in new_matrix for pixel in row]
    
    return rotated_data, new_width, new_height

# read the image data from file
with open('image.pbm', 'r') as f:
    # read the header information
    header = f.readline().strip()
    width, height = map(int, f.readline().strip().split())
    data = []
    # read the data
    for line in f:
        data += list(map(int, line.strip().split()))

# rotate the image by the given angle
angle = int(input("Enter the rotation angle (in degrees): "))
rotated_data, new_width, new_height = rotate_image(data, width, height, angle)

# write the rotated image to a new file
with open('rotated_image.pbm', 'w') as f:
    f.write(header+'\n')
    f.write(f"{new_width} {new_height}\n")
    for i in range(0, len(rotated_data), new_width):
        f.write(' '.join(map(str, rotated_data[i:i+new_width])) + '\n')
