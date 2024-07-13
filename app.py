from flask import Flask, render_template
from flask import request
import logging
import time

tested = 0
sick = 0
inconclusive = 0

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


@app.route('/', methods=['GET', 'POST'])
def index():
   """
   Route for handling GET and POST requests on the '/' endpoint. Renders the 'index.html' template.
   """
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
    return render_template('healthbenifits.html')

@app.route('/currentstats/percents', methods=['GET'])
def pcurrentstats():
  """
  Route for handling GET requests related to religious matters for vegetarians. Renders the 'preligousmatters.html' template.
  """
  return render_template('pcurrentstats.html')

@app.route('/currentstats/rawnumbers', methods=['GET'])
def ncurrentstats():
  """
  Route for handling GET requests related to religious matters for vegetarians. Renders the 'nreligousmatters.html' template.
  """
  return render_template('ncurrentstats.html')

@app.route('/vegetarian/religousmatters/', methods=['GET'])
def religousmatters():
  """
  Route for handling GET requests related to religious matters for vegetarians. Renders the 'religousmatters.html' template.
  """
  return render_template('religousmatters.html')

@app.route('/vegetarian/vegan/', methods=['GET'])
def vegan():
  """
  Route for handling GET requests related to vegan information.
  Renders the vegan.html template.
  """
  return render_template('vegan.html')

@app.route('/animallove/pets/', methods=['GET'])
def pets():
  """
  Route for handling GET requests related to pets. Renders the 'pets.html' template.
  """
  return render_template('pets.html')

@app.route('/aboutdev/', methods=['GET'])
def aboutdev():
  """
  Route for handling GET requests related to the developer. Renders the 'aboutdev.html' template.
  """
  return render_template('aboutdev.html')

@app.route('/currentstats/', methods=['GET'])
def currentstats():
  """
  Route for handling GET requests related to the current stats. Renders the 'currentstats.html' template.
  """
  return render_template('currentstats.html')

@app.route('/animallove/theirhome/', methods=['GET'])
def theirhome():
  """
  Route for handling GET requests related to their home. Renders the 'theirhome.html' template.
  """
  return render_template('theirhome.html')

@app.route('/animallove/zoochosis/', methods=['GET'])
def zoochosis():
  """
  Route for handling GET requests related to zoochosis. Renders the 'zoochosis.html' template.
  """
  return render_template('zoochosis.html')

if __name__ == '__main__':
    app.run(debug=True)

