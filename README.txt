Gearman Dashboard
=================

Gearman Dashboard gives you an overview of the status of your Gearman
(http://www.gearman.org/) servers. It uses the status command in the
protocol to fetch information from each server.

This is a quick hack that I made because I wanted to experiment with
web.py and python-gearman. The the list of Gearman servers are hard
coded in gearmanweb.py.

The design is copied from Resque
(https://github.com/defunkt/resque). License and copyright message for
those files are included directly in the files (static/style.css and
static/reset.css).


Requirements
============
The following Python modules are required:

* web.py (http://webpy.org/).
* python-gearman (https://github.com/Yelp/python-gearman)


License
=======
Copyright (C) 2010, 2011 Oskar Skoog (oskar@osd.se). Gearman Dashboard
is provided under the MIT License. See the included LICENSE file for
specifics.


Source code
===========
The source code is located on Github at:
https://github.com/osks/gearman-dashboard
