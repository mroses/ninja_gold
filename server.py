from flask import Flask, redirect, session, render_template, request
import random
import time
import datetime
app = Flask(__name__)
app.secret_key = 'secrets'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    loc = request.form['location'] #just to make this easier to type later on
    location_map = {
        'farm': random.randint(10,21),
        'cave': random.randint(5,11),
        'house': random.randint(2,6),
        'casino': random.randint(-50,51)
    }
    print loc
    print location_map[loc] #location map of house/or whatever button you pushed. location map above keys are the location and values are the random.randint...
    curr_gold = location_map[loc]
    if not 'gold' in session:
        session['gold'] = curr_gold
    else:
        session['gold'] += curr_gold
    time = datetime.datetime.now().strftime("%Y/%m/%d,  %H:%M %p")
    if curr_gold > 0:
        message = {
            'class': 'green',
            'content': 'You won {} golds at the {}! ({})'.format(curr_gold, loc, time)
        }   
    else:
        message = {
            'class': 'red',  #comes from css class in css file
            'content': "You lost {} golds at the {}!. ({})".format(curr_gold, loc, time)
        }
    if not 'activities' in session:
        session['activities'] = [message]
        #time = datetime.datetime
        #print datetime.datetime

        
    else:
        session['activities'].insert(0, message) #use insert instead of append in order to keep the order of when the buttons were clicked. Now most recently clicked gold gain will be at the top
        session.modified = True #have to use this in order to append to a list in session 
        time = datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
        print datetime.datetime.now().strftime("%y-%m-%d-%H-%M")

    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)
