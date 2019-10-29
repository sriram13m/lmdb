import csv
import ast

with open('./table_movie.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    m = []
    for i, row in enumerate(csv_reader):
        m.append(row[1])
    m = set(m)
    
with open('credits.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    w = []
    unique_mov_cast = set()
    for i, row in enumerate(csv_reader):
        if i == 0:
            cast_index = row.index('cast')
            movie_index = row.index('id')
            targets = [cast_index]
        else:
            movie_id = row[movie_index]
            for i, t in enumerate(targets):
                dicts = ast.literal_eval(row[t])
                for d in dicts:
                    if movie_id in m:
                        if (movie_id, d.get('id')) not in unique_mov_cast:
                            unique_mov_cast.add((movie_id, d.get('id')))
                            w.append((movie_id, d.get('character'), d.get('id')))
                        
print(len(w))
w = set(w)
print(len(w))
with open('table_act.csv','w') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(['mov_id', 'role','cast_id'])
    for i, row in enumerate(w):
        csv_out.writerow(row)