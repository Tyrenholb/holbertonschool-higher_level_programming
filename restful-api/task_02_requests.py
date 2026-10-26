import requests
import csv


def fetch_and_print_posts():

    url = requests.get("https://jsonplaceholder.typicode.com/posts")

    print(f"Status Code: {url.status_code}")

    if url.status_code == 200:
        posts = url.json()

        for post in posts:
            print(post["title"])


def fetch_and_save_posts():

    url = requests.get("https://jsonplaceholder.typicode.com/posts")

    if url.status_code == 200:

        posts = url.json()

        saved_posts = []

    for post in posts:
        saved_post = {
            "id": post["id"], "title": post["title"], "body": post["body"]}
    saved_posts.append(saved_post)

    with open("posts.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
        writer.writeheader()
        writer.writerows(saved_posts)


fetch_and_print_posts()
fetch_and_save_posts()
