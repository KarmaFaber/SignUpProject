# Sign Up 

Sign up project in pro and basic version.

## Built With

* [Visual Studio Code](https://code.visualstudio.com/) - Windows 10 version.  
* [Xampp](https://www.apachefriends.org/es/index.html). 

### Project parts
The main difference between the two versions lies in the use of graphic interface and modules to maintain a clean and tidy code.
* sign_up_pro
* sign_up_user_basic

### Special modules: MyPyModule
* <b>class_sql</b>:
<br/><i>#sql</i>=database_host, server_username, server_password, database_name
     - insert_query(sql) -server connection
     - select_query(sql) -mysql queries
* <b>encrypt</b>:
     - encrypt_password_md5(password):

* <b>random_string_creator</b>:
     - password_generator()


### Python libraries used
* email_validator
* pillow
* pymysql
* random
* string
* tkinter


### DataBase MySQL
CREATE DATABASE <b>proyect</b>;
<br/>CREATE TABLE <b>user</b> (<b>email</b> varchar (50), <b>password</b> varchar(100), PRIMARY KEY(email));

## Contributing

This project is made for educational purposes, GitHub users are free to download and use it freely.

## Author

* [Karma Faber](https://www.linkedin.com/in/maria-zolotarova/). 

## Versions:
* <b>version 1.0</b> - Operational Version. In the test I discovered an error in the encryption of the password. Format check restructuring because it does not work as desired.
* <b>version 1.1</b> - Operational Version. Password is entered into the database without encryption and format_checker.
* <b>version 1.2</b> - Operation Version.  - encript module - fixed

  
  



