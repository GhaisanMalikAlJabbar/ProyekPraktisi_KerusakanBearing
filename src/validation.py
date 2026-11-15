
import math
from numbers import Real


def get_allowed_categories(model):
    """
    Mengambil kategori yang dikenal model
    langsung dari OneHotEncoder.
    """

    preprocessor = model.named_steps["preprocessor"]

    categorical_columns = []
    categorical_pipeline = None

    for name, transformer, columns in preprocessor.transformers_:
        if name == "cat":
            categorical_columns = list(columns)
            categorical_pipeline = transformer
            break

    if categorical_pipeline is None:
        return {}

    encoder = categorical_pipeline.named_steps["encoder"]

    categories = {}

    for column, values in zip(
        categorical_columns,
        encoder.categories_
    ):
        categories[column] = [
            str(value) for value in values
        ]

    return categories


def validate_input(input_data, model):
    """
    Memvalidasi input sebelum prediksi.

    Pemeriksaan:
    1. Input harus berupa dictionary.
    2. Semua fitur wajib tersedia.
    3. Tidak boleh ada fitur tambahan.
    4. Fitur numerik harus berupa angka finite.
    5. Fitur kategorikal harus dikenal model.

    Mengembalikan dictionary yang sudah dinormalisasi.
    """

    if not isinstance(input_data, dict):
        raise TypeError(
            "Input harus berupa dictionary."
        )

    preprocessor = model.named_steps["preprocessor"]

    expected_features = list(
        preprocessor.feature_names_in_
    )

    # Memeriksa fitur yang hilang
    missing_features = [
        feature
        for feature in expected_features
        if feature not in input_data
    ]

    if missing_features:
        raise ValueError(
            f"Fitur wajib belum diisi: {missing_features}"
        )

    # Memeriksa fitur yang tidak dikenal
    extra_features = [
        feature
        for feature in input_data
        if feature not in expected_features
    ]

    if extra_features:
        raise ValueError(
            f"Fitur tidak dikenal: {extra_features}"
        )

    allowed_categories = get_allowed_categories(model)

    validated_data = {}

    for feature in expected_features:

        value = input_data[feature]

        # Menolak nilai kosong
        if value is None:
            raise ValueError(
                f"Fitur '{feature}' tidak boleh kosong."
            )

        # Validasi kategorikal
        if feature in allowed_categories:

            if not isinstance(value, str):
                raise ValueError(
                    f"Fitur '{feature}' harus berupa teks."
                )

            value = value.strip()

            if value == "":
                raise ValueError(
                    f"Fitur '{feature}' tidak boleh kosong."
                )

            if value not in allowed_categories[feature]:
                raise ValueError(
                    f"Nilai '{value}' tidak dikenal untuk "
                    f"fitur '{feature}'. Pilihan yang tersedia: "
                    f"{allowed_categories[feature]}"
                )

            validated_data[feature] = value

        # Validasi numerik
        else:

            if isinstance(value, bool) or not isinstance(value, Real):
                raise ValueError(
                    f"Fitur '{feature}' harus berupa angka."
                )

            if not math.isfinite(float(value)):
                raise ValueError(
                    f"Fitur '{feature}' harus berupa angka finite."
                )

            validated_data[feature] = float(value)

    return validated_data
