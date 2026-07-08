"""
extract.py

Extracts model information from the Hugging Face API
and saves the raw JSON response locally.
"""

import json
import requests

from config import (
    API_URL,
    REQUEST_TIMEOUT,
    RAW_JSON_PATH
)

from logger import logger


def extract_data():
    """
    Extract data from Hugging Face API.

    Returns:
        list: Raw JSON response containing model metadata.
    """

    logger.info("=" * 70)
    logger.info("Starting Extract Phase")

    try:

        response = requests.get(
            API_URL,
            timeout=REQUEST_TIMEOUT
        )

        response.raise_for_status()

        data = response.json()

        logger.info(f"Successfully extracted {len(data)} models.")
        logger.info(f"API Endpoint : {API_URL}")

        # Save raw JSON
        with open(RAW_JSON_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        logger.info(f"Raw JSON saved at: {RAW_JSON_PATH}")

        logger.info("Extract Phase Completed")
        logger.info("=" * 70)

        return data

    except requests.exceptions.RequestException as error:

        logger.exception(f"API Request Failed: {error}")

        raise

    except Exception as error:

        logger.exception(f"Unexpected Error: {error}")

        raise


if __name__ == "__main__":

    extract_data()
"""
extract.py

Extract data from the Hugging Face API and save it as raw JSON.
"""

import json
import requests

from config import (
    API_URL,
    RAW_JSON_PATH,
    REQUEST_TIMEOUT
)

from logger import logger


def extract_data():
    """
    Extract model data from Hugging Face API.
    """

    logger.info("Starting Extract Phase")

    try:
        response = requests.get(
            API_URL,
            timeout=REQUEST_TIMEOUT
        )

        response.raise_for_status()

        data = response.json()

        logger.info(f"Successfully extracted {len(data)} models.")

    except requests.exceptions.Timeout:
        logger.error("Request timed out.")
        raise

    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP Error: {e}")
        raise

    except requests.exceptions.RequestException as e:
        logger.error(f"Request Error: {e}")
        raise

    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        raise

    # Save raw JSON
    with open(RAW_JSON_PATH, "w") as file:
        json.dump(data, file, indent=4)

    logger.info(f"Raw data saved to {RAW_JSON_PATH}")

    return data


if __name__ == "__main__":

    extract_data()

logger.info("Extract Phase Completed")
