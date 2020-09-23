import fitz
import sys

doc = fitz.open('demo.pdf')

for pg in range(doc.pageCount):
    page = doc[pg]
    zoom = int(100)
    rotate = int(0)
    trans = fitz.Matrix(zoom / 100.0, zoom / 100.0).preRotate(rotate)

    # create raster image of page (non-transparent)
    pm = page.getPixmap(matrix=trans, alpha=False)

    # write a PNG image of the page
    pm.writePNG('%s.png' % pg)
