from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post
from flaskblog.posts.forms import PostForm
posts = Blueprint('posts', __name__)

@posts.route("/posts/new", methods=['GET', 'POST'])
@login_required
def new_posts():
    """
    The new_posts route shows the form to create a new post.
    It renders the create_post.html template and passes the PostForm
    object to it. If the form validates, it creates a Post object
    with the form data and current_user as the author, adds the post
    to the database, and then redirects to the home page.
    """
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', category='success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post', 
                           form=form, legend='New Post')

@posts.route("/posts/<int:post_id>")
def post(post_id):
    """
    The post route shows the blog post with the given post_id.
    It renders the post.html template and passes the Post object
    to it. If the post is not found, it aborts with a 404 status.
    """
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

@posts.route("/posts/<int:post_id>/update", methods=['GET','POST'])
@login_required
def update_post(post_id):
    """
    The update_post route shows the form to update a post.
    It renders the create_post.html template and passes the PostForm
    object to it. If the form validates, it updates the Post object
    with the form data and commits the changes to the database,
    and then redirects to the post page.
    If the user is not the author of the post, it aborts with a 403 status.
    """
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post', 
                           form=form, legend='Update Post')

@posts.route("/posts/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    """
    The delete_post route deletes the post with the given post_id.
    If the post is not found, it aborts with a 404 status.
    If the user is not the author of the post, it aborts with a 403 status.
    """

    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))

@posts.route('/about')
def about():
    # Fetch recent posts from your database or CMS
    recent_posts = Post.query.order_by(Post.date_posted.desc()).limit(3).all()  # Adjust query as needed
    return render_template('about.html', recent_posts=recent_posts)

