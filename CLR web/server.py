
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, Flask
)
# from Parser.firstfollow import State
from Parser.clr import main
# from Parser import firstfollow
import os
from Parser.firstfollow import production_list, nt_list as ntl, t_list as tl
from Parser.clr import nt_list, t_list
# from CLR_Parser.firstfollow import
app = Flask(__name__)
LOGO = os.path.join('static', 'Group_1.png')
# app.config['UPLOAD_FOLDER'] = LOGO

app = Flask(__name__)


@app.route("/", methods=("GET", "POST"))
def hello_world():
    string = 'asdf'

    if request.method == 'POST':
        grammar = request.form['grammar']
        string = grammar.replace("\r", "").split("\n")
        to_parse = request.form['string']
        print(request.form)
        # string.append('')
        global production_list, tl, ntl, nt_list, t_list, first_list, follow_list

        items, sym_list, clr_items, goto_list, first_list, follow_list, input_test, string_validity, conflict = main(
            grammars=string, Input=to_parse)
        print(f"{items=}")
        return render_template('cannonical.html',
                               dictionary=items,
                               clr_items=clr_items,
                               symbols=sym_list,
                               goto_list=goto_list,
                               first_list=first_list,
                               follow_list=follow_list,
                               input_test=input_test,
                               grammar=grammar,
                               string_validity=string_validity,
                               conflict=conflict
                               )
                            
    return render_template('cannonical.html', hello="world")
