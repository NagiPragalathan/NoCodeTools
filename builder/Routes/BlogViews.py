from ..models import Blog
from django.shortcuts import render
from .Tool.Tools import get_blog 


def blog_edit(request):
    return render(request,"BlogBuilder/blog_edit.html")

def save_blog(request):
    ids = ['#title','#description','#content','#Category','#Thumbnail']
    title = request.POST.get(ids[0])
    description = request.POST.get(ids[1])
    content = request.POST.get(ids[2])
    Category = request.POST.get(ids[3])
    Thumbnail = request.POST.get(ids[4])

    obj = Blog(title=title,description=description,content=content,categories=Category,blog_profile_img=Thumbnail)
    obj.save()
    ob = Blog.objects.all()
    for i in ob:
        print(i.blog_profile_img,i.title,i.content)

    return render(request,"BlogBuilder/blog_edit.html")

def save_edit_blog(request,pk):
    ids = ['#title','#description','#content','#Category','#Thumbnail']
    title = request.POST.get(ids[0])
    description = request.POST.get(ids[1])
    content = request.POST.get(ids[2])
    Category = request.POST.get(ids[3])
    Thumbnail = request.POST.get(ids[4])

    obj = Blog.objects.get(id=pk)
    obj.content = content
    obj.title = title
    obj.description = description
    obj.categories = Category
    obj.blog_profile_img = Thumbnail
    obj.save()

    print("Saved...........")

    return render(request,"BlogBuilder/blog_edit.html")


def list_blog(request):
    items = get_blog()
    return render(request,"BlogBuilder/Blog.html",{'blogs':items})

def view_blog(request,pk):
    page = Blog.objects.get(id=pk)
    items = get_blog()
    return render(request,"BlogBuilder/view_Blog.html",{'blog':page,'item':items})

def delete_blog(request):
    bl_id = request.GET.get("id")
    page = Blog.objects.get(id=bl_id)
    page.delete()
    return render(request,"BlogBuilder/view_Blog.html",{'blog':page})

def list_edit_blog(request):
    items = get_blog()
    return render(request,"BlogBuilder/edit_blog_list.html",{'blogs':items})

def edit_blog(request,pk):
    obj = Blog.objects.get(id=pk)
    return render(request,"BlogBuilder/blog_re_edit.html",{'obj':obj})
