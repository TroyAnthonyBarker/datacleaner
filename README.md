# Datacleaner

## 📄 Descripción

**Datacleaner** es una librería de Python para la limpieza automática de datos utilizando pandas. Su objetivo es reducir el tiempo dedicado a tareas rutinarias de preprocesamiento y mejorar la calidad de los datos antes del análisis o modelado.

## 🚀 Instalación

```bash
pip install datacleaner
```

> ⚠️ Requiere Python 3.7+ y pandas 1.0+

## 📦 Características

- Limpieza de valores nulos con diferentes estrategias (`mean`, `median`, `drop`)
- Conversión automática de tipos (fechas, numéricos, booleanos, categóricos)
- Detección y eliminación de columnas constantes o con valores únicos
- Detección y tratamiento de outliers (`z-score`, `IQR`)
- Función `clean_data()` para limpiar un DataFrame en una sola línea

## 🧪 Ejemplo de uso

```python
import pandas as pd
from datacleaner import clean_data

df = pd.read_csv("datos.csv")

df_limpio = clean_data(df,
                       fill_strategy="mean",
                       remove_constants=True,
                       remove_outliers_flag=True)
```

## 🔧 Funciones principales

| Función                | Descripción                                         |
|------------------------|-----------------------------------------------------|
| `clean_data()`         | Limpieza integral del DataFrame                     |
| `handle_missing()`     | Relleno o eliminación de valores nulos              |
| `convert_types()`      | Ajusta los tipos de columnas automáticamente        |
| `detect_constant_columns()` | Detecta columnas sin variabilidad               |
| `remove_outliers()`    | Elimina outliers en columnas numéricas              |

## 📁 Estructura del proyecto

```
datacleaner/
├── datacleaner/
|    └── __init__.py
|    └── cleaner.py
|    └── missing.py
|    └── types.py
|    └── constants.py
|    └── outliers.py
├── test/
|    └── pytest.py
├── scripts/
|    └── main.py
```

## 📌 Posibles mejoras

- Generación de reportes EDA automáticos
- Integración con visualizaciones básicas

## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT.

## 👤 Autor

Desarrollado por Troy Anthony Barker.
