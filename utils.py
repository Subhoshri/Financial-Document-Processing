def assign_confidence_score(key_values):
    confidence_scores = [value for key, value in key_values.items()]
    avg_confidence = sum(confidence_scores) / len(confidence_scores)
    return avg_confidence

def flag_low_confidence(avg_confidence, threshold=0.8):
    return avg_confidence < threshold
