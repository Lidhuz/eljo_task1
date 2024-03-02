from flask import Flask
from public import public
from master import master
from employee import employee

app=Flask(__name__)
app.secret_key="Hello"
app.register_blueprint(public)
app.register_blueprint(master,url_prefix='/master')
app.register_blueprint(employee,url_prefix='/employee')
app.run(debug=True,port=5002)