
# Guía de Instalación y Ejecución del Proyecto (Python + Pandas + Matplotlib)

Este documento explica paso a paso cómo clonar, configurar y ejecutar este proyecto en **Visual Studio Code (VSCode)** utilizando **Python 3**, las librerías necesarias, y las extensiones recomendadas.

---

## ✅ 1. Requisitos previos

Antes de comenzar, asegúrate de tener instalado:

### A) Python 3
Puedes descargarlo desde:
https://www.python.org/downloads/

Durante la instalación marca la opción:
```
Add Python to PATH
```

Para verificar la instalación:
```bash
python --version
```
o en algunos sistemas:
```bash
python3 --version
```

---

### B) Git (para clonar repositorios)
Descargar desde:
https://git-scm.com/downloads

Verifica que funciona:
```bash
git --version
```

---

### C) Visual Studio Code
Descarga desde:
https://code.visualstudio.com/

---

## 🧩 2. Extensiones recomendadas en VSCode

Dentro de VSCode, instala:

| Extensión | Propósito |
|----------|-----------|
| **Python** (Microsoft) | Soporte para ejecución, debugging y formateo |
| **Pylance** | Análisis inteligente de código |
| **Jupyter** | Ejecución de notebooks (opcional) |
| **GitHub Pull Requests** | Integración con GitHub |

Puedes instalarlas desde la pestaña **Extensions** (Ctrl+Shift+X).

---

## 📥 3. Clonar el repositorio

Abre una terminal y ejecutá:

```bash
git clone https://github.com/MMRichter/TP-Proba.git
```

(⚠️ Reemplazá la URL por la de tu repositorio real)

Luego ingresá a la carpeta:

```bash
cd TP-Proba
```

---

## 🐍 4. Crear entorno virtual (RECOMENDADO)

Esto permite aislar las librerías del proyecto:

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

Linux / Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```

Verás `(venv)` en la terminal indicando que está activo.

---

## 📦 5. Instalar dependencias necesarias

Ejecutá:

```bash
pip install pandas matplotlib
```

> Si tenés un archivo `requirements.txt` podés usar:
```bash
pip install -r requirements.txt
```

---

## 📂 6. Abrir el proyecto en VSCode

Desde la terminal:
```bash
code .
```

O abrilo manualmente desde VSCode → *File → Open Folder…*

---

## ⚙️ 7. Seleccionar intérprete de Python en VSCode

Presioná:
```
Ctrl + Shift + P
```
Escribí:
```
Python: Select Interpreter
```
Elegí el que diga:
```
./venv/bin/python
```
o
```
./venv/Scripts/python.exe
```

---

## ▶️ 8. Ejecutar el script principal

Podés correrlo desde:

### Terminal:
Windows:
```bash
python app.py
```

Linux/Mac:
```bash
python3 app.py
```

### VSCode
Arriba a la derecha presioná el botón **Run** (flecha verde)

---

## 📊 9. Sobre el proyecto

Este proyecto utiliza:

- **pandas** → análisis y manipulación de datos
- **matplotlib** → generación de gráficos

El código cargará los datasets necesarios y generará gráficos estadísticos según la lógica implementada en `app.py` o los módulos correspondientes.

---

## 🔁 10. Actualizar el repositorio (pull)

Si tus compañeros hacen cambios:

```bash
git pull
```

---

## 🚀 11. Contribuir al proyecto

Para subir cambios:

```bash
git add .
git commit -m "Descripción de cambios"
git push
```

---

## 🧪 12. Solución de problemas comunes

| Problema | Solución |
|----------|----------|
| VSCode no reconoce Python | Seleccionar intérprete correctamente |
| `pip` no instala librerías | Activar el entorno virtual |
| matplotlib no muestra gráficos | Usar `plt.show()` |

---

## 📌 Notas finales

- Siempre trabajar con el entorno virtual activo
- Hacer `git pull` antes de comenzar a trabajar
- Comentar código para facilitar el trabajo grupal

---

### 👨‍💻 Si algo falla…
Podés consultar:
- Documentación oficial de Pandas
- Documentación de Matplotlib
- Documentación de Python
- Comunidad de StackOverflow

---

¡Listo! Ya podés trabajar y ejecutar el proyecto correctamente. 🎉
