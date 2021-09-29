from typing import List, Dict
import json


# class Rating:
#     def __init__(self, name: str, rating: float) -> None:
#         self.name = name
#         self.rating = rating


class Movie:
    def __init__(self, title, ratings: dict = {}) -> None:
        self.title = title
        self.ratings = ratings

    def print_movie(self):
        if len(self.ratings):
            print('{:<40}{:<10.2f}'.format(self.title, sum(map(
                lambda r: r[1], self.ratings.items())) / len(self.ratings)))
        else:
            print('{:<40}{:<10}'.format(self.title, 'Фильм не оценивался'))

    def print_movie_with_rating(self, rating):
        rating_sum = 0

        if len(rating) == 0:
            print('Фильм не оценивался')
        else:
            for i in rating.values():
                rating_sum += i
            for i in rating.items():
                print('{:<15}{:15}'.format(i[0], i[1]))
            average_rating = rating_sum / len(rating)
            print('{:<15}{:15}'.format('Средняя оценка',
                                       "{0:.2f}".format(average_rating)))

    def to_dict(self):
        return {
            'title': self.title,
            'ratings': self.ratings
        }


class MovieList:
    def __init__(self, movies: List[Movie] = []) -> None:
        self.movies = movies

    def command_list(self):
        print()
        print('{:<40}{:<10}'.format('Название фильма', 'Средний рейтинг'))
        for movie in self.movies:
            movie.print_movie()
        print()

    def find_movie(self, title: str):
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                return movie

    def add_movie(self, movie: Movie):
        self.movies.append(movie)
        print(movie.title)
        print(self.movies)

    def delete_movie(self, title: str):
        print(self.movies)
        movie = self.find_movie(title)
        self.movies.remove(movie)

        print(self.movies)

    def rate_movie(self, title: str, name: str, rating: float):

        movie = self.find_movie(title)
        if rating > 0 and rating <= 10:
            movie.ratings[name] = rating
        if rating == 0:
            movie.ratings.pop(name)

        movie.print_movie()


class Application:
    def __init__(self) -> None:
        self.movie_list = None
        self.load_from_file()

        self.commands = {
            'add': self.command_add,
            'delete': self.command_delete,
            'list': self.movie_list.command_list,
            'rate': self.command_rate,
            'find': self.command_find,
            'exit': self.command_exit,
        }

    def command_rate(self):
        movie_title = input("Введите название фильма > ")
        name = input("Введите своё имя > ")
        rating = int(input("Введите оценку от 1 до 10 > "))
        self.movie_list.rate_movie(movie_title, name, rating)
        self.save_to_file()

    def command_find(self):
        title = input('Для поиска введите название фильма > ')
        movie = self.movie_list.find_movie(title)
        print(movie.title)
        movie.print_movie_with_rating(movie.ratings)

    def command_add(self):
        name = input('Введите название фильма > ')
        movie = Movie(name)
        self.movie_list.add_movie(movie)
        self.save_to_file()

    def command_delete(self):
        title = input('Введите название фильма > ')
        self.movie_list.delete_movie(title)

        self.save_to_file()

    def load_from_file(self):
        with open('movies.json') as f:
            movies = []
            for movie_data in json.load(f):
                movie = Movie(movie_data['title'], movie_data['ratings'])
                movies.append(movie)
            self.movie_list = MovieList(movies)

    def save_to_file(self):
        with open('movies.json', 'w') as f:
            preparing_movies = [m.to_dict() for m in self.movie_list.movies]
            json.dump(preparing_movies, f, indent=4, ensure_ascii=False)

    def run(self):
        while True:
            self.commands_list = ['add', 'list',
                                  'rate', 'find', 'delete', 'exit']
            command = input(
                'Введите команду:\nadd, list, rate, find, delete, exit > ')

            if command in self.commands_list:
                self.commands[command]()
            else:
                print('Нет такой команды!')

    def command_exit(self):
        exit('До свидания!')


app = Application()
app.run()
