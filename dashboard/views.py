from django.shortcuts import get_object_or_404, redirect, render
# from django.contrib.auth.decorators import login_required,permission_required
from .form import PostForm
from .models import post
import json

#@login_required
def dash_index(request):
   total_posts = post.objects.count()
   recent_posts = post.objects.order_by('-created_at')[:4] 
   prediction_data = {
        'dates': ['2024-11-20', '2024-11-21', '2024-11-22', '2024-11-23'],
        'values': [65, 70, 50, 110],
    }

    # Rendering the template with the context containing prediction data
   return render(request, 'index.html', {
        'total_posts': total_posts,
        'recent_posts': recent_posts,
        'prediction_data': json.dumps(prediction_data)  # Pass prediction data to the template
    })
#@login_required
def create_edit_post(request,post_id=None):
    instance = get_object_or_404(post, id=post_id) if post_id else None

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('manage-post')
    else:
        form = PostForm(instance=instance)
    return render(request,'post.html',{'form':form})

#@login_required
def post_manage(request):
    posts = post.objects.all()
    return render(request, 'manage_post.html',{'posts':posts})

#@login_required
def delete_post(request,post_id):
    post_find = get_object_or_404(post, id=post_id)
    if post:
        post_find.delete()
        return redirect('manage-post')
    return render(request,'manage_post.html')

def prediction(request):
    return render(request, 'prediction.html')
from django.shortcuts import render

# Define views for each static page
def terms_conditions(request):
    return render(request, 'terms-conditions.html')

def privacy_policy(request):
    return render(request, 'privacy-policy.html')

def Locate_Us(request):
    return render(request, 'Locate-Us.html')
