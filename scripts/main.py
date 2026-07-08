"""
main.py

Main entry point for the Hugging Face ETL Pipeline.
Runs Extract -> Transform -> Load.
"""

import time
import platform

from extract import extract_data
from transform import transform_data
from load import load_data
from logger import logger


def run_pipeline():
    """
    Execute the complete ETL pipeline.
    """

    start_time = time.time()

    logger.info("=" * 70)
    logger.info("Hugging Face ETL Pipeline Started")
    logger.info(f"Python Version: {platform.python_version()}")
    logger.info("Execution Started")

    try:

        # -----------------------------
        # Extract
        # -----------------------------
        extract_data()

        # -----------------------------
        # Transform
        # -----------------------------
        dataframe = transform_data()

        # -----------------------------
        # Load
        # -----------------------------
        load_data(dataframe)

        logger.info("Pipeline executed successfully.")

    except Exception as error:

        logger.exception(f"Pipeline Failed: {error}")

    finally:

        runtime = round(time.time() - start_time, 2)

        logger.info(f"Pipeline Runtime: {runtime} seconds")
        logger.info("Pipeline Finished")
        logger.info("=" * 70)


if __name__ == "__main__":
    run_pipeline()

