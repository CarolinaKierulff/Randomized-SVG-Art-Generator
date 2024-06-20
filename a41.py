from typing import NamedTuple

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


#Write the generated HTML and SVG code to a text file (i.e., not to standard output).
def writeTxtFile(html_text: str) -> None:
    """writeTxtFile() method"""
    with open("a41.html", "w") as file:
        file.write(str(html_text))

def main() -> None:
    """main method"""
    html_doc = HtmlDocument("My Art")

    svg_canvas = SvgCanvas(1000, 3000)
    shapes = [
        CircleShape(50, 50, 50, ShapeColor(255, 0, 0, 1.0)),
        CircleShape(150, 50, 50, ShapeColor(255, 0, 0, 1.0)),
        CircleShape(250, 50, 50, ShapeColor(255, 0, 0, 1.0)),
        CircleShape(350, 50, 50, ShapeColor(255, 0, 0, 1.0)),
        CircleShape(450, 50, 50, ShapeColor(255, 0, 0, 1.0)),
        CircleShape(50, 250, 50, ShapeColor(0, 0, 255, 1.0)),
        CircleShape(150, 250, 50, ShapeColor(0, 0, 255, 1.0)),
        CircleShape(250, 250, 50, ShapeColor(0, 0, 255, 1.0)),
        CircleShape(350, 250, 50, ShapeColor(0, 0, 255, 1.0)),
        CircleShape(450, 250, 50, ShapeColor(0, 0, 255, 1.0))
    ]

    svg_canvas.gen_art(shapes)
    svg_text = svg_canvas.write_svg()
    
    html_doc.write_body(svg_text)

    html_text = html_doc.write_html()
    writeTxtFile(html_text)

if __name__ == "__main__":
    main()

