from plantmd.descriptions import FALLBACK_DESCRIPTION, format_description, load_descriptions


def test_load_descriptions_preserves_embedded_commas(tmp_descriptions_csv):
    """Regression test: the old `line.split(',')` parser truncated at the first comma."""
    descriptions = load_descriptions(tmp_descriptions_csv)
    assert descriptions["Corn Leaf spot"] == (
        "Symptoms are sometimes confused with northern leaf blight, "
        "southern leaf blight, and anthracnose."
    )


def test_format_description_known_label(tmp_descriptions_csv):
    descriptions = load_descriptions(tmp_descriptions_csv)
    header, body = format_description(("Apple Scab", 87.654), descriptions)
    assert header == "Apple Scab : 87.654%"
    assert body == "Apple scab affects leaves and fruit."


def test_format_description_missing_label_falls_back(tmp_descriptions_csv):
    descriptions = load_descriptions(tmp_descriptions_csv)
    _, body = format_description(("Some Unknown Class", 50.0), descriptions)
    assert body == FALLBACK_DESCRIPTION
