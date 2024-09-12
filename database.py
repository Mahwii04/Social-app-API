import sqlite3

connection = sqlite3.connect('social.db')

test_post = {
    'post_title': 'First Post',
    'post_text': 'Hi, here are some text for my post',
    'user_id': 0 
}

with connection:
    cur = connection.cursor()
    cur.execute(
        '''
        INSERT INTO posts (post_title, post_text, user_id)
        VALUES
        (:post_title, :post_text, :user_id)''',
        test_post
    )