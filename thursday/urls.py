from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'thursday.views.home', name='home'),
    # url(r'^thursday/', include('thursday.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^movies/$', 'hollywood.views.movies', name='movies'),
    url(r'^movies/new/$', 'hollywood.views.new_movie', name='new_movie'),
    url(r'^movies/(?P<movie_id>\w+)/$', 'hollywood.views.view_movie', name='view_movie'),
    url(r'^movies/(?P<movie_id>\w+)/edit$', 'hollywood.views.edit_movie', name='edit_movie'),
    url(r'^movies/(?P<movie_id>\w+)/delete', 'hollywood.views.delete_movie', name='delete_movie'),


)
