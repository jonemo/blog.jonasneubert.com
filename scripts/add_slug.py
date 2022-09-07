from pathlib import Path

posts_dir = Path("../content/posts")


def add_slug():

    """
    add a slug to front matter
    """

    for post in posts_dir.iterdir():

        if post.name == "_index.md":
            continue

        post_name = post.name[11:].replace(".md","")
        
        print("slug" , post_name)

        with open(post) as f :
            post_content = f.readlines()

        with open(post,"w") as f :
            post_content.insert(1,f"slug: {post_name}\n")
            f.writelines(post_content)
        
        

if __name__ == "__main__":
    add_slug()
