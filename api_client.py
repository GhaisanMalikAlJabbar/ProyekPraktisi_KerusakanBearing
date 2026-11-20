
import os
import requests


# Alamat FastAPI
API_URL = os.getenv(
    "API_URL",
    "http://127.0.0.1:8000"
).rstrip("/")


def check_api_health():
    """Memeriksa apakah FastAPI tersedia."""

    try:
        response = requests.get(
            f"{API_URL}/health",
            timeout=5
        )

        response.raise_for_status()
        return response.json()

    except requests.RequestException as e:
        return {
            "status": "error",
            "message": str(e)
        }


def predict_bearing_api(input_data):
    """Mengirim data sensor ke endpoint FastAPI."""

    try:
        response = requests.post(
            f"{API_URL}/predict",
            json=input_data,
            timeout=30
        )

        response.raise_for_status()

        return response.json()

    except requests.HTTPError as e:

        try:
            detail = response.json().get(
                "detail",
                response.text
            )
        except ValueError:
            detail = response.text

        raise RuntimeError(
            f"API Error ({response.status_code}): {detail}"
        ) from e

    except requests.Timeout as e:
        raise RuntimeError(
            "Request timeout. FastAPI tidak merespons."
        ) from e

    except requests.ConnectionError as e:
        raise RuntimeError(
            "Tidak dapat terhubung ke FastAPI. "
            "Pastikan server backend berjalan."
        ) from e

    except requests.RequestException as e:
        raise RuntimeError(
            f"Terjadi kesalahan komunikasi API: {e}"
        ) from e
