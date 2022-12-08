
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, Flask
)

from Parser.clr import main
# from Parser import firstfollow
from Parser.firstfollow import production_list, nt_list as ntl, t_list as tl
from Parser.clr import nt_list, t_list
# from CLR_Parser.firstfollow import 
app = Flask(__name__)


@app.route("/", methods=("GET", "POST"))
def hello_world():
    string = 'asdf'
    if request.method == 'POST':
        string = request.form['grammar'].replace("\r", "").split("\n")
        to_parse = request.form['string']
        # string.append('')
        global production_list, tl, ntl, nt_list, t_list

        main(grammars=string)
        production_list, nt_list, t_list = list(), list(), list()
        tl, ntl  = dict(), dict()
        print(string)
        return render_template('cannonical.html', hello=string)
    return render_template('cannonical.html', hello="world")
        