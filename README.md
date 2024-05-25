# Django Job Board Web Application

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

## Introduction
This is a simple Django Job Board Application where users can view and apply for job listings.

## Installation
1. **Clone the repository:**
    ```sh
    git clone https://github.com/mgithens/jobboard.git
    cd jobboard
    ```

2. **Run the setup script:**
    ```sh
    ./setup.sh
    ```

   The `setup.sh` script will:
   - Check for Python and pip installations.
   - Check for and install `virtualenv` if necessary.
   - Create and activate a virtual environment.
   - Install the required dependencies.
   - Run database migrations.
   - Prompt to create a Django superuser.
   - Start the Django development server.

### Windows

1. **Clone the repository:**
    ```cmd
    git clone https://github.com/yourusername/jobboard.git
    cd jobboard
    ```

2. **Run the setup script:**
    ```cmd
    setup.bat
    ```

   The `setup.bat` script will:
   - Check for Python and pip installations.
   - Check for and install `virtualenv` if necessary.
   - Create and activate a virtual environment.
   - Install the required dependencies.
   - Run database migrations.
   - Prompt to create a Django superuser.
   - Start the Django development server.

## Scripts Overview

### `setup.sh` (Unix-based Systems)

```bash
#!/bin/bash

# Check if manage.py exists in the current directory
if [ ! -f manage.py ]; then
    echo "Error: manage.py not found in the current directory."
    exit 1
fi

# Check if Python is installed and its version
PYTHON_CMD=""
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "Error: Python is not installed. Please install Python 3.6 or higher."
    exit 1
fi

PYTHON_VERSION=$($PYTHON_CMD -c "import sys; print('.'.join(map(str, sys.version_info[:3])))")
if [[ $PYTHON_VERSION < "3.6" ]]; then
    echo "Error: Python version 3.6 or higher is required. Found version $PYTHON_VERSION."
    exit 1
fi

echo "Using $PYTHON_CMD (version $PYTHON_VERSION)"

# Check if pip is installed
if ! command -v pip3 &> /dev/null && ! command -v pip &> /dev/null; then
    echo "Error: pip is not installed. Please install pip."
    exit 1
fi

# Use pip3 if available, otherwise use pip
PIP_CMD="pip"
if command -v pip3 &> /dev/null; then
    PIP_CMD="pip3"
fi

echo "Using $PIP_CMD"

# Check if venv is installed
if ! $PYTHON_CMD -m venv --help &> /dev/null; then
    read -p "Python venv module is not installed. Do you want to install it? (y/n): " install_venv
    if [[ $install_venv == [Yy] ]]; then
        $PIP_CMD install virtualenv
    else
        echo "Error: venv is required to proceed."
        exit 1
    fi
fi

# Create a virtual environment if not already present
if [ ! -d "venv" ]; then
    $PYTHON_CMD -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
$PIP_CMD install -r requirements.txt

# Perform database migrations
$PYTHON_CMD manage.py migrate

# Create superuser (admin user)
read -p "Do you want to create a Django superuser? (y/n): " create_superuser
if [[ $create_superuser == [Yy] ]]; then
    read -p "Enter admin username: " admin_username
    read -p "Enter admin email: " admin_email
    read -s -p "Enter admin password: " admin_password
    echo ""
    echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('$admin_username', '$admin_email', '$admin_password')" | $PYTHON_CMD manage.py shell
fi

# Run the development server
$PYTHON_CMD manage.py runserver