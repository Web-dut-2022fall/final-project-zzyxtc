## What's this?
This is a forum system powered by Django and Bootstrap to share your ideas of some interesting books. All of the forum's posts are based the book node though, it can also have many other topics by extending the book node.

## Features(under development)
- Powered by Django and Bootstrap。
- Scalable multi-node system.
- Follow, collect, and get the dynamic news. 
- Personalized user page.
- Multi-user、multi-role permission management system.
- Restful API.
- Common forum's functions:
    + Register, login/logout, reset password, email confirm.
    + Post, reply.
    + Add node, tag.
    + Notification.

## How to use?
1.  ```bash
    pip install -r requirements.txt
    ```
    
2. ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

3. Start up:
    ```bash
    python manage.py runserver
    ```
4. Create a administrator user:
    ```bash
    python manage.py createsuperuser
    ```


