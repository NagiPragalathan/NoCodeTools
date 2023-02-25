from django.urls import path
from .Routes import NoCodeViews
from .Routes import BlogViews


#Initilizes........................

urlpatterns = []
def Make_Join(Componets):
    OutComponets = []
    for i in Componets:
        for j in i:
            OutComponets.append(j)
    return OutComponets


# Paths.............................

NoCodeMaker = [
    path('',NoCodeViews.index, name='home'),
    path('add', NoCodeViews.addPage, name="addpage"),
    path('edit/<id>', NoCodeViews.editPage, name="editpage"),
    path('page/create', NoCodeViews.savePage, name="create_page"),
    path('editPage/<id>', NoCodeViews.editPageContent, name="editPageContent"),
    path('preview/<id>', NoCodeViews.previewPage, name='previewPage')
]

BlogBuilder = [
    path('list_blog',BlogViews.list_blog),
    path('list_edit_blog',BlogViews.list_edit_blog),
    path('view_blog/<str:pk>',BlogViews.view_blog),
    path('edit_blog/<str:pk>',BlogViews.edit_blog),
    path('blog_edit',BlogViews.blog_edit),
    path('save_blog',BlogViews.save_blog),
    path('delete_blog',BlogViews.delete_blog),
    path('edit_blog/save_edit_blog/<int:pk>',BlogViews.save_edit_blog),
]



# Add Paths Together..............

urlpatterns.extend(Make_Join([NoCodeMaker,BlogBuilder]))

