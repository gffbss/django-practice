# Create your views here.
from django.shortcuts import render, redirect
from hollywood.forms import MovieForm
from hollywood.models import Movie


def movies(request):
    movies = Movie.objects.all()
    return render(request, "movies.html", {'movies':movies})

def new_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid:
            if form.save():
                return redirect("/movies")

    else:
        form = MovieForm()
    data = {'form':form}
    return render(request, "new_movie.html", data)

def view_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    data = {'movie': movie}
    return render(request, "view_movie.html", data)

# Edit Movie info
def edit_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid:
            if form.save():
                return redirect("/movies/{}".format(movie_id))

    else:
        form = MovieForm(instance=movie)
    data = {"movie": movie, "form": form}
    return render(request, "edit_movie.html", data)

# Delete a Movie
def delete_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    movie.delete()
    return redirect("/movies")