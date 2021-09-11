from flask import Flask, render_template, request
import requests

app = Flask(__name__)
parameters = {
        "amount": 10,
        "category": 18,
        "difficulty": "easy",
        "type": "boolean"
    }

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
quest_data = data['results']



@app.route('/')
def home():
    datas = quest_data
    length = len(datas)
    for x in range(len(datas)):
        print(datas[x]['question'])
    return render_template("index.html", data=datas, length=length)

@app.route('/post/<int:num>')
def post_page(num):
    quest = quest_data[num]['question']
    ans = quest_data[num]['correct_answer']
    print(quest)
    print(ans)
    return render_template("post.html", question=quest, answer=ans)


@app.route("/form/", methods=['GET', 'POST'],)
def form():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("forms.html", msg_sent=True)
    return render_template("forms.html", msg_sent=False)

# #making your response show on another html page
# @app.route("/result", methods=["POST"],)
# def result_page():
#
#     name = request.form['fname']
#     lname = request.form['lname']
#     return render_template("form_result.html", name=name, lname=lname)


@app.route("/second_form", methods=['GET', 'POST'],)
def second_form():
    if request.method == "POST":
        data = request.form
        print(data["lname"])
        print(data["fname"])
        return "<h1>Successfully sent your message</h1>"
    return render_template("form_result.html")


if __name__ == "__main__":
    app.run(debug=True)
