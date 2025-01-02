from typing import List

def list_avg(seq: list) -> float:
    return sum(seq)/len(seq)

print(list_avg([123]))