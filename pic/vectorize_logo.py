"""Trace the supplied CUMT wordmark into editable SVG and vector PDF."""
from pathlib import Path
import numpy as np
from PIL import Image
from potrace import Bitmap
from reportlab.pdfgen import canvas

root = Path(__file__).resolve().parent
im = Image.open(root / 'cumt-logo-wordmark-hd.png').convert('RGBA')
arr = np.array(im)
mask = (arr[:, :, 3] >= 100) & (arr[:, :, :3].mean(axis=2) < 180)
bitmap = Image.fromarray(np.where(mask, 0, 255).astype('uint8'))
curves = Bitmap(bitmap).trace(turdsize=0, alphamax=0.85, opttolerance=0.12)
w, h = im.size
c = canvas.Canvas(str(root / 'cumt-logo-wordmark-vector.pdf'), pagesize=(w, h))
c.setTitle('China University of Mining and Technology wordmark')
c.setFillColorRGB(22/255, 51/255, 103/255)
c.translate(0, h)
c.scale(1, -1)
p = c.beginPath()
commands = []
count = 0
for curve in curves:
    x, y = curve.start_point.x, curve.start_point.y
    p.moveTo(x, y)
    commands.append(f'M{x:.3f},{y:.3f}')
    for segment in curve:
        x, y = segment.end_point.x, segment.end_point.y
        if segment.is_corner:
            cx, cy = segment.c.x, segment.c.y
            p.lineTo(cx, cy)
            p.lineTo(x, y)
            commands.append(f'L{cx:.3f},{cy:.3f} L{x:.3f},{y:.3f}')
        else:
            x1, y1 = segment.c1.x, segment.c1.y
            x2, y2 = segment.c2.x, segment.c2.y
            p.curveTo(x1, y1, x2, y2, x, y)
            commands.append(f'C{x1:.3f},{y1:.3f} {x2:.3f},{y2:.3f} {x:.3f},{y:.3f}')
    p.close()
    commands.append('Z')
    count += 1
c.drawPath(p, stroke=0, fill=1, fillMode=0)
c.showPage()
c.save()
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
       f'width="{w}" height="{h}"><title>CUMT wordmark</title>'
       '<path fill="#163367" fill-rule="evenodd" d="' + ' '.join(commands) + '"/></svg>')
(root / 'cumt-logo-wordmark-vector.svg').write_text(svg, encoding='utf-8')
print(f'Traced {count} contours; exported SVG and PDF with Bezier paths.')
