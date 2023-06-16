import json

FILE_NAME = 'posts.json'


def get_posts() -> list[dict]:
    """ Returns all posts from the storage """
    with open(FILE_NAME) as handle:
        return json.loads(handle.read())


def add_post(title: str, author: str, content: str) -> None:
    """ Adds a post to the storage """
    posts = get_posts()
    new_id = posts[-1]['id'] + 1
    posts.append(
        {'id': new_id, 'title': title, 'author': author, 'content': content}
    )
    update_file(posts)


def del_post(post_id: int) -> None:
    """ Deletes a post from the storage """
    posts = get_posts()
    update_file([post for post in posts if post['id'] != post_id])


def update_post(old_post: dict, new_post: dict) -> None:
    """ Updates a post from the storage """
    posts = get_posts()
    posts[posts.index(old_post)] = new_post
    update_file(posts)


def update_file(posts: list[dict]) -> None:
    """ Updates the json file """
    with open(FILE_NAME, 'w') as handle:
        handle.write(json.dumps(posts))
