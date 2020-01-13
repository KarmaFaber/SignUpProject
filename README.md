# Sign Up 

Sign up project in pro and basic version.

## Built With

* [Visual Studio Code](https://code.visualstudio.com/) - Windows 10 version.  
* [Xampp](https://www.apachefriends.org/es/index.html). 

### Project parts
The main difference between the two versions lies in the use of graphic interface and modules to maintain a clean and tidy code.
* sign_up_pro
* sign_up_user_basic

### Special modules
* <b>class_sql</b>:
<br/><i>sql</i>=database_host, server_username, server_password, database_name
     - insert_query(sql) -server connection
     - select_query(sql) -mysql queries

* <b>format_check</b> - functions to check string formats:
     - check_email(string)
     - empty_check(string)
     - size_check(string)
     - lov_check(string)
     - cap_check(string)
     - num_check(string)
     - char_check_1(string) -> (re library)
     - char_check_2(string) -> (string library)
* <b>random_string_creator</b> -   :
     - ig_generator()
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

* **Karma Faber** 

## Versions:
* <b>version 1.0</b> - Operational Version. In the test I discovered an error in the encryption of the password. Format check restructuring because it does not work as desired.
* <b>version 1.1</b> - Operational Version. Password is entered into the database without encryption and format_checker.



