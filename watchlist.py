import requests
import json
import time
class watch_list():

    def watchlist(self, moviename, platform, session):
        """
        Creates a dictonary of the movies and 
        TV shows user watched and make recommendations for other movies and TV shows
        for the user

        Args:
        self
        moviename: The movie title
        platform: The platform it is streaming on

        Return:
        A dictonary of the movie and TV shows for the users
        """
        watchlist = client.get_watchlist_request()
        contents = []
        for list_ in watchlist:
            contents.append({
            'WatchlistID': list_.get('watchlistId')
            'Title': list_.get('title'),
            'Category': list_.get('category')
            })

            watched={"moviename":"platform"}
    
    def get_watchlist(self):
        if not logged_in(self._session):
            raise Exception("User must be logged in.")

        me = await fetch(self._session, API_URLS["me"])
        return me["watched"] 