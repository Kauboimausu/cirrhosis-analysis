from kaggle.api.kaggle_api_extended import KaggleApi
import sys
from pathlib import Path

DATASET = "fedesoriano/cirrhosis-prediction-dataset"
TARGET_FOLDER = "cirrhosis"
OUTPUT_DIR = Path(f"data/raw/{TARGET_FOLDER}")

def main():
    try:
        api = KaggleApi()
        api.authenticate()
    except Exception:
        sys.exit(
            "Kaggle API credentials not found.\n"
            "Set KAGGLE_USERNAME and KAGGLE_KEY environment variables."
        )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Downloading {DATASET}...")
    api.dataset_download_files(
        DATASET,
        path=OUTPUT_DIR,
        unzip=True
    )

    print(f"Dataset downloaded to {OUTPUT_DIR.resolve()}")

if __name__ == "__main__":
    main()
