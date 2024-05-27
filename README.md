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
Welcome to the Django Job Board project! This project provides a job board application built with Django. This README will guide you through the steps required to set up and run the project locally.

## Setup and Run with Docker

### Prerequisites

- [Docker installed on your machine](https://docs.docker.com/engine/install/).
- Docker Compose installed on your machine.

### Steps

1. Clone the repository:
    ```sh
    git clone https://github.com/mgithens/jobboard.git
    cd jobboard
    ```

2. Build and run the Docker container:
    ```sh
    docker-compose up --build
    ```

3. Open your web browser and navigate to `http://0.0.0.0:8000`.

### Creating a Superuser

The setup script will automatically create a superuser with the following credentials:
- Username: admin
- Password: admin
- Email: admin@example.com

### Stopping the Container

To stop the Docker container, press `Ctrl+C` in the terminal where Docker is running or run:
    ```sh
    docker-compose down
    ```

## Admin Login for listing Jobs & Viewing Applications
Browse to [http://0.0.0.0:8000/admin](http://0.0.0.0:8000/admin) and login with a Username of `admin` and Password of `admin`


