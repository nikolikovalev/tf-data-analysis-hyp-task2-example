import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu


chat_id = 411809593 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    a = 0.06
    res = mannwhitneyu(x, y)
    return res.pvalue < a
