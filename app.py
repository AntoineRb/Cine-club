from PySide2 import QtWidgets, QtCore
from movie import get_movies, Movie

class App(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ciné Club")
        self.resize(300, 400)
        self.setup_ui() 
        self.populate_movies() 
        self.setup_connections()
        self.setup_css()

    def setup_ui(self):
        """Creates and sets Widgets in instance"""
        self.layout_ = QtWidgets.QVBoxLayout(self) 

        self.le_movieTitle = QtWidgets.QLineEdit() 
        self.btn_submit = QtWidgets.QPushButton("Ajouter un film") 
        self.lw_movies = QtWidgets.QListWidget()  
        self.lw_movies.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection) 
        self.btn_delete = QtWidgets.QPushButton("Supprimer le(s) film(s)")  

        #Set Widgets in layout_
        self.layout_.addWidget(self.le_movieTitle)
        self.layout_.addWidget(self.btn_submit)
        self.layout_.addWidget(self.lw_movies)
        self.layout_.addWidget(self.btn_delete)

    def setup_connections(self):
        """Connect Widgets -> api(movie.py)"""
        # Add movie in list
        self.le_movieTitle.returnPressed.connect(self.add_movie) 
        self.btn_submit.clicked.connect(self.add_movie) 
        # remove movie from list
        self.btn_delete.clicked.connect(self.remove_movie)

    def populate_movies(self):
        """Return movies from Json file list"""
        movies = get_movies()
        for movie in movies:
            lw_item = QtWidgets.QListWidgetItem(movie.title) 
            lw_item.setData(QtCore.Qt.UserRole, movie) 
            self.lw_movies.addItem(lw_item)

    def add_movie(self):
        """Insert value : LineEdit --> Json"""
        movie_title = self.le_movieTitle.text()

        if not movie_title: #for empty string
            return False

        movie = Movie(title=movie_title)
        resultat = movie.add_to_movies()

        if resultat:
            lw_item = QtWidgets.QListWidgetItem(movie.title) 
            lw_item.setData(QtCore.Qt.UserRole, movie) 
            self.lw_movies.addItem(lw_item)
        
        self.le_movieTitle.setText("") #Clear lineEdit field
       
    def remove_movie(self):
        for selected_item in self.lw_movies.selectedItems():
            movie = selected_item.data(QtCore.Qt.UserRole)   
            movie.remove_from_movies() 
            self.lw_movies.takeItem(self.lw_movies.row(selected_item))

    def setup_css(self):
        self.setStyleSheet("background-color: rgba(82, 117, 179, 0.5);")

        self.btn_submit.setStyleSheet("background-color: rgb(196, 196, 196);")

        self.btn_delete.setStyleSheet("background-color: rgb(196, 196, 196);")

        self.le_movieTitle.setStyleSheet("""
        background-color: rgb(196, 196, 196);
        border: none;
        """)

        self.lw_movies.setStyleSheet("""
        background-color: rgb(196, 196, 196);
        border: none;
        """)




if __name__ == "__main__":
    app = QtWidgets.QApplication([])  
    Win = App()  
    Win.show()   
    app.exec_()  



