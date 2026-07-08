"""
transform.py

Reads the raw JSON file, transforms the data into a clean
Pandas DataFrame, performs feature engineering,
and returns the transformed DataFrame.
"""

import json
import pandas as pd

from config import (
    RAW_JSON_PATH,
    POPULAR_DOWNLOAD_THRESHOLD
)

from logger import logger


def transform_data():
    """
    Transform raw Hugging Face model data.

    Returns:
        pandas.DataFrame
    """

    logger.info("=" * 70)
    logger.info("Starting Transform Phase")

    try:

        # ---------------------------------------------------
        # Read raw JSON
        # ---------------------------------------------------

        with open(RAW_JSON_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)

        logger.info("Raw JSON loaded successfully.")

        models = []

        # ---------------------------------------------------
        # Extract required fields
        # ---------------------------------------------------

        for model in data:

            models.append({

                "model_name": model.get("id"),

                "downloads": model.get("downloads", 0),

                "likes": model.get("likes", 0),

                "pipeline_tag": model.get("pipeline_tag"),

                "last_modified": model.get("lastModified")

            })

        # ---------------------------------------------------
        # Create DataFrame
        # ---------------------------------------------------

        df = pd.DataFrame(models)

        logger.info(f"DataFrame Shape : {df.shape}")

        # ---------------------------------------------------
        # Handle Missing Values
        # ---------------------------------------------------

        df.fillna(
            {
                "pipeline_tag": "Unknown",
                "downloads": 0,
                "likes": 0
            },
            inplace=True
        )

        logger.info("Missing values handled.")

        # ---------------------------------------------------
        # Feature Engineering
        # ---------------------------------------------------

        df["is_popular"] = df["downloads"].apply(

            lambda x: "Yes"
            if x >= POPULAR_DOWNLOAD_THRESHOLD
            else "No"

        )

        logger.info("Created 'is_popular' column.")

        # ---------------------------------------------------
        # Sort Data
        # ---------------------------------------------------

        df.sort_values(

            by="downloads",

            ascending=False,

            inplace=True

        )

        df.reset_index(drop=True, inplace=True)

        logger.info("Sorted models by downloads.")

        logger.info("Transform Phase Completed")
        logger.info("=" * 70)

        return df

    except Exception as error:

        logger.exception(f"Transform Failed : {error}")

        raise


if __name__ == "__main__":

    dataframe = transform_data()

    print(dataframe.head())

