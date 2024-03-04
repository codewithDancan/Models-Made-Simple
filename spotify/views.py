from django.shortcuts import render
from spotify.models import PostMusic


# all(), filter(), exclude(), get(), first(), last(), exists(), orde_by(), reverse(), count()
# distinct(), values(), value_list(), annotate(), aggregate(), select_related(), prefetch_related()
# defer(), only()
def my_post(request):
    # posts = PostMusic.objects.all()
    # posts = PostMusic.objects.filter(artist_name='Pop Smoke')
    posts = PostMusic.objects.exclude(artist_name='Pop Smoke')
    # posts = PostMusic.objects.get(artist_name='Pop Smoke')

    context = {
        'posts': posts,
    }
    return render(request, 'post.html', context)
