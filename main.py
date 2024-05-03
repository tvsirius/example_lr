"""
Sample flask application with index.html and welcome.html pages

index.html: simple html file with "Hello World!" text, image (img/MIT.png) 
and a form field with "Name:" field, and "Submit" button, sending a POST request to welcome.html

welcome.html: simple html file with "Hello <username>!" text and image (img/MIT.png), 
response from POST request with Name data.

String with Name is processed with str.title()

All code is simple flask routines, providing required functionality 

Author: tvsirius
Date: 2024-04-29
"""

import flask

from linear_regression import process_linear


app = flask.Flask(__name__, static_folder='static')


def my_basic_computation(data_string, degree_string, x_val: str) -> str:
    """This function provides a way to see how a computation with input data is integrated
    into Flask web application.

    Args:
        input (str): Some string user will input to the field "input" in the HTML form

    Returns:
        str: String with the result of your computation
    """
    # If you want to do some data processing, or converting a string to int or float,
    # you can do it here
    # You can add a check that can return error message in result_string
    # instead of results, if input_string is not valid
    # (note: you can specify data format if HTML form, but additional check will not do wrong)

    # Here I just use str.title() for capitalizing
    result_string = process_linear(data_string, degree_string, x_val)

    # result_string will be send to output HTML, that user will receive
    return result_string

#This decorator tells flask that the function index_page() will process request to '/'
@app.route('/')
def index_page():
    """Render the index.html page.
    This function is called when flask receives a GET request to '/' endpoint

    Returns:
        str: Rendered HTML content of the index.html page.
    """
    return flask.render_template('index.html', processed_data1='')

#This decorator tells flask that the function computation_page() will process POST request to '/computation'
@app.route('/computation', methods=['POST'])
def computation_page():
    """Render the computation html page with the processed input from the form.
    This function is called when flask receives a POST request to '/computation' endpoint  
    with this function will be able to get the data of the request, including the inputs of the form that sends this request 

    Returns:
        str: Rendered HTML content of the index.html page with the processed input data.
    """
    # Here we take the string from the input filed in form of the HTML file
    # In the POST form of HTML there is:
    # <input type="text" id="name" name="input_data1" required>
    # where name="input_data1" specify how you will address the data in POST request
    # that we are processing now

    input_data = flask.request.form['input_data']
    input_degree = flask.request.form['input_degree']
    input_xval = flask.request.form['input_xval']

    # Apply desired computation
    processed_data1 = my_basic_computation(input_data, input_degree, input_xval)

    # this method renders the HTML template, using our data
    # inside the HTML template the string {{ processed_data1 }} will be replaced with
    return flask.render_template('index.html', processed_data1=processed_data1)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
