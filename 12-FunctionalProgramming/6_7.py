judge_scores = [
    (17, 15, 16, 17, 15),
    (16, 18, 19, 17, 19),
    (19, 15, 15, 19, 18),
    (18, 17, 19, 15, 16)
]

total_points = list(map(lambda s: sum(s) - min(s) - max(s), judge_scores))

print(total_points)