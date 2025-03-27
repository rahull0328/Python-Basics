# Sort a dictionary by values in descending order

scores = {'John': 85, 'Emma': 92, 'Ava': 78, 'Mike': 90}

sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))
print(sorted_scores)
