import os
import json

# All scripts should be run from the project root!
pwd = os.getcwd()
config = {
    "data_dir": str(os.path.join(pwd, "ml_scraping", "data")),
    "model_dir": str(os.path.join(pwd, "ml_scraping", "model")),
    "out_dir": str(os.path.join(pwd, "ml_scraping", "out")),
    "job_dir": str(os.path.join(pwd, "ml_scraping", "job"))
}

for d_path in config.values():
    if not os.path.isdir(d_path):
        os.mkdir(d_path)

with open(os.path.join(pwd, "config.json"), "w") as f:
    json.dump(config, f, indent=4)
