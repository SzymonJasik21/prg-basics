results = [37, 51, 44, 23, 78, 92, 39, 84, 83, 51]

def min_pts(limit):
   return lambda pts: pts >= limit

pts_70 = list(filter(min_pts(70), results))
pts_40 = list(filter(min_pts(40), results))
pts_30 = list(filter(min_pts(30), results))

print(f"Min 70 pts: {pts_70}")
print(f"Min 40 pts: {pts_40}")
print(f"Min 30 pts: {pts_30}")