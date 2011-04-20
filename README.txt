Gearman Dashboard
=================

Gearman Dashboard gives you an overview of the status of your Gearman
(http://www.gearman.org/) servers. It uses the status command in the
protocol to fetch information from each server.

The current version is based on Pyramid
(http://pylonsproject.org/projects/pyramid/about) and the Python
Gearman (http://github.com/Yelp/python-gearman) client. It is still a
bit of a quick hack and the list of servers is hard-coded in
gearmandashboard/models.py, but this will be fixed soon.

The design is copied from Resque
(http://github.com/defunkt/resque). License and copyright message for
those files are included directly in the files
(gearmandashboard/static/stylesheets/style.css and
gearmandashboard/static/stylesheetsreset.css).


License
=======
Copyright (C) 2010, 2011 Oskar Skoog (oskar@osd.se). Gearman Dashboard
is provided under the MIT License. See the included LICENSE.txt file
for specifics.


Source code
===========
The source code is located on Github at:
http://github.com/osks/gearman-dashboard
