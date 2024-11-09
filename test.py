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



def get_city_id(city):
        #! connect to bd
        conn = sqlite3.connect('databases/database.db')
        cur = conn.cursor()
        
        city_id = cur.execute('''
            SELECT id
            FROM worldcities
            WHERE city = ?
        ''', (city,)
        )

        #! close connection
        conn.close()

        return str(city_id)

print(len('ffffffffffffffffffffffffffffffffffffffff'))