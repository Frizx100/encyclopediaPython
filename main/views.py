from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import*
# Create your views here.
def index(request):
    category = list(Category.objects.order_by("order"))
    post = Article.objects.all()
    context = {
        'category': category,
        'pos': post
    }
    return render(request, 'main/main.html', context=context)

class ArticleView(DetailView):
    # specify the model to use
    model = Article

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleView,
             self).get_context_data(*args, **kwargs)
        # add extra field 
        context["category"] = list(Category.objects.order_by("order"))    
        return context