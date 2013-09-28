import os
from distutils.core import setup

os.putenv('TAR_OPTIONS', '--owner root --group root --mode a+rX')

setup(
    name = 'food_gui',
    version = '1.2.1',
    license = 'GPL',
    description = 'A simple calculator, that calculates proteins, fats, carbohydrates, food energy and glycemic index',
    url = 'https://github.com/arcan1s/food_gui',
    author = 'Evgeniy Alekseev',
    author_email = 'esalexeev@gmail.com',
    packages = ['food_gui'],
    py_modules = ['food_gui']
)
