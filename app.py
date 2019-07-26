from flask import Flask, render_template,request
import random


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST", "GET"])
def generate():
    states =  ["Abia", "Adamawa", "Anambra", "Akwa Ibom", "Bauchi", "Bayelsa", "Benue", "Borno", "Cross River", "Delta", "Ebonyi", "Enugu", "Edo", "Ekiti", "Gombe", "Imo", "Jigawa", "Kaduna", "Kano", "Katsina", "Kebbi", "Kogi", "Kwara", "Lagos", "Nasarawa", "Niger", "Ogun", "Ondo", "Osun", "Oyo", "Plateau", "Rivers", "Sokoto", "Taraba", "Yobe", "Zamfara"]
    tribes = ["Abayon", "Abua","Achipa", "Adim", "Attakar", "Bachama", "Bachere", "Bahumono"
    "Buduma","Challa", "Chamba", "Daba", "Dakarkari", "Ouguri", "Ejagham", "Fyam", "Ga’anda", "Gade", "Galambi", "Gwandara", "Gwoza", "Hausa", "Higi", "Ibibio", "ljumu", "Ikorn", "lyala" ]
    name = request.form["name"]
    if len(name) < 10:
        target_list_state = states[0:10]
        target_list_tribe = tribes[0:10]
        state = random.choice(target_list_state)
        tribe = random.choice(target_list_tribe)
        gender = "male"
    else :
        target_list_state = states[10:36]
        target_list_tribe = tribes[10:27]
        state = random.choice(target_list_state)
        tribe = random.choice(target_list_tribe)
        gender = "female"
    return render_template("index.html", name=name, state=state, tribe=tribe, gender=gender)

    
if __name__ == "__main__":
    app.run(debug=True)


