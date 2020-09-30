from rest_framework.routers import Route, DynamicRoute, SimpleRouter
from rest_framework.routers import DefaultRouter


class CustomRouter(DefaultRouter):
    """
    A router for read-only APIs, which doesn't use trailing slashes.
    """
    routes = [
        Route(
            url=r'^{prefix}{trailing_slash}$',
            mapping= {'get': 'list', 'post': 'create'},
            name='{basename}-list_create',
            # trailing_slash = '/',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        Route(
            url=r'^{prefix}/{lookup}{trailing_slash}$',
            mapping={'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'},
            name='{basename}-detail_update_destroy',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        ),
        # Route(
        #     url=r'^{prefix}/{lookup}/{url_path}$',
        #     mapping= {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update'},
        #     name='{basename}-url_name',
        #     detail=True,
        #     initkwargs={}
        # )
    ]