# Exotic-Bay

An e-commerce web app created for the COMPSCI2021 Web App Development group project coursework at the University of Glasgow.

### Examine project

This project is currently hosted at https://ansfarooq.pythonanywhere.com/. You must log in or sign up to access the watchlist and basket.

### Running this project

To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

```
pip install virtualenv
```

Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

```
virtualenv env
```

That will create a new folder `env` in your project directory. Next activate it with this command on mac/linux:

```
source env/bin/active
```

Then install the project dependencies with

```
pip install -r requirements.txt
```

Now you can run the project with this command

```
python manage.py runserver
```

## Built With

* [Django](https://www.djangoproject.com/) - The Python web framework used
* [Bootstrap 4](https://getbootstrap.com/) - Front-end framework
* [AllAuth](https://django-allauth.readthedocs.io/en/latest/index.html) - Web app authentication


## Authors

* [**Ans Farooq**](https://github.com/ansfarooq7)
* [**Stephen Graham**](https://github.com/Stephen00)
* [**Tom Anderson**](https://github.com/TomAnderson0)
* [**Daniyal Khan**](https://github.com/Daniyal6197)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
