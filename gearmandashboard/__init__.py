from pyramid.config import Configurator
import akhet


from pyramid.url import static_url
from pyramid.threadlocal import get_current_request


def static_url_filter(path, **kw):
    request = get_current_request()
    return static_url(path, request, **kw)


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    # Create the Pyramid Configurator.
    config = Configurator(settings=settings)
    config.include("pyramid_handlers")
    config.include("akhet")
    config.include("pyramid_jinja2")
    
    
    # Configure renderers and event subscribers
    config.add_subscriber("gearmandashboard.subscribers.create_url_generator",
        "pyramid.events.ContextFound")
    config.add_subscriber("gearmandashboard.subscribers.add_renderer_globals",
                          "pyramid.events.BeforeRender")

    # Set up view handlers
    config.add_handler("home", "/", "gearmandashboard.handlers:Main",
                       action="index")
    config.add_handler("main", "/{action}", "gearmandashboard.handlers:Main",
        path_info=r"/(?!favicon\.ico|robots\.txt|w3c)")


    # Set up other routes and views
    # ** If you have non-handler views, create create a ``gearmandashboard.views``
    # ** module for them and uncomment the next line.
    #
    #config.scan("gearmandashboard.views")

    # Mount a static view overlay onto "/". This will serve, e.g.:
    # ** "/robots.txt" from "gearmandashboard/static/robots.txt" and
    # ** "/images/logo.png" from "gearmandashboard/static/images/logo.png".
    #
    #config.add_static_route("gearmandashboard", "static", cache_max_age=3600)

    # Mount a static subdirectory onto a URL path segment.
    # ** This not necessary when using add_static_route above, but it's the
    # ** standard Pyramid way to serve static files under a URL prefix (but
    # ** not top-level URLs such as "/robots.txt"). It can also serve files from
    # ** third-party packages, or point to an external HTTP server (a static
    # ** media server).
    # ** The first commented example serves URLs under "/static" from the
    # ** "gearmandashboard/static" directory. The second serves URLs under 
    # ** "/deform" from the third-party ``deform`` distribution.
    #
    config.add_static_view("static", "gearmandashboard:static")

    return config.make_wsgi_app()
