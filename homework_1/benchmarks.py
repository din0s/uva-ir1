import json

if __name__ == '__main__':
    with open('results_part1.json', 'r') as f:
        results = json.load(f)

    # TODO: We do not have bow (binary)

    assert results['2']['BOW']['Recall@5'] >= 0.0279
    assert results['2']['BOW']['Precision@5'] >= 0.0484

    assert results['2']['TF-IDF']['Recall@10'] >= 0.1175
    assert results['2']['TF-IDF']['Precision@10'] >= 0.0969

    # TODO: We do not have recall@20 and precision@20.
    # assert results['2']['NaiveQL']['Recall@20'] >= 0.0130
    # assert results['2']['NaiveQL']['Precision@20'] >= 0.0086

    assert results['2']['QL']['Recall@5'] >= 0.1211
    assert results['2']['QL']['Precision@5'] >= 0.2261

    assert results['2']['BM25']['Recall@10'] >= 0.1937
    assert results['2']['BM25']['Precision@10'] >= 0.1973
