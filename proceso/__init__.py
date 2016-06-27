import os.path as pth
from climatepy.scenario import ETA_20K

__author__ = 'agimenez'
ROOT_DIR = pth.dirname(pth.dirname(__file__))
MODEL_DIR = "/home/agimenez/Media/Desktop/ProyectoCC/"
ETA_20K = pth.join(MODEL_DIR, ETA_20K)
#"/Users/agimenez/Desktop/ProyectoCC/"
SHP_DIR = pth.join(ROOT_DIR, "alcance")
OUTPUT_DIR = pth.join(ROOT_DIR, "salida")
