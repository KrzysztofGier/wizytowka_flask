from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/mypage/me', methods=['GET'])
def me():
    return render_template("me.html")

@app.route('/mypage/contact.html', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template("contact.html")
    elif request.method == 'POST':
        print("We received POST")
        print(request.form)
        return redirect("/mypage/contact.html")