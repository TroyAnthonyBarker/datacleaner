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
from datacleaner import na_handler

df = pd.read_csv("datos.csv")

df_limpio = na_handler(df, stratage="next")
```

## 🔧 Funciones principales

| Función                | Descripción                                         |
|------------------------|-----------------------------------------------------|
| `na_handler()` | Relleno o eliminación de valores nulos |
| `fill_mean()` | Relleno de valores nulos con la media |
| `fill_median()` | Relleno de valores nulos con la mediana |
| `fill_mode()` | Relleno de valores nulos con el valor más común |
| `fill_previous()` | Relleno de valores nulos con el valor anterior |
| `fill_next()` | Relleno de valores nulos con el valor siguiente |
| `fill_interpolate()` | Relleno de valores nulos con el valor calculado basándose en los valores adyacentes, asumiendo una relación lineal entre ellos |
| `convert_to_datetime()` | Esta función intenta convertir la Serie al formato de fecha y hora, convirtiendo los errores en NaN |
| `convert_to_numeric()` | Esta función intenta convertir la Serie a formato numérico, convirtiendo los errores en NaN |
| `encode_labels()` | Esta función convierte la Serie a un tipo categórico y luego codifica las categorías como códigos numéricos |

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
|    └── pytest.ini
|    └── test_data_types.py
|    └── test_na_manager.py
├── scripts/
|    └── main.py
├── LICENSE
├── README.md
├── requirements.txt
└── setup.py
```

## ⚙️ Desarrollo

1. Clona este repositorio
2. Crea un entorno virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   ```
3. Instala las dependencias de desarrollo:
   ```bash
   pip install -r requirements.txt
   ```
4. Instala el paquete en modo desarrollo:
   ```bash
   pip install -e .
   ```

## 🦺 Ejecutar Pruebas

```bash
pytest
```

## 😊 Buenas Prácticas Implementadas

1. **Modularidad**: Separación de responsabilidades en módulos
2. **Documentación**: Docstrings detallados para métodos
3. **Pruebas**: Cobertura completa de pruebas unitarias
4. **Manejo de Errores**: Validación de entrada y manejo de excepciones
5. **Código Limpio**: Nombres descriptivos y estructura clara


## 📌 Posibles mejoras

- Generación de reportes EDA automáticos
- Integración con visualizaciones básicas

## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT.

## 👤 Autor

Desarrollado por Troy Anthony Barker.
