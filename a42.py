import random   

class PyArtConfig:
    """PyArtConfig class"""
    default_ranges = {
        'shape': (0, 2),
        'x_cor': (0, 500),
        'y_cor': (0, 300),
        'circle_r': (0, 100),
        'ellipse_rx': (10, 30),
        'ellipse_ry': (10, 30),
        'rect_w': (10, 100),
        'rect_h': (10, 100),
        'red': (0, 255),
        'green': (0, 255),
        'blue': (0, 255),
        'opacity': (0.0, 1.0)
    }

    def __init__(self, count=0, **kwargs):
        """__init__ method"""
        self.count = count
        for key, value in PyArtConfig.default_ranges.items():
            setattr(self, key, kwargs.get(key, value))

    def gen_count(self):
        """gen_count method"""
        temp = 0
        if self.count == 0:
            self.count = 1
            return f"{temp:>3}"
        temp = self.count
        self.count += 1
        return f"{temp:>3}"

    def gen_shape(self):
        """gen_shape method"""
        return f"{random.randint(*self.shape):>3}"
    
    def gen_cor(self):
        """gen_cor method"""
        return (f"{random.randint(*self.x_cor):>4}",
                f"{random.randint(*self.y_cor):>4}")
    
    def gen_circus_r(self):
        """gen_circus_r method"""
        return f"{random.randint(*self.circle_r):>3}"
    
    def gen_ellipse_r(self):
        """gen_ellipse_r method"""
        return (f"{random.randint(*self.ellipse_rx):>3}",
                f"{random.randint(*self.ellipse_ry):>3}")
    
    def gen_rect(self):
        """gen_rect method"""
        return (f"{random.randint(*self.rect_w):>3}",
                f"{random.randint(*self.rect_h):>3}")

    def gen_color(self):
        """gen_color method"""
        return (f"{random.randint(*self.red):>3}",
                f"{random.randint(*self.green):>3}",
                f"{random.randint(*self.blue):>3}")
    
    def gen_op(self):
        """gen_op method"""
        number = round(random.uniform(*self.opacity), 1)
        return f"{number:>3}"
        

class RandomShape:
    """RandomShape class"""
    def __init__(self, config):
        self.count = config.gen_count()
        self.shape = config.gen_shape()
        self.cor = config.gen_cor()
        self.circus_r = config.gen_circus_r()
        self.ellipse_r = config.gen_ellipse_r()
        self.recta = config.gen_rect()
        self.color = config.gen_color()
        self.opacity = config.gen_op()
    
    def __str__(self):
        """__str__ method"""
        return f"{self.count} {self.shape} {self.cor} {self.circus_r} {self.ellipse_r} {self.recta} {self.color} {self.opacity}"
    
    def as_Part2_line(self):
        """as_Part2_line method"""
        return f"{self.count} {self.shape} {' '.join(str(i) for i in self.cor)} {self.circus_r} {' '.join(str(i) for i in self.ellipse_r)} {' '.join(str(i) for i in self.recta)} {' '.join(str(i) for i in self.color)} {self.opacity}"

    def as_svg(self):
        """as_svg method"""
        shape = int(self.shape)
        if shape == 0:      #circle
            cx, cy = [int(i) for i in self.cor]
            r, g, b = [int(i) for i in self.color]
            return f"<circle cx=\"{cx}\" cy=\"{cy}\" r=\"{self.circus_r}\" fill=\"rgb({r}, {g}, {b})\" opacity=\"{self.opacity}\" />"
        
        elif shape == 1:    #rectangle
            x, y = [int(i) for i in self.cor]
            w, h = [int(i) for i in self.cor]
            r, g, b = [int(i) for i in self.color]
            return f"<rect x=\"{x}\" y=\"{y}\" width=\"{w}\" height=\"{h}\" fill=\"rgb({r}, {g}, {b})\" opacity=\"{self.opacity}\" />"
        
        else:               #ellipse 
            cx, cy = [int(i) for i in self.cor]
            rx, ry = [int(i) for i in self.ellipse_r]  
            r, g, b = [int(i) for i in self.color]
            return f"<ellipse cx=\"{cx}\" cy=\"{cy}\" rx=\"{rx}\" ry=\"{ry}\" fill=\"rgb({r}, {g}, {b})\" opacity=\"{self.opacity}\" />"    

def main() -> None:
    """main method"""
    config = PyArtConfig()
    print("CNT SHA    X    Y RAD  RX  RY   W   H   R   G   B  OP")
    for i in range(10):
        print(RandomShape(config).as_Part2_line())

    
if __name__ == "__main__":
    main()