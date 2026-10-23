
# 1. Importar la biblioteca para analizar datos
from pathlib import Path
import pandas as pd

ruta_csv = Path(__file__).resolve().parent.parent / "datos" / "produccion.csv"

datos = pd.read_csv(ruta_csv) 

print("\n=== PRODUCCIÓN POR MÁQUINA ===")
print(datos[["Máquina", "Unidades fabricadas"]])    