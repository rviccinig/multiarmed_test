#App.py file is where the CORE of the applications is#There are thre components
#This file is basically just going to have a single line importing the __init.py from the multiarmed_test folder

from multiarmed_test import app


if __name__ == '__main__':
    app.run(debug=True)
