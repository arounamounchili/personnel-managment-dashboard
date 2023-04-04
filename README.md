# personnel-managment-dashboard

The objective of this project is to develop a personnel management dashboard for a fictitious company which should store the data of job applicants in a database in an intuitive way and allow easy editing of the data of each person. It should allow filtering of the information contained in the dashboard.

![Dashboard-Design](assets/Dashboard.jpg)

## Setting Up the Project

### Create a project folder

```
mkdir my-projet && cd my-project
```

### Install virtualenv

```
pip install virtualenv
```

### Create, activate the virtual environment and install PySide6 - Windows

```
virtualenv env
source \env\Scripts\activate
pip install pyside6
```

### Create, activate the virtual environment and install PySide6 - MacOS/Linux

```
virtualenv env
source env/bin/activate
pip install pyside6
```

### How to deactivate virtualenv

```
deactivate
```

### Check the PySide version

```python
import PySide6
PySide6.__version__
```
