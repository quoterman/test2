from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import json
import api
from Database.models import D_PROJECT


def index(request):
    return render_to_response('BackEnd/index.html')


def download_repo(request):
    repo_path = request.POST["path"]
    repo_login = request.POST["login"]
    repo_password = request.POST["password"]
    try:
        url = repo_path[:8] + repo_login + ':' + repo_password + '@' + repo_path[8:]
        if api.valid(url):
            if D_PROJECT.objects.filter(LINK=repo_path, LOGIN=repo_login).exist(): # consider login and pass?
                id = D_PROJECT.objects.get(id=D_PROJECT.objects.filter(LINK=repo_path, LOGIN=repo_login).values("id"))
                api.git(url, id)
            else:
                project = D_PROJECT()
                project.LINK = repo_path
                project.LOGIN = repo_login
                project.PASSWORD = repo_password
                project.save()
                api.git(url, project.id)

        else:
            return HttpResponse(json.dumps({"response": 1}))
    except Exception:
        return HttpResponse(json.dumps({"response": 1}))
    else:
        return HttpResponse(json.dumps({"response": 0}))