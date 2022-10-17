#!python
"""
Generates an HTML file with the contours for a list of furnitures
from the application SweetHome3D (CSV export). 
The resulting HTML code/page can then be printed and used for modeling.
"""
import sys
from string import Template


__version__ = "1.0.0"
__date__ = "2017-12-16"
__updated__ = "2017-12-16"

# resizing factor
FACTOR = 1.0 / 50.0

# read CSV file
with open(sys.argv[1], "r", encoding="utf8") as fin:
    lines = fin.readlines()

for i, line in enumerate(lines):
    if i == 0:
        # skip first/header line
        continue

    name,width,depth,height,visible = line.split('\t')
    w = float(width.replace(',','.')) * FACTOR
    h = float(depth.replace(',','.')) * FACTOR
    t = float(depth.replace(',','.')) * FACTOR

    tpl = Template('<div style="width:${w}cm;height:${h}cm;">$name ($breite x $hoehe x $tiefe)</div>')
    s = tpl.substitute(locals())

    print(s)
