from typing import NamedTuple
import random

#PART 1 ------------------------------------------------------------------------------------------------------------------------------------

#HtmlDocument to generate an HTML page consisting of a header and a body
class  HtmlDocument:
    """HtmlDocument class"""
    def __init__(self,title) -> None:
        """__init__ method""" 
        self.title = title

    def write_body(self, body_text) -> None:
        """write_body method""" 
        self.body = body_text

    def write_html(self) -> str:
        """write_html method""" 
        html_text = f"<html>\n<head>\n    <title>{self.title}</title>\n</head>\n<body>\n{self.body}\n</body>\n</html>"
        return html_text


#Python super class called HtmlComponent to render an HTML component. Then use single inheritance to inherit the properties from HtmlComponent.     
class HtmlComponent:
    """HtmlComponent class"""
    def __init__(self, component) -> None:
        """__init__ method""" 
        self.component = component 
        self.content = ""

    def set_content(self, content) -> None:
        """set_content method"""
        self.content = content    

    def write_component(self) -> str:
        """write_component method"""
        html_component = f"<{self.component}>{self.content}</{self.component}>"
        return html_component


class HtmlElement(HtmlComponent):
    """HtmlElement class"""
    def __init__(self, component) -> None:
        """__init__ method""" 
        super().__init__(component)


#Python class called SvgCanvas to generate the <svg>, </svg> tags for the SVG drawing in an SVG canvas or viewport.
class SvgCanvas:
    """SvgCanvas class"""
    def __init__(self, width: int, height: int) -> None:
        """__init__ method""" 
        self.width = width
        self.height = height
        self.shapes = []

    def gen_art(self, shapes: list) -> None:
        """gen_art method"""   
        self.shapes.extend(shapes)

    def write_svg(self) -> str:
        """write_svg method"""  
        svg_text = f"    <svg width=\"{self.width}\" height=\"{self.height}\">\n"
        for shape in self.shapes:
            svg_text += str(shape)
        svg_text += "    </svg>"
        return svg_text

#Class that returns the shape's color formatted
class ShapeColor(NamedTuple):
    """ShapeColor class"""
    r: int              #red
    g: int              #green
    b: int              #blue
    opacity: float

    def __str__(self) -> str:
        """__str__ method"""
        color_text = f'fill=\"rgb({self.r}, {self.g}, {self.b})\" fill-opacity=\"{self.opacity}\"'
        return color_text
   
#Python classes called CircleShape, RectangleShape, EllipseShape to draw circles, rectangles, and ellipses using the SVG <circle>, <rect> and <ellipse> tags.
class CircleShape:
    """CircleShape class"""
    def __init__(self, cx: int, cy: int, radius: int, fill: ShapeColor) -> None:  
        """__init__ method"""
        self.cx = cx
        self.cy = cy
        self.radius = radius
        self.fill = fill

    def __str__(self) -> str:
        """__str__ method"""
        circle_text = f"        <circle cx=\"{self.cx}\" cy=\"{self.cy}\" r=\"{self.radius}\" {self.fill}></circle>\n"
        return circle_text


class RectangleShape:
    """RectangleShape class"""
    def __init__(self, x: int, y: int, width: int, height:int, fill: ShapeColor) -> None: 
        """__init__ method""" 
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fill = fill

    def __str__(self) -> str:
        """__str__() method"""
        rectangle_text = f"        <rect x=\"{self.x}\" y=\"{self.y}\" width=\"{self.width}\" height=\"{self.width}\" {self.fill}></rect>\n"
        return rectangle_text


class EllipseShape:
    """EllipseShape class"""
    def __init__(self, cx: int, cy: int, rx: int, ry: int, fill: ShapeColor) -> None: 
        """__init__() method"""  
        self.cx = cx
        self.cy = cy
        self.rx = rx
        self.ry = ry
        self.fill = fill

    def __str__(self) -> str:
        """__str__() method"""
        ellipse_text = f"        <ellipse cx=\"{self.cx}\" cy=\"{self.cy}\" rx=\"{self.rx}\" ry=\"{self.ry}\" {self.fill}></ellipse>\n"
        return ellipse_text                                  


