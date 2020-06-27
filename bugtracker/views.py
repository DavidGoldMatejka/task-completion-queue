from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, MyProjects
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# To do for tomorrow:
#   On the DashBoard Page, Where turn the dashboard title into a dropdown menu of all the projects, then the progress bar/ pie chart / percent could just be for that project
#   Make a projects model where Posts are associated with a certain project


def Tracker(request):
    return redirect('/tracker/projects/1/')

    

class ProjectView(DetailView):
    model = MyProjects
    template_name = "bugtracker/index.html"

    def get_context_data(self, **kwargs):
        current_project =  self.get_object()
        posts = current_project.post_set.all()
        completed = posts.filter(status='Completed', project= current_project)
        inProgress = posts.filter(status='InProgress', project= current_project)
        Features = posts.filter(ticket_type='Features', project= current_project)
        Bug = posts.filter(ticket_type='Bug/Error', project= current_project)
        Design = posts.filter(ticket_type='Design', project= current_project)
        projects = MyProjects.objects.all()

        if posts.count() == 0:
            percentCompleted = 0
            percentBug = 0
            percentDesign = 0
            percentFeatures = 0
        else:
            percentBug = int((Bug.count()/posts.count())* 100) 
            percentDesign = int((Design.count()/posts.count())* 100) 
            percentFeatures = int((Features.count()/posts.count())* 100) 
            percentCompleted = int((completed.count()/posts.count())* 100) 



        if posts.filter(ticket_type="Design", project= current_project).count() == 0:
            completedDesign = 0
        else:
            completedDesign = int((completed.filter(ticket_type='Design', project= current_project).count() / posts.filter(ticket_type="Design", project= current_project).count()) * 100)

        if posts.filter(ticket_type="Bug/Error").count() == 0:
            completedBug = 0
        else: 
            completedBug = int((completed.filter(ticket_type='Bug/Error', project= current_project).count() / posts.filter(ticket_type="Bug/Error", project= current_project).count()) * 100)

        if posts.filter(ticket_type="Features").count() == 0:
            completedFeature = 0
        else:
            completedFeature = int((completed.filter(ticket_type='Features', project= current_project).count() / posts.filter(ticket_type="Features", project= current_project).count()) * 100)
            
        context = super().get_context_data(**kwargs)
        context['posts'] = posts
        context['completed'] = completed
        context['percentCompleted'] = percentCompleted
        context['inProgress'] = inProgress
        context['percentFeatures'] = percentFeatures
        context['percentBug'] = percentBug
        context['percentDesign'] = percentDesign
        context['completedBug'] = completedBug
        context['completedDesign'] = completedDesign
        context['completedFeature'] = completedFeature
        context['projects'] = projects
        context['project_title'] = current_project.title


        return context


    
    

#def Tables(request):
    #ordering = ["-priority"]
 #   context = {
#        'posts': Post.objects.all()
  #  }

   # return render(request, "bugtracker/tables.html", context)

def Tables(request):
    return redirect('/tracker/projects/1/tables')


class PostTableView(DetailView):
    model = MyProjects
    template_name ='bugtracker/tables.html'
    context_object_name = 'posts'
    ordering = ['priority']

    def get_context_data(self, **kwargs):
        current_project =  self.get_object()
        posts = current_project.post_set.all()
        context = super().get_context_data(**kwargs)
        context['posts'] = posts
        context['project_title'] = current_project.title
        context['projects'] = MyProjects.objects.all()
        return context

class ProjectListView(ListView):
    model = MyProjects
    template_name = 'bugtracker/projects.html'
    context_object_name = 'projects'





class PostListView(ListView):
    model = Post
    template_name ='bugtracker/tasklist.html'
    context_object_name = 'posts'
    ordering = ['priority']





class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'priority', 'ticket_type', 'status', 'assigned_developer']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.assigned_developer = self.request.user
        return super().form_valid(form)


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = MyProjects
    fields = ['title', 'description']



class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'priority', 'ticket_type', 'status', 'project']
    success_url = '/tracker/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/tracker/'
