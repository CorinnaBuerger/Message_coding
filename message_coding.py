import cv2

def char_generator(message):
    for c in message:
        yield ord(c)

def get_image(image_location):
    img = cv2.imread(image_location)
    return img

def gcd(x, y): # returns the greatest common divisor of x and y
  while(y):
    x, y = y, x % y

  return x

def encode_image(image_location, msg):
    img = get_image(image_location)
    msg_gen = char_generator(msg)
    pattern = gcd(len(img), len(img[0]))
    for i in range(len(img)):
        for j in range(len(img[0])):
            if ((i + 1) * (j + 1)) % pattern == 0: # starting at the second pixel: if the pixel is a multiple of our gcd 
                try:
                    img[i-1][j-1][0] = next(msg_gen) # we change the pixel 
                except StopIteration: # if it has already generated everything and the message is over
                    img[i-1][j-1][0] = 0 # 0 marks the end
                    return img

def decode_image(img_loc):
  img = get_image(img_loc)
  pattern = gcd(len(img), len(img[0]))
  message = ''
  for i in range(len(img)):
    for j in range(len(img[0])): 
      if ((i - 1) * (j - 1)) % pattern == 0: # for every multiple of our gcd
        if img[i-1][j-1][0] != 0: # if the numeric value of the pixel's red value is not 0 (0 is the end)
          message = message + chr(img[i-1][j-1][0]) # we add the numeric value of the pixel's red value
        else:
          return message # returns message if we reached the end(0)

