import subprocess
import os


def valid(url):
    pr = subprocess.Popen(['curl -s -o /dev/null -w "%{http_code}" ' + url],
                          cwd=os.path.abspath(os.curdir),
                          stdin=subprocess.PIPE,
                          stdout=subprocess.PIPE,
                          shell=True,
    )
    out, error = pr.communicate()
    return out == 200 or out == 302 or out == 301


def getPathToFolder(folder):
    path = os.getcwd()
    path_arr = path.split(os.sep)
    path2 = ''
    for i in xrange(len(path_arr)):
        path2 = os.path.join(path2, path_arr[i])
        if path_arr[i] == folder:
            break
    return path2


def git(path, id):
    try:
        os.chdir(getPathToFolder('misterfantastic'))
        if not (os.path.exists('Repos')):
            os.mkdir('Repos')
        os.chdir('Repos')
        repo_dir = 'Repo' + id
        if os.path.exists(repo_dir):
            os.chdir(os.path.join(os.curdir, repo_dir))
            pr = subprocess.Popen(['git', 'pull'],
                                  cwd=os.path.abspath(os.curdir),
                                  stdin=subprocess.PIPE,
                                  stdout=subprocess.PIPE,
            )
            out, error = pr.communicate()
        else:
            os.mkdir(repo_dir)
            os.chdir(os.path.join(os.curdir, repo_dir))
            pr = subprocess.Popen(["git", 'clone', str(path)],
                                  cwd=os.path.abspath(os.curdir),
                                  stdin=subprocess.PIPE,
                                  stdout=subprocess.PIPE,
            )
            out, error = pr.communicate()
    except Exception as detail:
        f = open("errors.txt", 'wb')
        f.write(detail)
        f.close()


def repoParse(id):
    try:
        os.chdir(getPathToFolder('misterfantastic'))
        if os.path.exists('Repos'):
            os.chdir('Repos')
            repo_dir = 'Repo' + id
            if os.path.exists(repo_dir):
                pass
            else:
                return {"response": "error can not find repo"}
        else:
            return {"response": "error"}
    except Exception as detail:
        f = open('errors.txt', 'wb')
        f.write(detail)
        f.close()