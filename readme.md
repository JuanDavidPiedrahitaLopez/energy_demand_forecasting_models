# 📊 Predicción de Series Temporales con ML y DL

Este repositorio contiene la implementación de modelos de **Machine Learning (ML)** y **Deep Learning (DL)** para la predicción de series temporales. Se utilizan modelos como **ARIMA, Prophet, XGBoost, Redes Neuronales (LSTM, GRU) y TimeGPT**, con integración de **PySpark y Apache** para el manejo de grandes volúmenes de datos.

## 📁 Estructura del Proyecto

```
📂 tu_proyecto/
│── 📂 src/               # Código fuente (scripts y módulos)
│    ├── main.py          # Script principal
│    ├── utils.py         # Funciones auxiliares
│── 📂 notebooks/         # Jupyter notebooks (si usas)
│── 📂 data/              # Datos crudos o de entrada (opcional)
│── 📂 models/            # Modelos entrenados (si decides guardarlos)
│── .gitignore            # Ignorar archivos innecesarios
│── requirements.txt      # Lista de dependencias
│── README.md             # Documentación del proyecto

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

## 📊 Uso del Proyecto

### 🔹 **Ejecutar el código principal**

```sh
python src/main.py
```

### 🔹 **Ejecutar un notebook Jupyter**

```sh
jupyter notebook
```

## 📦 Dependencias

Este proyecto usa las siguientes librerías principales:

- **Manipulación de datos**: `pandas`, `numpy`
- **Machine Learning**: `scikit-learn`, `xgboost`, `lightgbm`, `catboost`
- **Deep Learning**: `tensorflow`, `keras`, `torch`
- **Series Temporales**: `statsmodels`, `prophet`, `pmdarima`, `sktime`
- **Big Data**: `pyspark`, `apache-airflow`
- **Datos financieros**: `yfinance`, `pandas-datareader`, `alpha_vantage`
- **Seguimiento de experimentos**: `mlflow`, `optuna`

## 🛠 Contribución

Si deseas contribuir al proyecto:

1. **Haz un fork** del repositorio.
2. **Crea una nueva rama** con tu cambio (`git checkout -b nueva_funcionalidad`).
3. **Realiza un commit** (`git commit -m "Descripción del cambio"`).
4. **Haz push a la rama** (`git push origin nueva_funcionalidad`).
5. **Abre un Pull Request**.

## 📜 Licencia

Este proyecto está bajo la licencia **MIT**.

---
