class movie:
    def __init__(self,movie_title,director,rating):
        self.movie_title=movie_title
        self.director=director
        self.rating=rating

    def display(self):
        print("Movie title is",self.movie_title)
        print("Director is",self.director)
        print("rating is",self.rating )

    def check(self):
        if self.rating>8:
            print("blockbuster🎉")
        else:
            print("Flop😞")
obj1=movie("hello","kali devi",8)
obj1.display()
obj1.check()
