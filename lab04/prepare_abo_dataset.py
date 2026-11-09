from pathlib import Path

import pandas as pd

metadata = pd.read_csv("images/metadata/images.csv.gz")
metadata = metadata[(metadata["width"] >= 1000) & (metadata["height"] >= 1000)]

image_paths = [Path("images/small") / path for path in metadata["path"]]
image_paths = [str(path) for path in image_paths if path.is_file()]

print(f"Found {len(image_paths)} images")
