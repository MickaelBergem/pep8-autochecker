from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import get_object_or_404
from models import Project, Repository
from pep8runs.models import Run
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.core.urlresolvers import reverse
import simplejson
from github import Github
from allauth.socialaccount.models import SocialAccount, SocialToken


class RunsList(ListView):
    context_object_name = "liste_bdc"
    template_name = "bsct/plain/list.html"

    def get_queryset(self):
        self.project = get_object_or_404(Project, id=self.kwargs['pk'])
        return Run.objects.filter(project=self.project)


class ProjectDetail(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'

    def get_plot(self):
        plot = {'title': 'Number of issues'}

        plot_list = []

        total_errors_list = [
            [run.time_start.ctime(), run.total_errors]
            for run in Run.objects.filter(project=self.object, status='ok').order_by('time_start').all()
        ]

        plot_list.append({'points': total_errors_list, 'label': 'Number of total issues'})

        plot['plot_list'] = plot_list

        return plot


class ProjectImport(TemplateView):
    template_name = "projects/project_import.html"

    def get_repo_list(self):
        if self.request.user.is_authenticated():
            # Authenticated user
            try:
                # Retrieve GitHub User
                social_account = SocialAccount.objects.get(user=self.request.user)

                token = SocialToken.objects.get(account=social_account)

                g = Github(token.token)

                return g.get_user().get_repos()

            except SocialAccount.DoesNotExist as e:
                # TODO
                print "SocialAccount does not exist..."
                pass

        else:
            # Anonymous user
            print "Not authenticated"


def ProjectImporter(request, repo_id):

    if request.user.is_authenticated():
        # Authenticated user
        try:
            # Retrieve GitHub User
            social_account = SocialAccount.objects.get(user=request.user)
            token = SocialToken.objects.get(account=social_account)
            g = Github(token.token)

            # Save repositories if not already existing
            for repo in g.get_user().get_repos():
                Repository.objects.get_or_create(
                    id=repo.id,
                    defaults={
                        'name': repo.name,
                        'owner': request.user,
                        'github_object': repo.raw_data
                    }
                )

            # Bind the repository to a project
            repo = Repository.objects.get(id=repo_id)
            repo_git_url = simplejson.loads(repo.github_object)['clone_url']

            project = Project.objects.create(
                name=repo.name,
                repository=repo,
                git_url_clone=repo_git_url
            )

            return HttpResponseRedirect(reverse('project_list'))

        except Repository.DoesNotExist as e:
            return HttpResponseNotFound('Repository not found')

        except SocialAccount.DoesNotExist as e:
            # TODO
            print "SocialAccount does not exist..."
            pass

    else:
        # Anonymous user
        print "Not authenticated"

    return HttpResponseRedirect(reverse('project_import'))
