from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin)
from rest_framework.viewsets import GenericViewSet


class ModelMixinSet(
    CreateModelMixin, ListModelMixin, DestroyModelMixin, GenericViewSet
):
    pass


class CreateViewSet(CreateModelMixin, GenericViewSet):
    pass
