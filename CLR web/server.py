
from curses.ascii import isupper
from typing import Type
import os
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
LOGO = os.path.join('static', 'Group_1.png')
# app.config['UPLOAD_FOLDER'] = LOGO

app = Flask(__name__)


@app.route("/", methods=("GET", "POST"))
def hello_world():
    string = 'asdf'
    isError = False

    if request.method == 'POST':
        # for element in dir():
        #     if element[0:2] != "__":
        #         del globals()[element]
        # string = 'asdf'
        grammar = request.form['grammar']
        string = grammar.replace("\r", "").split("\n")
        to_parse = request.form['string']
        # string.append('')
        try:
            if '->' not in grammar:
                print('production error')
                raise TypeError('error')
            else:
                ctr = 1
                for i in range(len(grammar)):
                    head, body=grammar[ctr-1].split('->')
                    ctr+=1
                if all(x.isupper() for x in head):
                    print('grammar error')
                raise TypeError('error')
        except:
            print('ss')
            isError = True
            if isError:
                print('grammar error')
                return render_template('cannonical.html', hello="world", isError = isError)
            else:
                global production_list, tl, ntl, nt_list, t_list, first_list, follow_list


                items, sym_list, clr_items, goto_list, first_list, follow_list, input_test, string_validity, conflict = main(
                    grammars=string, Input=to_parse)
                print(f'grammar {grammar}')    
                print(f'variables {dir()}')
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
