from pathlib import Path

posts_dir = Path("../content/posts")


def remove_dates():

    """
    rename files from
    2019-04-27-file-name.md
    file-name.md
    """

    for post in posts_dir.iterdir():

        if post.name == "_index.md":
            continue

        post_name = post.name.split("-")

        if not len(post_name) > 3:
            continue

        new_name = "-".join(post_name[3:])
        print(f"[+] Renaming {post.name} to {new_name}")
        post.rename(posts_dir.joinpath(new_name))


if __name__ == "__main__":
    remove_dates()
