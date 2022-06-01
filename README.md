# PasswordManager

Are you looking for a lightweight but practical OS agnostic application for your daily password management? PasswordManager provides several handy features, such as a friendly GUI for a user, keeping your secrets in a place you can easily access, and automatic password generation. PasswordManager can be one of the best choices in your pocket. 
Try it now!

## Preview

#### PasswordManager GUI

![app preview](https://user-images.githubusercontent.com/4502089/162113351-0cc985b4-3212-4402-babd-38f2f19ac269.PNG)

#### PasswordManager Unitest

![app test](https://user-images.githubusercontent.com/4502089/162113384-93884f2f-c427-4289-8e26-292b45c8a274.PNG)

## Quick-start

You can run PasswordManager on your local Windows/Mac/Linux environment with Python3+ installed. 

We can categorize the use scenarios of PasswordManager into 2 cases. 
1. Normal Flow 
2. UnitTest Flow (Whitebox testing)

### Normal Flow 

a. In your OS command prompt, enter 
```
$ python src\password_manager_main.py
```

b. The PasswordManager GUI will pop up to wait for users to enter their credential info such as Website URL, email, and password

c. Users can either click the *Generate Password* button to have the automatically-generated password or fill out their password manually. 

d. Once you are satisfied with the info you fill in, you can just click the button of *Add* to save all data into my_password.txt, which is the place to store all your secrets.

e. Since in the most use scenarios, users would use the same email for your new website registration, PasswordManager presets a default password by a global variable called *DEFAULT_EMAIL* in *src\password_manager_main.py*. Users can freely change it to save the repetitive effort of inputting the same email address.  


### UnitTest/Pytest Flow
a.  In your OS command prompt, enter 
```
$ pytest tests\test_password_manager.py
```

b.  Python UnitTest verifies each method of PasswordManager class to report PASS/FAILED results. 

Notes: 

- In some situations, to make pytest work, you will need to create a new Variable called 
**PYTHONPATH** in your OS, for example, in Windows:
```
set PYTHONPATH=src
```

## Python Dependencies

Please refer to requirements.txt and install all the required packages by 
```
$ pip install -r requirements.txt
```

## License

It is distributed under the Apache License. See LICENSE.txt for more information.

## Contact

Kana Kunikata

## Acknowledgments

- Thanks for the ideas from Angela's 100 Days of Code: The Complete Python Pro Bootcamp for 2022 on Udemy
- Thanks [**Paul Yang**](https://github.com/paulyang0125) for his technical peer review to guide me to know the best-known practices for clean code, OSS release process, and agile methodology.    
