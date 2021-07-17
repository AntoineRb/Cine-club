import os
import json
import logging

logging.basicConfig(level=logging.WARNING)


CUR_DIR = os.path.dirname(__file__) #Path to current directory
DATA_FILE = os.path.join(CUR_DIR, "data", "movies.json") #Path to Json file

def get_movies():
    """récupère une instance de la classe Movie pour chaque tire de films"""
    with open(DATA_FILE, "r", encoding='utf-8') as f:
        movies_titles = json.load(f)

    movies = [Movie(movie_title) for movie_title in movies_titles]  

    return movies    
    
    
class Movie:
    def __init__(self, title):
       self.title = title.title() #Init title format for title


    def __str__(self):
        """Return argument with title format"""
        return self.title

    def _get_movies(self):
        """Get values from list in json file"""
        with open(DATA_FILE, "r", encoding='utf-8') as f:
            return json.load(f)
                        
    def _write_movies(self, movies):
        """Insert values into json file list"""
        with open(DATA_FILE, "w") as f:
            json.dump(movies, f, indent=4)

    def add_to_movies(self):
        """add value at json file, returns a bool depend on operation result"""
        movies = self._get_movies()

        if not self.title in movies:
            movies.append(self.title)
            self._write_movies(movies) 
            return True
        else:
            logging.warning(f"Le Film {self.title} est déjà dans la liste")
            return False        

    def remove_from_movies(self):
        """Remove value from json file, returns a bool depend on operation result"""
        movies = self._get_movies()

        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f"Le film {self.title} n'est pas dans la liste.")
            return False



if __name__ == "__main__":
    m = Movie("harry potter")
    movies = get_movies()
    print(movies)
    








    

