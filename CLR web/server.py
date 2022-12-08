
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, Flask
)
# from Parser.firstfollow import State
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

        items, sym_list, clr_items, goto_list, input_test = main(grammars=string, Input=to_parse)
        print(f"{items=}")

        return render_template('cannonical.html', dictionary=items, symbols= sym_list, goto_list=goto_list, clr_items = clr_items, input_test=input_test)
    return render_template('cannonical.html') 