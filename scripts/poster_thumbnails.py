"""
This script reads in all poster PDFs and generates missing thumbnails.

External libraries required:

- ImageMagick
- PostScript (for PDF support in ImageMagick)
"""

import subprocess
from pathlib import Path

poster_folder = Path("../_data/poster_fullsize")
thumbnail_folder = Path("../assets/images/poster_thumbnails")

posters = list(poster_folder.glob("*.pdf"))
thumbnails = list(thumbnail_folder.glob("*.webp"))

for poster in posters:
    # validate poster name
    try:
        int(poster.stem)
    except ValueError:
        print(f"Invalid poster name: {poster.name}")
        continue

    thumbnail = thumbnail_folder / (poster.stem + ".webp")
    if thumbnail in thumbnails:
        # already generated thumbnail for this poster in the past
        #continue
        pass

    print(poster.name, thumbnail.name)

    subprocess.run(
        f"magick {poster} -thumbnail 400x -quality 70 -define webp:lossless=false {thumbnail}",
        shell=True,
    )
