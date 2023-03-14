from . import bp as app
from app import db
from app.blueprints.social.models import Post, User
from flask_cors import cross_origin

@app.route('/posts')
def api_posts():
    result = []
    for post in Post.query.all():
        result.append({
            'id': post.id,
            'body': post.body,
            'date_created': post.timestamp,
            'username': post.author.username
        })

    return result

@app.route('/user-posts/<user>')
def user_posts(user):
    result = []
    user_match = User.query.filter_by(username=user).first()
    user_posts= user_match.posts
    for post in user_posts:
        result.append({
            'id': post.id,
            'body': post.body,
            'date_created': post.timestamp,
            'username': post.author.username
        })

    return result

@app.route('/post/<id>')
def api_post_by_id(id):
    post = Post.query.get(int(id))
    return {
            'id': post.id,
            'body': post.body,
            'date_created': post.timestamp,
            'username': post.author.username
        }