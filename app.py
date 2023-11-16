import os
from flask import Flask, render_template
import markdown
import frontmatter
from datetime import datetime

app = Flask(__name__)

def read_post_content(filename):
    with open(os.path.join('posts', filename), 'r') as file:
        post = frontmatter.load(file)
        return {
            "date": post.metadata.get('date', datetime.now()), 
            "title": post.metadata.get('title'),
            "path": filename.split(".")[0],
            "content": markdown.markdown(post.content)
        }

def get_posts():
    posts = []
    for filename in os.listdir('posts'):
        if filename.endswith('.md'):
            posts.append(read_post_content(filename))
    return sorted(posts, key=lambda x: x['date'])  # Sort by date

@app.route('/')
def home():
    print('hi')
    posts = get_posts()
    return render_template('home.html', posts=posts)

@app.route('/post/<string:post_path>')
def post(post_path):
    post = read_post_content(post_path + '.md')
    return render_template('post.html', post=post)

@app.route('/posts')
def posts():
    posts = get_posts()
    return render_template('posts.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True, port=3000)