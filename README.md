# Python Modular Architecture & Best Practices

<div align="center">

<img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version" />
<img src="https://img.shields.io/badge/Architecture-Modular-success?style=for-the-badge&logo=diagram-next&logoColor=white" alt="Architecture" />
<img src="https://img.shields.io/badge/Code_Style-PEP8-informational?style=for-the-badge&logo=python&logoColor=white" alt="Code Style" />
<img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License" />

</div>

---

## Tabla de Contenidos

* [Visión General](#visión-general)
* [Principios de Diseño](#principios-de-diseño)
* [Arquitectura del Proyecto](#arquitectura-del-proyecto)
* [Instalación y Configuración](#instalación-y-configuración)
* [Guía de Uso](#guía-de-uso)
* [Estándares de Código](#estándares-de-código)
* [Contacto](#contacto)

---

## Visión General

Este repositorio alberga una colección de módulos, scripts y patrones de diseño orientados a la **Programación Modular en Python**. El objetivo principal es aplicar los principios **DRY** (*Don't Repeat Yourself*) y la **separación de responsabilidades** (SoC), estructurando el código de manera que sea desacoplado, testeable y fácilmente extensible.

---

## Principios de Diseño

El código desarrollado en este proyecto sigue directrices estrictas de ingeniería de software:

<table align="center">
  <tr>
    <th width="30%">Principio</th>
    <th width="70%">Descripción</th>
  </tr>
  <tr>
    <td><b>Modularidad</b></td>
    <td>División de la lógica de negocio en componentes independientes y reutilizables.</td>
  </tr>
  <tr>
    <td><b>Mantenibilidad</b></td>
    <td>Estructura clara de paquetes que facilita la depuración y actualización de funcionalidades.</td>
  </tr>
  <tr>
    <td><b>Escalabilidad</b></td>
    <td>Diseño preparado para la incorporación de nuevas herramientas sin romper la arquitectura base.</td>
  </tr>
  <tr>
    <td><b>Formato Clean Code</b></td>
    <td>Adherencia a estándares PEP 8, documentado mediante docstrings y uso estricto de <i>type hinting</i>.</td>
  </tr>
</table>

---

## Arquitectura del Proyecto

```text
Python_ProgramacionModular/
│
├── src/                    # Código fuente principal
│   ├── core/               # Lógica de negocio y algoritmos base
│   ├── utils/              # Funciones auxiliares e utilidades comunes
│   └── __init__.py         # Marcador de paquete Python
│
├── tests/                  # Pruebas unitarias e integración
│   └── test_modules.py
│
├── main.py                 # Punto de entrada principal (Entrypoint)
├── requirements.txt        # Dependencias del proyecto
└── README.md               # Documentación del repositorio
```

---

## Instalación y Configuración

### Prerrequisitos

* **Python 3.10** o superior instalado en el sistema.
* **Git** para el control de versiones.

### Paso a paso

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/paconino1/Python_ProgramacionModular.git
   cd Python_ProgramacionModular
   ```

2. **Crear y activar un entorno virtual (Recomendado):**

   *En Linux/macOS:*
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   *En Windows:*
   ```cmd
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Instalar dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

---

## Guía de Uso

Para ejecutar el programa principal y verificar la ejecución de los módulos:

```bash
python main.py
```

### Ejemplo de Importación Modular

```python
# Ejemplo de uso de módulos de la arquitectura
from src.core.processor import process_data
from src.utils.helpers import format_output

def run():
    raw_data = [10, 20, 30]
    result = process_data(raw_data)
    print(format_output(result))

if __name__ == "__main__":
    run()
```

---

## Estándares de Código y Calidad

Para garantizar la calidad técnica del repositorio se aplican las siguientes prácticas:

* **Type Hinting:** Declaración explícita de tipos de datos para funciones y parámetros.
* **Docstrings:** Documentación estructurada en estilo Google/NumPy para describir módulos y funciones.
* **Manejo de Excepciones:** Control exhaustivo de errores en módulos clave.

---

## Contacto

**Desarrollador:** [paconino1](https://github.com/paconino1)  
**Proyecto:** Python Modular Architecture