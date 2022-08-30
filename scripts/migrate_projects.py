import os
from datetime import datetime
from pathlib import Path

import markdownify
from bs4 import BeautifulSoup


def get_all_projects():
    return os.listdir("../old-site/projects")


def gen_front_matter(heading, subtitle):

    template = """---
title: "{title}"
date: 2022-08-27T18:09:38+05:30
draft: false
subtitle: "{subtitle}"
---"""

    return template.format(title=heading, subtitle=subtitle)


def gen_file_name(name: str):
    clean = name.replace(" ", "-")
    return f"{clean}"


def migrate():

    project_dirs = get_all_projects()
    project_index_files = [
        f"../old-site/projects/{p}/index.html" for p in get_all_projects()
    ]

    for project_dir in project_dirs:
        file = f"../old-site/projects/{project_dir}/index.html"

        with open(file) as f:

            soup = BeautifulSoup(f.read())
            article = soup.find("article")

            heading = article.find("h1").find("span").text
            subtitle = article.find("p", attrs={"class": "subtitle"}).text

            front_matter = gen_front_matter(heading, subtitle)
            article_body = markdownify.markdownify(str(article))

            project_file_path = f"../content/work/{project_dir}/index.md"

            with open(project_file_path, "w") as project_file:
                content = f"{front_matter}\n{article_body}"
                project_file.write(content)

            print(f"[done] {project_dir}")


if __name__ == "__main__":
    print(
        """Danger Ahead The Following Action will overwrite
         existing files create backup before moving ahead :) \n 
         """
    )
    confirm = input("Continue [Y/N] ").strip().lower()
    if confirm == "y" or confirm == "yes":
        migrate()
