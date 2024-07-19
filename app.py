herokufrom flask import Flask, render_remplate
#from flask import Flask, render_template//replace line 1 with this line when not using heroku (web api)
from flask import request
import logging
import time

var = True

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


@app.route('/', methods=['GET', 'POST'])
def index():
   """
   Route for handling GET and POST requests on the '/' endpoint. Renders the 'index.html' template.
   """
   if var == True:
    return render_template ('index.html')

@app.route('/vegetarian/healthbenifits/', methods=['GET'])
def healthbenifits():
    """
    This function is a route handler for the '/vegetarian/healthbenifits/' endpoint. It handles HTTP GET requests
    and renders the 'healthbenifits.html' template.

    Parameters:
    None

    Returns:
    The rendered 'healthbenifits.html' template.
    """
    if var == True:
      return render_template('healthbenifits.html')

@app.route('/currentstats/percents', methods=['GET'])
def pcurrentstats():
  """
  Route for handling GET requests related to religious matters for vegetarians. Renders the 'preligousmatters.html' template.
  """
  if var == True:
    return render_template('pcurrentstats.html')

@app.route('/currentstats/rawnumbers', methods=['GET'])
def ncurrentstats():
  """
  Route for handling GET requests related to religious matters for vegetarians. Renders the 'nreligousmatters.html' template.
  """
  if var == True: 
    return render_template('ncurrentstats.html')

@app.route('/vegetarian/religousmatters/', methods=['GET'])
def religousmatters():
  """
  Route for handling GET requests related to religious matters for vegetarians. Renders the 'religousmatters.html' template.
  """
  if var == True:
    return render_template('religousmatters.html')

@app.route('/vegetarian/vegan/', methods=['GET'])
def vegan():
  """
  Route for handling GET requests related to vegan information.
  Renders the vegan.html template.
  """
  if var == True:
    return render_template('vegan.html')

@app.route('/animallove/pets/', methods=['GET'])
def pets():
  """
  Route for handling GET requests related to pets. Renders the 'pets.html' template.
  """
  if var == True:
    return render_template('pets.html')

@app.route('/aboutdev/', methods=['GET'])
def aboutdev():
  """
  Route for handling GET requests related to the developer. Renders the 'aboutdev.html' template.
  """
  if var == True:
    return render_template('aboutdev.html')

@app.route('/currentstats/', methods=['GET'])
def currentstats():
  """
  Route for handling GET requests related to the current stats. Renders the 'currentstats.html' template.
  """
  if var == True:
    return render_template('currentstats.html')

@app.route('/animallove/theirhome/', methods=['GET'])
def theirhome():
  """
  Route for handling GET requests related to their home. Renders the 'theirhome.html' template.
  """
  if var == True:
    return render_template('theirhome.html')

@app.route('/animallove/zoochosis/', methods=['GET'])
def zoochosis():
  """
  Route for handling GET requests related to zoochosis. Renders the 'zoochosis.html' template.
  """
  if var == True:
    return render_template('zoochosis.html')

@app.route('/devreq', methods=['GET'])
def devreq():
  """
    Handle the POST request for the '/devreq' route.

    Check the password response and render different templates based on the response.

    Parameters:
        None

    Returns:
        The rendered template for the '/conclusion.html' route if the password is correct,
        otherwise the rendered template for the '/devreqdenied.html' route.
  """
  global pwdresponse
  pwdresponse = request.form['pwd'] #should be 1452

  if float(pwdresponse) == float(1452):
    return render_template('conclusion.html', var=var)
  
  else:
    return render_template('devreqdenied.html')

@app.route('/devpage', methods=['GET'])
def conclusion():
    """
    Function to define the /devpage route of the app. Uses method POST
    """
    return render_template('devpage.html', var=var)

@app.route('/devloginpage', methods=['GET'])
def devloginpage():
   """
   Handle the GET request for the '/developer' route with methods ['GET'].
   This function renders the 'developerpage.html' template.
   """
   return render_template('devloginpage.html')

def changeValuesAndRedirect():
  var = False
  return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

