import csv
import sqlite3
import time

start = time.time()


conn = sqlite3.connect('databases/database.db')

cur = conn.cursor()

# with open('databases/worldcities.csv', 'r', encoding='utf-8') as file:
#     reader = csv.DictReader(file, delimiter=',')

#     for row in reader:
#         cur.execute('''
#             INSERT INTO worldcities (city, city_ascii, lat, lng, country)
#             VALUES (?,?,?,?,?)
#         ''', (row['city'], row['city_ascii'], row['lat'], row['lng'], row['country'])
#         )


conn = sqlite3.connect('databases/database.db')
cur = conn.cursor()



conn.commit()

end = time.time()

print(f'Time taken: {end - start} seconds')


user: tuple = cur.execute(
            '''
                SELECT *
                FROM user
                WHERE username = ? AND password = ?
            ''', ('Oqisu', "1234")).fetchone()

print(user)
print(len('ffffffffffffffffffffffffffffffffffffffff'))