# Author: Kevin Riemer
# GitHub username: khriemer2596
# Date: 5/19/2022
# Description: Creates 3 private classes. Movie contains movies and their information.
#              StreamingService contains a dictionary of movies with the ability to
#              add and remove movies. StreamingGuide tells the user what streaming
#              services they can use to watch their movie, if there are any.

class Movie:
    """A Movie class that creates/stores information on the movie"""

    def __init__(self, title, genre, director, year):
        """Initializes objects"""
        self._title = title
        self._genre = genre
        self._director = director
        self._year = year

    def get_title(self):
        """Get method for title"""
        return self._title

    def get_genre (self):
        """Get method for genre"""
        return self._genre

    def get_director(self):
        """Get method for director"""
        return self._director

    def get_year(self):
        """Get method for year"""
        return self._year


class StreamingService:
    """
    A streaming service class that creates a dictionary of movies
    and assigns each movie to the corresponding streaming service
    """

    def __init__(self, name):
        """Initializes objects and creates an empty dictionary called catalog"""
        self._name = name
        self._catalog = {}

    def get_name(self):
        "Get method for streaming service name"
        return self._name

    def get_catalog(self):
        """Get method for the catalog"""
        return self._catalog

    def add_movie(self, movie_object):
        """Adds a movie to the catalog"""
        movie_name = movie_object.get_title()
        self._catalog[movie_name] = movie_object

    def delete_movie(self, movie_title):
        """Removes a movie from the catalog"""
        if movie_title in self.get_catalog():
            self._catalog.pop(movie_title)


class StreamingGuide:
    """
    A streaming guide class that tells the user where to
    watch a movie
    """

    def __init__(self):
        """Initializes the empty streaming services list"""
        self._streaming_serv = []

    def add_streaming_service(self, streaming_service_obj):
        """Adds a streaming service to the list"""
        self._streaming_serv.append(streaming_service_obj)

    def delete_streaming_service(self, streaming_service_name):
        """Removes a streaming service from the list"""
        if streaming_service_name in self._streaming_serv:
            self._streaming_serv.remove(streaming_service_name)

    def where_to_watch(self, movie_title):
        """
        Shows the user where to watch the given movie and gives some
        information about it
        """
        streaming_list = []
        for key in self._streaming_serv:
            catalog_instance = key.get_catalog()
            if movie_title in catalog_instance:
                movie_obj = catalog_instance[movie_title]
                year = movie_obj.get_year()
                movie_title_and_year = movie_title + " (" + str(year) + ")"
                streaming_list.append(movie_title_and_year)

        if len(self._streaming_serv) > 0:
            for key in self._streaming_serv:
                if movie_title in key.get_catalog():
                    streaming_options = key.get_name()
                    streaming_list.append(streaming_options)
                    return streaming_list

        else:
            print("None")


#movie_1 = Movie('The Seventh Seal', 'comedy', 'Ingmar Bergman', 1957)
#movie_2 = Movie('Home Alone', 'tragedy', 'Chris Columbus', 1990)
#movie_3 = Movie('Little Women', 'action thriller', 'Greta Gerwig', 2019)
#movie_4 = Movie('Galaxy Quest', 'historical documents', 'Dean Parisot', 1999)

#stream_serv_1 = StreamingService('Netflick')
#stream_serv_1.add_movie(movie_2)

#stream_serv_2 = StreamingService('Hula')
#stream_serv_2.add_movie(movie_1)
#stream_serv_2.add_movie(movie_4)
#stream_serv_2.delete_movie('The Seventh Seal')
#stream_serv_2.add_movie(movie_2)

#stream_serv_3 = StreamingService('Dizzy+')
#stream_serv_3.add_movie(movie_4)
#stream_serv_3.add_movie(movie_3)
#stream_serv_3.add_movie(movie_1)

#stream_guide = StreamingGuide()
#stream_guide.add_streaming_service(stream_serv_1)
#stream_guide.add_streaming_service(stream_serv_2)
#stream_guide.add_streaming_service(stream_serv_3)
#stream_guide.delete_streaming_service('Hula')
#search_results = stream_guide.where_to_watch('Little Women')
#print(search_results)






