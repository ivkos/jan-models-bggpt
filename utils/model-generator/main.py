import json
import os

import requests

THIS_DIR = os.path.dirname(__file__)
REPO_ROOT = os.path.join(THIS_DIR, "..", "..")
MODELS_DIR = os.path.join(REPO_ROOT, "models")


def main():
    files = []

    with open(os.path.join(THIS_DIR, "models_list.json"), "r") as fd:
        models_list = json.load(fd)

    for model_object in models_list:
        repo = model_object["repo"]
        gguf_files = model_object["gguf_files"]

        for filename in gguf_files:
            file_url = f"{repo}/resolve/main/{filename}"

            head_resp = requests.head(file_url, allow_redirects=True)
            files.append((file_url, filename, head_resp.headers["Content-Length"]))

        with open(os.path.join(os.path.dirname(__file__), "model.template.json"), "r") as template:
            template_content = template.read()

            for file_url, filename, size in files:
                filename_no_ext = os.path.splitext(filename)[0]
                filled_template = template_content \
                    .replace("<<FILENAME>>", filename) \
                    .replace("<<FILENAME_NO_EXT>>", filename_no_ext) \
                    .replace("<<FILE_URL>>", file_url) \
                    .replace("<<SIZE>>", size)

                os.makedirs(os.path.join(
                    MODELS_DIR, filename_no_ext
                ), exist_ok=True)

                with open(os.path.join(MODELS_DIR, filename_no_ext, "model.json"), "w", newline="\n") as model:
                    model.write(filled_template)


if __name__ == "__main__":
    main()
