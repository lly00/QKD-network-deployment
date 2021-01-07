#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

from utils import myIO
from utils import myDraw

G = myIO.read_file("./data/links.csv",1)
print(G.nodes())
print(G.edges())
myDraw.draw(G)
