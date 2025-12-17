# 📊 Predicción de Series Temporales con ML y DL

Este repositorio contiene la implementación de modelos de **Machine Learning (ML)** y **Deep Learning (DL)** para la predicción de series temporales. Se utilizan modelos como **ARIMA-GARCH, Prophet, XGBoost, Redes Recurrentes y NeuralProphet**, junto con criterios de hibridación asociados a las predicciones híbridas.

## 📁 Estructura del Proyecto

```
📂 data/
│── 📂 best_parameters/   # Conjunto de mejores hiperparámetros asociados a cada modelo
│── 📂 csv/               # archivos csv que contienen los datos por divisa
│    ├── Carga de datos Lakehouse.ipynb # creación de tablas (dataframes / tablas delta)
📂 models/
│── 📂 notebooks/         # Código fuente (notebooks asociados a cada modelo)
│    ├── main.py          # Script principal
📂 src/
│    ├── main.py
📂 utils/                # funciones adicionales
│    ├── functions.py
│── .gitignore            # Ignorar archivos innecesarios
│── requirements.txt      # Lista de dependencias
│── readme.md             # Documentación del proyecto

```

## 🚀 Instalación

### 1️⃣ **Clonar el repositorio**

```sh
git clone https://github.com/usuario/tu_proyecto.git
cd tu_proyecto
```

### 2️⃣ **Crear y activar el entorno virtual**

- **Windows**:
  ```sh
  python -m venv venv_tesis
  venv_tesis\Scripts\activate
  para desactivarlo: deactivate
  ```
- **Mac/Linux**:
  ```sh
  python3 -m venv venv_tesis
  source venv_tesis/bin/activate
  ```

### 3️⃣ **Instalar dependencias**

```sh
pip install -r requirements.txt
```

## 📦 Dependencias

Este proyecto usa las siguientes librerías principales:

- **Manipulación de datos**: `pandas`, `numpy`
- **Machine Learning**: `scikit-learn`, `xgboost`
- **Deep Learning**: `tensorflow`, `keras`, `torch`
- **Series Temporales**: `statsmodels`, `neuralprophet`, `pmdarima`, `sktime`
- **Datos financieros**: `yfinance`
- **Seguimiento de experimentos**: `optuna`

## 📜 Licencia

Este proyecto está bajo la licencia **MIT**.

---
