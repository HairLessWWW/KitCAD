import FreeCAD
import Part
import math
from FreeCAD import Vector
from parse_prompt import parse_description

def make_hex_head(radius=6, height=5):
    points = []
    for i in range(6):
        angle = 2 * math.pi * i / 6
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        points.append(Vector(x, y, 0))
    points.append(points[0])
    poly = Part.makePolygon(points)
    face = Part.Face(poly)
    hex_head = face.extrude(Vector(0, 0, height))
    return hex_head

# Загружаем описание
with open("input.txt", "r", encoding="utf-8") as f:
    description = f.read()

params = parse_description(description)
diameter = params.get("diameter", 6)
length = params.get("length", 30)
head_type = params.get("head", "none")

doc = FreeCAD.newDocument("result")
shaft = Part.makeCylinder(diameter / 2, length)

if head_type == "hex":
    head = make_hex_head(radius=diameter / 1.6, height=5)
    head.translate(Vector(0, 0, length))
    bolt = shaft.fuse(head)
else:
    bolt = shaft

Part.show(bolt)
doc.recompute()
doc.saveAs("result.FCStd")
