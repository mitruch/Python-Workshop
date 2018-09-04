class Picture():
    red_ = []
    green_ = []
    blue_ = []
    width = 0
    height = 0
    def __init__(self, red, green, blue, width, height):
        self.red_ = list(red) #lepiej przerzucic si ena wlany typ zeby uniezaleznic sie od otrzymanego
        self.green_ = list(green)
        self.blue_ = list(blue) 
        self.width = width
        self.height = height

    def red(self):
        canal = [color for color in self.red_]
        return tuple(canal)
    
    def green(self):
        canal = [color for color in self.blue_]
        return tuple(canal)
    
    def blue(self):
        canal = [color for color in self.blue_]
        return tuple(canal)
    
    def size(self):
        return (self.width, self.height)

    def crop(self, x, y, width, height):

        old_width = self.width
        old_height = self.height

        if x + width > self.width:
            self.width = self.width - x
        else:    
           self.width = width 

        if y + height > self.height:
            self.height = self.height - y
        else:
            self.height = height

        num = y*old_width + x  
        step = old_width 
    
        if step == 0:
            step = 1

        end = (self.height * step)

        new_red = []
        for limit in range(num, num + end, step):
            for counter in range(limit, limit + self.width):
                new_red.append(self.red_[counter])

        new_green = []
        for limit in range(num, num + end, step):
            for counter in range(limit, limit + self.width):
                new_green.append(self.green_[counter])

        new_blue = []
        for limit in range(num, num + end, step):
            for counter in range(limit, limit + self.width):
                new_blue.append(self.blue_[counter])
      
        self.red_ = new_red
        self.green_ = new_green
        self.blue_ = new_blue

    def pixel(self, x, y):
        num = y*self.width + x
        color = []
        color.append(self.red_[num])
        color.append(self.green_[num])
        color.append(self.blue_[num])
        return tuple(color)


def test_one_red_pixel():
    red = [255]
    green = [0]
    blue = [0]
    width = 1
    height = 1
    obrazek = Picture(red=red, green=green, blue=blue, width=width, height=height)
    assert (1, 1) == obrazek.size()
    assert (255, ) == obrazek.red()
    assert (0, ) == obrazek.green() 
    assert (0, ) == obrazek.blue()
    assert (255, 0, 0) == obrazek.pixel(0, 0)

def test_kwadrat_gradient():
    obrazek = Picture(red=range(256), green=range(256), blue=range(256), width=16, height=16)
    assert (16, 16) == obrazek.size()
    val = 0
    for y in range(16):
        for x in range(16):
            assert (val, val, val) == obrazek.pixel(x, y)
            val += 1

    # Same picture
    obrazek_2 = Picture(red=range(256), green=range(256), blue=range(256), width=16, height=16)
    obrazek_2.crop(0, 0, 16, 16) # powinniśmy dostać ten sam obrazek
    assert obrazek.red() == obrazek_2.red()
    assert obrazek.green() == obrazek_2.green()
    assert obrazek.blue() == obrazek_2.blue()

    # Left upper corner
    obrazek_2 = Picture(red=range(256), green=range(256), blue=range(256), width=16, height=16)
    obrazek_2.crop(0, 0, 1, 1)
    assert (0, ) == obrazek_2.red()
    assert (0, ) == obrazek_2.green()
    assert (0, ) == obrazek_2.blue()

    # right upper corner
    obrazek_2 = Picture(red=range(256), green=range(256), blue=range(256), width=16, height=16)
    obrazek_2.crop(15, 0, 1, 1)
    assert (15, ) == obrazek_2.red()
    assert (15, ) == obrazek_2.green()
    assert (15, ) == obrazek_2.blue()

    # right lower corner
    obrazek_2 = Picture(red=range(256), green=range(256), blue=range(256), width=16, height=16)
    obrazek_2.crop(15, 15, 1, 1)
    assert (255, ) == obrazek_2.red()
    assert (255, ) == obrazek_2.green()
    assert (255, ) == obrazek_2.blue()

    # left lower corner
    obrazek_2 = Picture(red=range(256), green=range(256), blue=range(256), width=16, height=16)
    obrazek_2.crop(0, 15, 1, 1)
    assert (240, ) == obrazek_2.red()
    assert (240, ) == obrazek_2.green()
    assert (240, ) == obrazek_2.blue()

    # 2x3 near lower corner
    obrazek_2 = Picture(red=range(256), green=range(256), blue=range(256), width=16, height=16)
    obrazek_2.crop(1, 12, 2, 3)
    assert (193, 194, 209, 210, 225, 226) == obrazek_2.red()
    assert (193, 194, 209, 210, 225, 226) == obrazek_2.green()
    assert (193, 194, 209, 210, 225, 226) == obrazek_2.blue()

    # 10x15 wystający → 3x5 lower right corner
    obrazek_2 = Picture(red=range(256), green=range(256), blue=range(256), width=16, height=16)
    obrazek_2.crop(13, 11, 10, 15)
    assert (189, 190, 191, 205, 206, 207, 221, 222, 223, 237, 238, 239, 253, 254, 255) == obrazek_2.red()
    assert (189, 190, 191, 205, 206, 207, 221, 222, 223, 237, 238, 239, 253, 254, 255) == obrazek_2.green()
    assert (189, 190, 191, 205, 206, 207, 221, 222, 223, 237, 238, 239, 253, 254, 255) == obrazek_2.blue()


test_one_red_pixel()
test_kwadrat_gradient()


# i = range(1,10, 2)
# print(i)
# print(type(i))
# print(i[::2])
