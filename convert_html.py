#!/usr/bin/env python3
import click
import re

import bs4

VIDEO_FILE_HEADER = """<?xml version="1.0" encoding="UTF-8" ?>
<?xml-stylesheet type="text/xsl" href="videoshow.xsl"?>
<!DOCTYPE videoshow SYSTEM "videoshow.dtd">
<videoshow>
"""
VIDEO_FILE_FOOTER = """
</videoshow>
"""

TITLE_TAG = "title"
COPYRIGHT_TAG = "copyright"
VIDEO_TAG = "video"
SOURCE_TAG = "source"
CAPTION_TAG = "caption"

INDENT_SPACE = " "


def tag_str(tag_name, indent=0, content=None):
    if content is None:
        return f"{INDENT_SPACE * indent}<{tag_name}>\n"
    else:
        return f"{INDENT_SPACE * indent}<{tag_name}>{content}</{tag_name}>\n"


def end_tag_str(tag_name, indent=0):
    return f"{INDENT_SPACE * indent}</{tag_name}>\n"


@click.command(help="Convert specified html video files to viewer format.")
@click.option("--outfile",
              "-o",
              help="The output video viewer format file.",
              type=click.Path(exists=False, writable=True),
              default="video.xml")
@click.argument("files",
                nargs=-1,
                type=click.Path(exists=True, readable=True),
                required=True)
def convert_files(outfile, files):
    with open(outfile, "w") as out_fp:
        out_fp.write(VIDEO_FILE_HEADER)
        have_title = False

        for input_file in files:
            with open(input_file, "r") as fp:
                html = fp.read()
                soup = bs4.BeautifulSoup(html, "html.parser")
                if not have_title:
                    title = soup.find(TITLE_TAG)
                    if title is not None:
                        out_fp.write(tag_str(TITLE_TAG, indent=2, content=title.text))
                        have_title = True
                    # The copyright is not in a specific tag, so we need to search the whole text for it.
                    all_text = soup.get_text()
                    copyright = re.search(r"Copyright\s*[\d-]+.*", all_text)
                    if copyright is not None:
                        out_fp.write(tag_str(COPYRIGHT_TAG, indent=2, content=copyright.group(0).split()[1]))
                videos = soup.find_all('td')
                for video in videos:
                    caption = video.find('center')
                    source = video.find(SOURCE_TAG)
                    out_fp.write(tag_str(VIDEO_TAG, indent=2))
                    out_fp.write(tag_str(SOURCE_TAG, indent=4, content=source['src']))
                    out_fp.write(tag_str(CAPTION_TAG, indent=4, content=caption.text))
                    out_fp.write(end_tag_str(VIDEO_TAG, indent=2))
        out_fp.write(VIDEO_FILE_FOOTER)


if __name__ == "__main__":
    convert_files()