from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    user = request.args['username'] 
    reply1 = "Hello, " + user + "."
    gamer = request.args['gamer_scale'] 
    if gamer == 'no':
        reply2 = "Unfortunately, you have not met the minimum requirements to join Gamer Club©."
    else:
        reply2 = "You are now a part of Gamer Club©"
    return render_template('response.html', response1 = reply1, response2 = reply2)
    
if __name__=="__main__":
    app.run(debug=False)