#PART 2 ------------------------------------------------------------------------------------------------------------------------------

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
        return f"{random.randint(*self.circle_r):>1}"
    
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
        if shape == 0:                                        #circle
            cx, cy = [int(i) for i in self.cor]
            r, g, b = [int(i) for i in self.color]
            return CircleShape(cx,cy,self.circus_r,ShapeColor(r, g, b, self.opacity)).__str__()
        
        elif shape == 1:                                      #rectangle
            x, y = [int(i) for i in self.cor]
            w, h = [int(i) for i in self.recta]
            r, g, b = [int(i) for i in self.color]
            return RectangleShape(x,y,w,h,ShapeColor(r, g, b, self.opacity)).__str__()  
        
        elif shape == 2:                                      #ellipse 
            cx, cy = [int(i) for i in self.cor]
            rx, ry = [int(i) for i in self.ellipse_r]  
            r, g, b = [int(i) for i in self.color]
            return EllipseShape(cx,cy,rx,ry,ShapeColor(r, g, b, self.opacity)).__str__() 
        

#PART 3 --------------------------------------------------------------------------------------------------------------------------------

#Generates the svg art
def generate_art(config: PyArtConfig):
    """generate_art method"""
    html_doc = HtmlDocument("My Art")

    svg_canvas = SvgCanvas(1000, 800)
    shapes = []

    for i in range(500):
        shapes.append(RandomShape(config).as_svg())

    shapes_str = "".join(shapes)

    svg_canvas.gen_art(shapes_str)
    svg_text = svg_canvas.write_svg()

    html_doc.write_body(svg_text)
    html_text = html_doc.write_html()
    writeTxtFile(html_text)  


#Write the generated HTML and SVG code to a text file (i.e., not to standard output).
def writeTxtFile(html_text: str):
    """writeTxtFile method"""
    with open("a433.html", "w") as file:

        file.write(str(html_text))

#Different configurations for the svg art  
def midnight():
    """midnight method"""
    return PyArtConfig(shape=(0,2), x_cor=(0, 1200), y_cor=(0, 600), red=(0, 45), green=(0, 45), blue=(0, 175), opacity=(1.0,1.0))

def rainbow():
    """rainbow method"""
    return PyArtConfig(shape=(0,2), x_cor=(0, 780), y_cor=(0, 780), opacity=(0.5,1.0))

def rain_drops():
    """rain_drops method"""
    return PyArtConfig(shape=(2,2), x_cor=(0, 980), y_cor=(0, 780), ellipse_rx=(5, 10), 
                       ellipse_ry=(10, 25), red=(117, 127), green=(188, 198), blue=(195, 230))

def toxic():
    """toxic method"""
    return PyArtConfig(shape=(0,0), x_cor=(0, 1180), y_cor=(200, 600), circle_r=(0, 50), red=(40, 50), green=(30, 140), blue=(45, 55), opacity=(0.0,1.0))

def bricks():
    """bricks method"""
    return PyArtConfig(shape=(1,1), x_cor=(0, 635), y_cor=(0, 600), rect_w=(30, 700), rect_h=(10, 50), red=(85, 190), green=(35, 55), blue=(15, 30), opacity=(0.5,1.0))

def barbie():
    """barbie method"""
    return PyArtConfig(shape=(0,2), x_cor=(0, 800), y_cor=(0, 600), red=(200, 255), green=(0, 0), blue=(200, 255), opacity=(0.0,1.0))

def waves():
    """waves method"""
    return PyArtConfig(shape=(0,0), x_cor=(50, 600), y_cor=(285, 580), circle_r=(0, 100), red=(25, 135), green=(180, 200), blue=(215, 215), opacity=(0.0,1.0))


def main() -> None:
    """main method"""
    config = rain_drops()
    generate_art(config)
    

if __name__ == "__main__":
    main()  
