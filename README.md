# Python-Full-Stack-Development
This project focuses on Django, HTML, CSS and JavaScript. 
The task is to build different dashboards using Chart.js/ D3.js/ plotly.js, etc. 
The data is provided in the form of json file. 
**Procedure**:
The virtual environment is created along with the project and app.
The JSON file is read in a management->commands->import_json.py folder under the app folder. 
Django model is created for all the fields.
Django views helps in the connectivity of the database, templates. Hence request is made to connect the database and the templates.
The urls.py under the app folder calls the views.py, and the urls.py under the project folder calls the urls.py under the app folder.
The template is the html body for the frontend, where data will be called with the help of JS, and charts will be made according to the data.
