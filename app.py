from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World! 👋 from Lucas Gonzalez-Rey.'


@app.route('/hello')
def hello():
    course = request.args.get('course')
    grade = request.args.get('grade')
    return render_template('hello.html', course=course, grade=grade)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/about-css', methods=['GET'])
def about_css():
    colors = request.args.get('color')
    return render_template('about-css.html', favcolors=colors)


@app.route('/favorite-course', methods=['GET'])
def favorite_course():
    return render_template('favorite-course.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return render_template('contact.html', form_submitted=True)
    else:
        return render_template('contact.html')


if __name__ == '__main__':
    app.run()
