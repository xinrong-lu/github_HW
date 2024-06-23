dic = {}
with open("IMDB-Movie-Data.csv", "r") as f:
	key = f.readline().split(",")
	line = f.readline().split(",")
	for i in range(len(key)):
		dic[key[i]] = []
	while len(line) > 1:
		for i in range(len(line)):
			dic[key[i]].append(line[i])
		line = f.readline().split(",")

def top3_rating_2016(lst1, lst2, lst3):
    ratings_movies = list(zip(lst1, lst2, lst3))
    ratings_movies_2016 = [movie for movie in ratings_movies if movie[2] == "2016"]
    ratings_movies_2016.sort(reverse=True)
    top3_movies = ratings_movies_2016[:3]
    top3_movies_titles = [movie for _, movie, _ in top3_movies]
    return top3_movies_titles

top3_movies = top3_rating_2016(dic["Rating"], dic["Title"], dic["Year"])
print("Top-3 movies with the highest ratings in 2016?", end=" ")
print(", ".join(top3_movies))

def most_director(lst):
	counts = {}
	for item in lst:
		if item in counts:
			counts[item] += 1
		else:
			counts[item] = 1
	max_count = 0
	max_director = ""
	for item, count in counts.items():
		if count > max_count:
			max_count = count
			max_director = item
	return max_director

max_director = most_director(dic["Director"])
print("The director who involves in the most movies? ", end="")
print(max_director)

def highest_total_revenue(lst1, lst2):
    actor_revenue = {}
    for i in range(len(lst2)):
        revenue = lst2[i]
        if revenue == "":
            revenue = 0
        else:
            revenue = float(revenue)
        actor_list = lst1[i].split('|')
        for actor in actor_list:
            if actor in actor_revenue:
                actor_revenue[actor] += revenue
            else:
                actor_revenue[actor] = revenue
    highest_total_revenue_actor = max(actor_revenue, key=actor_revenue.get)
    return highest_total_revenue_actor

highest_actor_revenue = highest_total_revenue(dic["Actors"], dic["Revenue (Millions)"])

print("The actor generating the highest total revenue? ", end="")
print(highest_actor_revenue)

def Emma_average_rating(lst1, lst2):
    total_rating = 0
    n = 0
    for actors, rating in zip(lst1, lst2):
        actor_list = [actor.strip() for actor in actors.split('|')]
        if "Emma Watson" in actor_list:
            n += 1
            total_rating += float(rating)
    average_rating = total_rating / n if n != 0 else 0
    return average_rating

print("The average rating of Emma Watson’s movies? ", end="")
print(Emma_average_rating(dic["Actors"], dic["Rating"]))

def top4_actors(lst1):
	actor_time = {}
	for actors in lst1:
		actor_list = [actor.strip() for actor in actors.split('|')]
		for actor in actor_list:
			if actor in actor_time:
				actor_time[actor] += 1
			else:
				actor_time[actor] = 1
	top_actor = sorted(actor_time.items(), key=lambda x: x[1], reverse=True)[:4]
	top4_actor = [actor for actor, _ in top_actor]
	return top4_actor

top4_actor = top4_actors(dic["Actors"])
print("Top‐4 actors playing the most movies? ", end="")
print(", ".join(top4_actor))

def top7_pairs(lst1, lst2):
	director_actor = {}
	for director, actors in zip(lst1, lst2):
		actor_list = [actor.strip() for actor in actors.split('|')]
		for actor in actor_list:
			if (director, actor) in director_actor:
				director_actor[(director, actor)] += 1
			else:
				director_actor[(director, actor)] = 1
	top_pairs = sorted(director_actor.items(), key=lambda x: x[1], reverse=True)[:7]
	top7_pairs = [(director, actor) for (director, actor), _ in top_pairs]
	top7_pairs = ['{}&{}'.format(director, actor) for (director, actor), _ in top_pairs]
	return top7_pairs

top7_pairs = top7_pairs(dic["Director"], dic["Actors"])
print("Top‐7 frequent collaboration pairs of director & actor? ", end="")
print(", ".join(top7_pairs))

def top3_director(lst1, lst2):
	director_actor = {}
	for director, actors in zip(lst1, lst2):
		actor_list = [actor.strip() for actor in actors.split('|')]
		if director not in director_actor:
			director_actor[director] = set()
		for actor in actor_list:
			director_actor[director].add(actor)
	top3_director = sorted(director_actor.items(), key=lambda x: len(x[1]), reverse=True)[:3]
	top3_director = [director for director, _ in top3_director]
	return top3_director

top3_director = top3_director(dic["Director"], dic["Actors"])
print("Top‐3 directors who collaborate with the most actors? ", end="")
print(", ".join(top3_director))

def top6_actor_genre(lst1, lst2):
	actor_genre = {}
	for actors, genres in zip(lst1, lst2):
		actor_list = [actor.strip() for actor in actors.split('|')]
		genre_list = [genre.strip() for genre in genres.split('|')]
		for actor in actor_list:
			if actor not in actor_genre:
				actor_genre[actor] = set()
			for genre in genre_list:
				if genre not in actor_genre[actor]:
					actor_genre[actor].add(genre)
	top6_actor = sorted(actor_genre.items(), key=lambda x: len(x[1]), reverse=True)[:6]
	top6_actor = [actor for actor, _ in top6_actor]
	return top6_actor

top6_actor = top6_actor_genre(dic["Actors"], dic["Genre"])
print("Top‐6 actors playing in the most genres of movies? ", end="")
print(", ".join(top6_actor))

def top3_actor_gap(lst1, lst2):
	actor_year = {}
	for actors, year in zip(lst1, lst2):
		actor_list = [actor.strip() for actor in actors.split('|')]
		for actor in actor_list:
			if actor not in actor_year:
				actor_year[actor] = set()
			if year not in actor_year[actor]:
				actor_year[actor].add(int(year))
	for actor in actor_year:
		gap = max(actor_year[actor]) - min(actor_year[actor])
		actor_year[actor] = gap
	top3_actor_gap = sorted(actor_year.items(), key=lambda x: x[1], reverse=True)[:3]
	top3_actor = [actor for actor, _ in top3_actor_gap]
	return top3_actor

top3_actor = top3_actor_gap(dic["Actors"], dic["Year"])
print("Top‐3 actors whose movies lead to the largest maximum gap of years? ", end="")
print(", ".join(top3_actor))