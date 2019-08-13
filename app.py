from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<username>", methods=['GET'])
def hello(username):
    return "Hello, %s!" % username


@app.route("/post")
def post():
    return render_template("post.html")


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
