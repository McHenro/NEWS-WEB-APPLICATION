### THIS IS A NEWS WEB APPLICATION

## Challenge

Have you ever heard of Hacker News? It's a great source of tech-related news. They provide a public API at https://hackernews.api-docs.io.

The goal is to make a web app to make it easier to navigate the news:

- Choose a web framework of your choice. Django, Flask, use what you like. Make a new virtualenv and pip install it;

- Make a scheduled job to sync the published news to a DB every 5 minutes. You can start with the latest 100 items, and sync every new item from there. Note: here are several types of news (items), with relations between them;

- Implement a view to list the latest news;

- Allow filtering by the type of item;

- Implement a search box for filtering by text;

- As there are hundreds of news you probably want to use pagination or lazy loading when you display them.
It is also important to expose an API so that our data can be consumed:

`GET` : List the items, allowing filters to be specified;
`POST` : Add new items to the database (not present in Hacker News);


## Bonus

- Only display top-level items in the list, and display their children (comments, for example) on a detail page;

- In the API, allow updating and deleting items if they were created in the API (but never data that was retrieved from Hacker News);


## Setting Up For Local Development

* Start up Django sever/App:

    ```
    python3 manage.py runserver
    ```

* Start up Redis server:

    ```
    redis-server
    ```
With your Django App and Redis running, open two new terminal windows/tabs. In each new window, navigate to 

your project directory, activate your virtualenv, and then run the following commands (one in each window):

* Start up celery beat to schedule periodic tasks:

    ```
    celery -A project beat -l info
    ```

* Start up celery worker to execute tasks:

    ```
    celery -A project worker -l info
    ```
Alternatively you can get a redis broker url from services like Heroku.
