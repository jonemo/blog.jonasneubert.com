import os
from datetime import datetime
from pathlib import Path

import markdownify
from bs4 import BeautifulSoup


def gen_front_matter(heading):

    template = """---
title: "{title}"
date: 2022-08-27T18:09:38+05:30
draft: false
location: "SF Python"
---"""

    return template.format(title=heading)


def gen_file_name(name: str):
    clean = name.replace(" ", "-")
    return f"{clean}"


def migrate():

    talks = os.listdir("../old-site/talks/")
    print("All Talk files :", talks)

    for talk in talks:
        file = f"../old-site/talks/{talk}"

        print(f"[migrating] : {file}")
        with open(file) as f:

            soup = BeautifulSoup(f.read())
            article = soup.find("article")

            heading = article.find("h1").text

            front_matter = gen_front_matter(heading)
            article_body = markdownify.markdownify(str(article))

            project_file_path = f"../content/talks/{gen_file_name(heading)}.md"
            print(f"[saving] : {project_file_path}")
            with open(project_file_path, "w") as project_file:
                content = f"{front_matter}\n{article_body}"
                project_file.write(content)

            print(f"[done] {talk}")


if __name__ == "__main__":

    print(
        """Danger Ahead The Following Action will overwrite
         existing files create backup before moving ahead :) \n 
         """
    )
    confirm = input("Continue [Y/N] ").strip().lower()
    if confirm == "y" or confirm == "yes":
        migrate()
