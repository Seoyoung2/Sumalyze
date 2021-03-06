from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from itertools import chain
from operator import attrgetter
from django.views.generic import ListView
from pdf.models import PdfPost
from video.models import VideoPost
from audio.models import AudioPost
from text.models import TextPost
from image.models import ImagePost
from django.views.generic import ListView
from .crowling import image_crowling
# from lexrankr import LexRank

def main(request):
    return render(request, 'sumalyze/main.html')


# class StorageView(ListView):
#     template_name = 'sumalyze/storage.html'
#     context_object_name = 'posts'
#     paginate_by = 6

#     def get_queryset(self):
#         videos = VideoPost.objects.all()
#         audios = AudioPost.objects.all()
#         pdfs = PdfPost.objects.all()
#         posts = sorted(chain(pdfs, videos, audios),
#                     key=attrgetter('created'),
#                     reverse=True)         
#         return posts

@login_required
def storage(request):
    pdfs = PdfPost.objects.all()
    videos = VideoPost.objects.all()
    audios = AudioPost.objects.all()
    texts = TextPost.objects.all()
    images = ImagePost.objects.all()

    posts = sorted(chain(pdfs, videos, audios,texts,images),
                        key=attrgetter('created'),
                        reverse=True)
    paginator = Paginator(posts, 6) # Show 10 contacts per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'sumalyze/storage.html', {
        'posts': posts,
    })



@login_required
def pdfResult(request, pk):
    post = get_object_or_404(PdfPost, pk=pk)
    keyword_list = post.keyword.split('#')
    relevance_list = post.relevance.split('#')
    category_list = post.category_ibm.split('#')
    content_list = post.content.split('\n')
    index_list = post.index.split('#')
    index_list = list(filter(None, index_list))
    content_list = list(filter(None, content_list))

    keyword_pair = []
    for a,b in zip(keyword_list, relevance_list):
        keyword_pair.append((a,b))

    img_src = image_crowling(request, keyword_list[0])
    return render(request, 'sumalyze/result.html', {
        'post' : post,
        'keywords': keyword_pair,
        'categories': category_list,
        'index':index_list,
        'content':content_list,
        'image' : img_src,
    })


@login_required
def videoResult(request, pk):
    post = get_object_or_404(VideoPost, pk=pk)
    keyword_list = post.keyword.split('#')
    relevance_list = post.relevance.split('#')
    category_list = post.category_ibm.split('#')
    content_list = post.content.split('\n')
    index_list = post.index.split('#')
    index_list = list(filter(None, index_list))
    content_list = list(filter(None, content_list))

    keyword_pair = []
    for a,b in zip(keyword_list, relevance_list):
        keyword_pair.append((a,b))

    img_src = image_crowling(request, keyword_list[0])
    return render(request, 'sumalyze/result.html', {
        'post' : post,
        'keywords': keyword_pair,
        'categories': category_list,
        'index':index_list,
        'content':content_list,
        'image' : img_src,
    })


@login_required
def audioResult(request, pk):
    post = get_object_or_404(AudioPost, pk=pk)
    keyword_list = post.keyword.split('#')
    relevance_list = post.relevance.split('#')
    category_list = post.category_ibm.split('#')
    content_list = post.content.split('\n')
    index_list = post.index.split('#')
    index_list = list(filter(None, index_list))
    content_list = list(filter(None, content_list))
    keyword_pair = []
    for a,b in zip(keyword_list, relevance_list):
        keyword_pair.append((a,b))

    img_src = image_crowling(request, keyword_list[0])
    return render(request, 'sumalyze/result.html', {
        'post' : post,
        'keywords': keyword_pair,
        'categories': category_list,
        'index':index_list,
        'content':content_list,
        'image' : img_src,
    })


@login_required
def textResult(request, pk):
    post = get_object_or_404(TextPost, pk=pk)

    keyword_list = post.keyword.split('#')
    relevance_list = post.relevance.split('#')
    category_list = post.category_ibm.split('#')
    content_list = post.content.split('\n')
    index_list = post.index.split('#')
    index_list = list(filter(None, index_list))
    content_list = list(filter(None, content_list))
    keyword_pair = []
    for a,b in zip(keyword_list, relevance_list):
        keyword_pair.append((a,b))

    img_src = image_crowling(request, keyword_list[0])
    return render(request, 'sumalyze/result.html', {
        'post' : post,
        'keywords': keyword_pair,
        'categories': category_list,
        'index':index_list,
        'content':content_list,
        'image' : img_src,
    })

@login_required
def imageResult(request, pk):
    post = get_object_or_404(ImagePost, pk=pk)

    keyword_list = post.keyword.split('#')
    relevance_list = post.relevance.split('#')
    category_list = post.category_ibm.split('#')
    content_list = post.content.split('\n')
    index_list = post.index.split('#')
    index_list = list(filter(None, index_list))
    content_list = list(filter(None, content_list))
    keyword_pair = []
    for a,b in zip(keyword_list, relevance_list):
        keyword_pair.append((a,b))

    img_src = image_crowling(request, keyword_list[0])
    return render(request, 'sumalyze/result.html', {
        'post' : post,
        'keywords': keyword_pair,
        'categories': category_list,
        'index':index_list,
        'content':content_list,
        'image' : img_src,
    })
