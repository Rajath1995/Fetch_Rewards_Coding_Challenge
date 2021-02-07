from flask import Flask, request, render_template
from text_similarity import finding_the_similarity

app = Flask(__name__)

@app.route("/")
def my_form():
    return render_template('text_input.html')

@app.route('/',methods=['POST'])
def my_form_post():
    text1 = request.form.get("text1")
    text2 = request.form.get('text2')
    similarity = finding_the_similarity(text1,text2)

    return str("The similarity value between the document 1 and document 2 based on cosine distance = "+ str(similarity))

if __name__ == "__main__":
    app.run()