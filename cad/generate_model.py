import FreeCAD
import Part

doc = FreeCAD.newDocument("Generated")
part = Part.makeCylinder(5, 10)
Part.show(part)
doc.recompute()
doc.saveAs("result.FCStd")
