import json
import requests
import mimetypes
from PIL import Image

with open("Members_raw.json", "r") as f:
    data = json.load(f)

for i in range(len(data)):
    link = data[i]["image"].replace("/file/d/", "/uc?id=").replace("/open?id=", "/uc?id=").replace("/view?usp=sharing", "")+"&export=download"
    name = "-".join(data[i]["fullName"].split())
    response = requests.get(link)
    content_type = response.headers['content-type']
    extension = mimetypes.guess_extension(content_type)
    with open(f"{name}{extension}", "wb") as image:
        image.write(response.content)
    compressed_image = Image.open(f"{name}{extension}")
    width, height = compressed_image.size
    TARGET_WIDTH = 500
    coefficient = width / 500
    new_height = height / coefficient
    compressed_image.resize((int(TARGET_WIDTH),int(new_height)),Image.ANTIALIAS)
    compressed_image.save(f"{name}{extension}", quailty=80, optimize=True)
    data[i]["image"] = f"about-us-images/{name}.jpg"

with open("Members.json", "w") as f:
    json.dump(data, f)