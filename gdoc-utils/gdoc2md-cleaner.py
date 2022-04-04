#!/usr/bin/env python3

# When using the "Docs to Markdown" Google Docs add-on, chose these settings:
# * Demote headings (H1 → H2, etc.)
# * Suppress top comment

import re

from argparse import ArgumentParser
from pathlib import Path


parser = ArgumentParser(
    description='Cleans up files imported from Google Docs using the Docs to Markdown addon.'
)
parser.add_argument(
    'fname',
    type=str,
    help='The filename of the file to clean up.',
)
parser.add_argument(
    '--i',
    dest='inplace',
    action='store_true',
    help='Set flag to change file in place. Otherwise new file with suffix _clean is created.',
)
args = parser.parse_args()

IMAGES = {
    "1": {
        "path": "/assets/2021/2021-01-10-moderna-vaccine-in-fridge.jpg",
        "title": "Source/attribution: U.S. Navy Photo by Elaine Heirigs, NHC/NMRTC Lemoore public affairs/Released, https://www.flickr.com/photos/navymedicine/50755819886/",
    },
    "2": {
        "path": "/assets/2021/2021-01-10-ows-vaccine-distribution-process.png",
        "title": "Operation Warp Speed vaccine distribution process. Source: U.S. Department of Health & Human Services, https://www.hhs.gov/coronavirus/explaining-operation-warp-speed/index.html",
    },
    "3": {
        "path": "/assets/2021/2021-01-10-baltimore.jpg",
        "title": "A station at a vaccination clinic for Baltimore County frontline health workers on Wednesday, December 23, 2020. This clinic used the Moderna vaccine. Source/attribution: Baltimore County Government, https://www.flickr.com/photos/baltimorecounty/50753216127/",
    },
    "4": {
        "path": "/assets/2021/2021-01-10-strasbourg.jpg",
        "title": "A vaccination station at the University Hospital in Strasbourg on January 8, 2021. The vaccine shown is Pfizer/BioNTech’s Comirnaty. The tray appears to contain four remaining prepared syringes and the empty vial they were drawn from. Source/attribution: © Claude Truong-Ngoc / Wikimedia Commons (CC-BY-SA-4.0)",
    },
}


fpath = Path = Path(args.fname)
assert fpath.exists()
assert fpath.is_file()

with fpath.open() as f:
    lines = f.readlines()

cleaned_lines = [
    "---",
    "layout: post",
    'title: "Exploring the Supply Chain of the Pfizer/BioNTech and Moderna COVID-19 vaccines"',
    "tags:",
    " - vaccines",
    "published: true",
    "date: January 10, 2021",
    "---",
]

# to clean off a header use simple started state variable
started = False
skip = 0

for line in lines:
    line = line.strip("\r\n")

    # If lines are supposed to be skipped, do so
    if skip:
        skip -= 1
        continue

    # if we haven't found the start, keep looking
    if not started:
        if line.startswith("#"):
            # Found the first heading (the title). Switch started flag but don't include this line
            started = True
        continue

    if line.startswith('<p id="gdcalert'):
        # drop the previous two lines
        cleaned_lines = cleaned_lines[:-2]
        # drop the next two lines
        skip = 2
        # drop this line
        continue

    if line.startswith("![alt_text]"):
        matches = re.match(r"\!\[alt_text\]\(images/image(\d+)\.", line)
        image_id = matches.group(1)
        image_info = IMAGES.get(image_id)
        cleaned_lines.append("{% include image.html")
        cleaned_lines.append(f'  img="{image_info["path"]}"')
        cleaned_lines.append(f'  title="{image_info["title"]}"')
        cleaned_lines.append("%}")
        cleaned_lines.append("")
        skip = 4  # trims out the image heading which exists both in the google doc and in the constants fo this file
        continue

    if line.startswith("<!-- Footnotes themselves at the bottom. -->"):
        continue

    if line.startswith("    _") and line.endswith("_"):
        cleaned_lines = cleaned_lines[:-1]
        line = "".join(["> ", line[5:-1]])

    cleaned_lines.append(line)


new_fpath = fpath if args.inplace else fpath.with_suffix(".cleaned.md")
with new_fpath.open(mode="w") as f:
    f.writelines([f"{l}\n" for l in cleaned_lines])

print(f"Wrote output to {new_fpath}")
