#!/bin/bash
# This bash script was AI generated. Please let me know if you run into any issues.


# Function to check if command exists
command_exists() {
    command -v "$1" &> /dev/null
}

# Check if manage.py exists in the current directory
if [ ! -f manage.py ]; then
    echo "Error: manage.py not found in the current directory."
    exit 1
fi

# Check if Python is installed and its version
PYTHON_CMD=""
if command_exists python3; then
    PYTHON_CMD="python3"
elif command_exists python; then
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
if ! command_exists pip3 && ! command_exists pip; then
    echo "Error: pip is not installed. Please install pip."
    exit 1
fi

# Use pip3 if available, otherwise use pip
PIP_CMD="pip"
if command_exists pip3; then
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
