from flask import Blueprint, request, redirect, render_template, url_for

import json_storage

bp = Blueprint('routes', __name__, template_folder='templates')


@bp.route('/')
def index():
    blog_posts = json_storage.get_posts()
    return render_template('index.html', posts=blog_posts)


@bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        json_storage.add_post(
            request.form['title'],
            request.form['author'],
            request.form['content']
        )
        return redirect(url_for('routes.index'))
    return render_template('form.html', url='/add')


@bp.route('/delete/<int:post_id>')
def delete(post_id: int):
    json_storage.del_post(post_id)
    return redirect(url_for('routes.index'))


def find_post(post_id: int):
    """ Helper function, finds a post by its id """
    posts = json_storage.get_posts()
    for post in posts:
        if post['id'] == post_id:
            return post


@bp.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id: int):
    old_post = find_post(post_id)
    if request.method == 'POST':
        new_post = {
            'id': post_id,
            'title': request.form['title'],
            'author': request.form['author'],
            'content': request.form['content']
        }
        if new_post != old_post:
            json_storage.update_post(old_post, new_post)
        return redirect(url_for('routes.index'))
    return render_template('form.html', post=old_post,
                           url=f'/update/{post_id}')
