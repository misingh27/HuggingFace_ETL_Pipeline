"""
load.py

Loads the transformed DataFrame into:
1. CSV
2. SQLite Database
"""

import sqlite3
import pandas as pd

from config import (
    CSV_PATH,
    DATABASE_PATH,
    TABLE_NAME
)

from logger import logger


def load_data(df: pd.DataFrame):
    """
    Load the transformed DataFrame into CSV and SQLite.

    Args:
        df (pd.DataFrame): Cleaned DataFrame
    """

    logger.info("=" * 70)
    logger.info("Starting Load Phase")

    try:

        # ---------------------------------------
        # Save CSV
        # ---------------------------------------

        df.to_csv(CSV_PATH, index=False)

        logger.info(f"CSV saved successfully at: {CSV_PATH}")
        logger.info(f"Rows Written: {len(df)}")

        # ---------------------------------------
        # SQLite Connection
        # ---------------------------------------

        connection = sqlite3.connect(DATABASE_PATH)

        df.to_sql(
            TABLE_NAME,
            connection,
            if_exists="replace",
            index=False
        )

        connection.close()

        logger.info(f"SQLite database updated: {DATABASE_PATH}")

        logger.info("Load Phase Completed")
        logger.info("=" * 70)

    except Exception as error:

        logger.exception(f"Load Failed: {error}")

        raise


if __name__ == "__main__":

    from transform import transform_data

    dataframe = transform_data()

    load_data(dataframe)

    print("Load completed successfully!")
