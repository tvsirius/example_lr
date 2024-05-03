"""
Module for linear_regression_function
Provides a implementation of linear regression function of desired degree.

Author: tvsirius
Date: 2024-05-02
"""
import numpy as np

def process_linear(data_string:str,degree:str,x_argument:str)->str:
    """Extracts data from the data_string to a array of floats, to numpy array of (X,Y) paris
    Convert degree to int value of linear regression degree.
    Fits linear regression model.
    Predicts Y value based on provided X value of the x_argument.
    In case of wrong input returns string "Error processing input"

    >>> process_linear("(1,1),(2,2),(3,3)","1","4")
    "4.000000000000001"
    
    >>> process_linear("(1,1.2),(2,2.8),(3,8.2)","2","4")
    "17.400000000000016"
    
    >>> process_linear((4,3),"d","3")
    "Error processing input"

    Args:
        data_string (str): Data for linear regression in string format like (X,Y), like: "(2,4.3), (3,6), (4.2,9.2)"
        degree (str): String with degree of linear regression, in format int, form 1 to infinity, i
                      if degree<1 returns "Degree must be 1 or higher"
        x_argument (str): X Argument for linear regression to make a prediction

    Returns:
        str: Y predicted value, or "Error processing input", or "Degree must be 1 or higher" if there is an errors in inputs
    """
    
    # Step 1: Extract data points and convert to NumPy array
    try:
        data = np.array([list(map(float, pair.split(','))) for pair in data_string.strip('()').split('),(')])
        X = data[:, 0]
        Y = data[:, 1]
    except (ValueError, AttributeError):
        return "Error processing input"

    # Step 2: Convert degree to int
    try:
        degree_int = int(degree)
        x_value = float(x_argument)
    except ValueError:
        return "Error processing input"
    
    if degree_int<1:
        return "Degree must be 1 or higher"

    # Step 3: Fit linear regression model
    coeffs = np.polyfit(X, Y, degree_int)
    poly = np.poly1d(coeffs)

    # Step 4: Predict Y value
    y_pred = poly(x_value)

    
    # Step 5: check for error, if Y is valid
    try:
        _ = float(str(y_pred))
    except ValueError:
        return "Error processing input"

    # Step 6: Return predicted Y value as a string
    return str(y_pred)
    