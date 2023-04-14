# <p align="center"><a href="https://www.djangoproject.com" target="_blank"><img src="https://github.com/tjmacphee/COP3710-Internship-app/blob/main/django-logo.webp" width="400" alt="Django Logo"></a></p>

<img src="https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white" />
### Laravel codebase developed for IMAG to advance their aquatics archival & measurement-taking process(es).

----------

# Getting started

## Installation

Please check the official laravel installation guide for server requirements before you start. [Official Documentation](https://laravel.com/docs/10.x/installation)

Required for Installation:

    Composer (https://getcomposer.org/download/)
    NPM (https://nodejs.org/en/download)

***Note*** : You can quickly clone the project using the github desktop feature. Visit the link to learn more about that process. [Official Documentation](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/adding-and-cloning-repositories/cloning-a-repository-from-github-to-github-desktop)

Clone the repository

    git clone git@github.com:Board-Kanban-template/IMAG-LARAVEL-DASHBOARD.git

Switch to the repo folder

    cd imag-aquatics-app

Install all the dependencies using composer

    composer install
    
Install all the node modules using npm

    npm install

Copy the example env file and **make the required configuration changes** in the .env file

    cp .env.example .env

Generate a new application key

    php artisan key:generate

Run the database migrations (**Set the database connection in .env before migrating**)

    php artisan migrate

Start the local development server

    php artisan serve --port=8080

You can now access the server at http://localhost:8000

**TL;DR command list**

    git clone git@github.com:Board-Kanban-template/IMAG-Aquatics-app.git
    cd iamg-aquatics-app
    composer install
    npm install
    cp .env.example .env
    php artisan key:generate
    
**Make sure you set the correct database connection information before running the migrations** [Environment variables](#environment-variables)

    php artisan migrate
    php artisan serve --port=8080

# Code overview

## Dependencies

## Folders

- `app` - Contains all the Eloquent models
- `app/Http/Controllers` - Contains all the web controllers
- `app/Http/Middleware` - Contains the auth middleware
- `app/Http/Requests` - Contains all the web form requests
- `config` - Contains all the application configuration files
- `database/factories` - Contains the model factory for all the models
- `database/migrations` - Contains all the database migrations
- `database/seeds` - Contains the database seeder
- `pulic` - Contains the public files & assets
- `resources` - Contains the hidden files/assets & views
- `routes` - Contains all the web routes defined in web.php file
- `tests` - Contains all the application tests

## Environment variables

- `.env` - Environment variables can be set in this file

***Note*** : You can quickly set the database information and other variables in this file and have the application fully working.

----------

# Testing Server

Run the laravel development server

    php artisan serve

The api can now be accessed at

    http://localhost:8080

----------

# Create a dummy user account

Access the web.php file in /routes

Change the email & pass to whatever you want, and goto the following address

    http://localhost:8080/create-user
    
You can now log in with those credentials

----------

# Connect mail services

Create an account at

    https://mailtrap.io

Head to the 'Email Testing' area & select laravel 7+ from the dropdown menu

<img width="1440" alt="Screenshot 2023-04-04 at 9 32 56 AM" src="https://user-images.githubusercontent.com/62121474/229810291-a98e54cd-2de7-4260-ad6d-29b288ed874b.png">
    
Copy the settings into your .env file, overwriting the existing mail settings

----------

Request headers

| **Required** 	| **Key**              	| **Value**            	|
|----------	|------------------	|------------------	|
| Yes      	| Content-Type     	| application/json 	|
| Yes      	| X-Requested-With 	| XMLHttpRequest   	|
| Yes      	| XSRF 	            | CSRF Token   	|

----------
