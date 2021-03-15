# masglobal_handsontest
_This repository contains a Python hands-on test sent by mas global consulting_


## Requirements:
- Django              3.1.7    
- djangorestframework 3.12.2   
- pip                 20.0.2   
- requests            2.25.1   
- urllib3             1.26.3   

I recommend to run all the application in a virtual environment because is more easy to install libraries with required versions.

## Running Server:

After installing all required libraries, you go to the project folder and run the command:

```sh
python3 manage.py runserver
```

## API URL:

This server is running under localhost domain. By default django run in port 8000 if no port is specified. To open the API you need to open the next URL:

```sh
localhost:port_number/api/get_employees/
```

if you don't specify any ID, the API get all avaiable employees. You can specify the id as follows:

```sh
localhost:port_number/api/get_employees/?id=id_number
```

## View URL:

The view web page can be accessed in next URL:

```sh
localhost:port_number/view/get_employees/
```

If you specify an ID in the form, it will retrieve data from the employee with that ID. If you don't specify any ID the system will get all employes data.

## Unit Test:

This application have 7 unit test for testing the Business Logic. To run all unit test you need to run the next command:

```sh
python3 manage.py test employees_api.UnitTest.tests
```

If you want to run one specific test, you need to run the next command (replace "TestName" by the test you want to run):

```sh
python3 manage.py test employees_api.UnitTest.tests.TestName
```



