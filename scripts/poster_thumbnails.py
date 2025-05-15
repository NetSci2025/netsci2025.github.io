"""
This script reads in all poster PDFs and generates missing thumbnails.

External libraries required:

- ImageMagick
- PostScript (for PDF support in ImageMagick)
"""

import csv
import shutil
import subprocess
from pathlib import Path
from tempfile import NamedTemporaryFile

poster_folder = Path("./poster_fullsize")
thumbnail_folder = Path("./poster_thumbnails")

# Step 1: Clean-up poster directory. Microsoft CMT gives the posters a non-optimal name
# that includes backslashes etc.
for poster in poster_folder.glob("*.pdf"):
    new_name = poster.stem.split("\\")[0] + ".pdf"
    poster.rename(poster_folder / new_name)

thumbnails = list(thumbnail_folder.glob("*.webp"))

# Step 2: Generate thumbnails for all posters
generated_ids = set()
for poster in poster_folder.glob("*.pdf"):
    generated_ids.add(poster.stem)

    thumbnail = thumbnail_folder / (poster.stem + ".webp")
    if thumbnail in thumbnails:
        # already generated thumbnail for this poster in the past
        continue

    print(poster.name, thumbnail.name)

    subprocess.run(
        f"magick {poster} -thumbnail 400x -quality 70 -define webp:lossless=false {thumbnail}",
        shell=True,
    )
    generated_ids.add(poster.stem)

# Step 3: Update CSV and indicate that thumbnails are available
temp_csv = NamedTemporaryFile(delete=False, mode="w")
with open("../_data/posters.csv") as csvfile, temp_csv:
    reader = csv.DictReader(csvfile)
    writer = csv.DictWriter(temp_csv, fieldnames=reader.fieldnames)

    writer.writeheader()
    for row in reader:
        if row["id"] in generated_ids:
            row["poster_uploaded"] = 1
        else:
            row["poster_uploaded"] = 0

        writer.writerow(row)

shutil.move(temp_csv.name, "../_data/posters.csv")
