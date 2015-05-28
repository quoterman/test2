Mister Fantastic
=======================

Module 1 (Mister Fantastic)

Цель модуля - отслеживать время жизни строк кода. Результат анализа представить в виде различных графиков и отчетов.

Интересующие показатели - когда и кем строка кода была создана, когда заменена/удалена, какой разработчик пишет самый "долгоживущий" код.

Отчеты в разрезе команды и отдельно взятого разработчика.

Url : http://misterfantastic-misterfantastic.rhcloud.com


Django project directory structure
----------------------------------

     djangoproj/
        .gitignore
     	.openshift/
     		README.md
     		action_hooks/  (Scripts for deploy the application)
     			build
     			post_deploy
     			pre_build
     			deploy
     			secure_db.py
     		cron/
     		markers/
     	setup.py   (Setup file with de dependencies and required libs)
     	README.md
     	libs/   (Adicional libraries)
     	data/	(For not-externally exposed wsgi code)
     	wsgi/	(Externally exposed wsgi goes)
     		application (Script to execute the application on wsgi)
     		openshift/	(Django project directory)
     			__init__.py
     			manage.py
     			openshiftlibs.py
     			settings.py
     			urls.py
     			views.py
     			wsgi.py
     			templates/
     				home/
     					home.html (Default home page)
     		static/	(Public static content gets served here)
     			README


