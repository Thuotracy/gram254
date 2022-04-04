# Gram254

## Author
### [Tracy Wangari]
## Description
This is an instagram clone

## Setup Instructions:
### Requirements

##### 1. Clone the repository
Clone the the repository by running

   ```bash
   git clone https://github.com/Thuotracy/gram254.git
   ```
 or download a zip file of the project from github


Navigate to the project directory
```bash
cd gram254
```

##### 2. Create a virtual environment
 To create a virtual environment named `virtual`, run

   ```prettier
   virtualenv virtual
   ```
To activate the virtual environment we just created, run

   ```bash
   source virtual/bin/activate
   ```
##### 3. Create a django and create django projects
 Install django
 ```bash
 pip install django
  ```
  Create django project
  ```bash
  django-admin startproject insta .
```
create a tracy app
 ```bash
 django-admin startapp account
 ```



##### 5. Create a database
You'll need to create a new postgress database, Type the following command to access postgress
   ```bash
    $ psql
   ```
   Then run the following query to create a new database named ```instagramclone```
   ```
   # create database instagramclone
   ```


#####  4.Install dependencies
To install the requirements from `requirements.txt` file,

   ```prettier
   pip install -r requirements.txt
   ```

#####  5.Create Database migrations
Making migrations on postgres using django

```prettier
pmake makemigrations
```


then run the command below;

 ```bash
 make migrate
 ```

##### 6.Run the app
To run the application on your development machine,

    make serve

## Technologies Used
* Django
* Python
* Html
* Css
* Bootstrap3
* Django-Admin

## Bugs
like functionality is not working as expected

## License
[![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](http://opensource.org/licenses/MIT)
>MIT license &copy;  2022 Tracy

# Collaboration Information
* Clone the repository
* Make changes and write tests
* Push changes to github
* Create a pull request

# Contacts
tracyjacobs775@gmail.com