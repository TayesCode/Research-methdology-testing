def compute_asr(successes, total):

    return successes / total


def compute_tpr(tp, fn):

    return tp / (tp + fn)


def compute_fpr(fp, tn):

    return fp / (fp + tn)


def compute_accuracy(correct, total):

    return correct / total