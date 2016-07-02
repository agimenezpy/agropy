import os.path as pth
from climatepy.scenario import RCP_45, RCP_85
from climatepy.util.dirs import load_all

__author__ = 'agimenez'

ROOT_DIR = pth.dirname(pth.dirname(__file__))
SYM_LINKS = load_all(pth.join(ROOT_DIR, "alcance"))
MODEL_DIR = SYM_LINKS["Modelo_ETA"]
RCP_45 = pth.join(MODEL_DIR, RCP_45)
RCP_85 = pth.join(MODEL_DIR, RCP_85)
SHP_DIR = SYM_LINKS["Mapas_Generales"]
OUTPUT_DIR = pth.join(ROOT_DIR, "salida")
