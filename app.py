from flask import Flask, render_template, request  # NOT the same as requests 
from github_api import get_github_user
app = Flask(__name__)

@app.route('/') # this takes you to the homepage
def homepage():
    return render_template('index.html')

@app.route('/get_user') # don't forget the slash
def get_user_info():
    # Get the username from github api an display some info 
    print('Form data is ', request.args)  # requests.args is a dictionary
    username = request.args.get('username')  # this is safer it returns None if not found
    user_info, error_message = get_github_user(username) # this is a dictionary
    if error_message:
        return render_template('error.html', error=error_message)
    else:
        return render_template('github.html', user_info=user_info)

if __name__ == '__main__':
    app.run()