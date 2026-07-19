from plantmd.inference import IMAGE_SIZE, LABELS, predict_top_k, preprocess_image


def test_labels_cover_38_classes_with_no_gaps():
    assert len(LABELS) == 38
    assert set(LABELS.values()) == set(range(38))


def test_preprocess_image_shape_and_range(synthetic_image_path):
    processed = preprocess_image(synthetic_image_path)
    assert processed.shape == (1, *IMAGE_SIZE, 3)
    assert processed.min() >= 0.0
    assert processed.max() <= 1.0


def test_predict_top_k_returns_sorted_top_k(synthetic_image_path, fake_model):
    processed = preprocess_image(synthetic_image_path)
    results = predict_top_k(processed, fake_model, k=3)

    assert len(results) == 3
    labels = [label for label, _ in results]
    assert labels[0] == "Tomato healthy"
    confidences = [confidence for _, confidence in results]
    assert confidences == sorted(confidences, reverse=True)
