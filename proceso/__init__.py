import matplotlib.pyplot as plt
import os.path as pth

from climatepy.scenario import RCP_45, RCP_85, REMOTE_URL
from climatepy.util.dirs import load_all

plt.style.use('ggplot')

__author__ = 'agimenez'

ROOT_DIR = pth.dirname(pth.dirname(__file__))
SYM_LINKS = load_all(pth.join(ROOT_DIR, "alcance"))
MODEL_DIR = SYM_LINKS["Modelo_ETA"]
MODEL2_DIR = SYM_LINKS["Modelo_MIROC"]
CRU_DIR = SYM_LINKS["Modelo_CRU"]
M_RCP_85 = pth.join(MODEL2_DIR, RCP_85)
RCP_45 = pth.join(MODEL_DIR, RCP_45)
RCP_85 = pth.join(MODEL_DIR, RCP_85)
SHP_DIR = SYM_LINKS["Mapas_Generales"]
OUTPUT_DIR = pth.join(ROOT_DIR, "salida")

RCP_45_URL = [
    ("Mensual/Prec/Eta_HG2ES_RCP45_20km_Prec_Mensual_template.ctl",
     "Anual/Prec/Eta_HG2ES_RCP45_20km_Prec_Anual_template.ctl"),
    ("Mensual/Temp/Eta_HG2ES_RCP45_20km_Temp_Mensual_template.ctl",
     "Anual/Temp/Eta_HG2ES_RCP45_20km_Temp_Anual_template.ctl")
]

RCP_85_URL = [
    ("Mensual/PREC/Eta_HadGEM2-ES_20km_RCP8.5_Mensual_PREC_template.ctl",
     "Anual/PREC/Eta_HadGEM2-ES_20km_RCP8.5_Anual_PREC_template.ctl"),
    ("Mensual/TP2M/Eta_HadGEM2-ES_20km_RCP8.5_Mensual_TP2M_template.ctl",
     "Anual/TP2M/Eta_HadGEM2-ES_20km_RCP8.5_Anual_TP2M_template.ctl")
]

M_RCP_85_URL = [
    ("Mensual/PREC/Eta_MIROC5_20km_RCP8.5_Mensual_PREC_template.ctl",
     "Anual/PREC/Eta_MIROC5_20km_RCP8.5_Anual_PREC_template.ctl"),
    ("Mensual/TP2M/Eta_MIROC5_20km_RCP8.5_Mensual_TP2M_template.ctl",
     "Anual/TP2M/Eta_MIROC5_20km_RCP8.5_Anual_TP2M_template.ctl")
]

CRU_URL = [
    REMOTE_URL + "cru/cru_pre_clim_1961-1990.nc",
    REMOTE_URL + "cru/cru_tmp_clim_1961-1990.nc"
]

GRANCHACO_SHP_URL = "Mapas Generales/Departamentos_y_Provincias_del_Gran_Chaco.shp"
PARAGUAY_SHP_URL = "shp/PRY_adm1.shp"
CRU_XLS = "shp/cru_ts23_1991_2014.xlsx"
