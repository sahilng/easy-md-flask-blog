# An easy markdown blog with Flask

To add a post, just add a markdown file with `title` and `date` frontmatter to the `posts` directory. See examples.

Runs on port `3000` by default.

Docker:
```sh
docker build -t easy-md-flask-blog:latest .
docker run -p 3210:3000 easy-md-flask-blog:latest
```