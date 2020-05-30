from rest_framework import mixins
from rest_framework import viewsets


class CreateListRetrieveViewset(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    pass


class CreateViewset(
    mixins.CreateModelMixin, viewsets.GenericViewSet,
):
    pass


class ListRetrieveViewset(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet,
):
    pass


class RetrieveViewset(
    mixins.RetrieveModelMixin, viewsets.GenericViewSet,
):
    pass


class ListViewset(
    mixins.ListModelMixin, viewsets.GenericViewSet,
):
    pass


class UpdateViewset(
    mixins.UpdateModelMixin, viewsets.GenericViewSet,
):
    pass


class CreateListRetrieveUpdateViewset(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    pass
