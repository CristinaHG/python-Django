# -*- coding=utf-8 -*-

from rest_framework.permissions import BasePermission

import users.api


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Define si el usuario autenticado en request.user tiene permiso
        para realizar la acción(GET,POST,PUT o DELETE)
        :param request:
        :param view:
        :return:
        """

        # si quiere crear un usuario, sea quien sea puede
        if request.method=="POST":
            return True
        # si no es POST, el superusuario siempre puede
        elif request.user.is_superuser:
            return True
        # si es un GET a la vista de detalle, tomo la decisión en has_object_permission
        elif isinstance(view, users.api.UserDetailAPI):
            True
        else:
            # GET a /api/1.0/users/
            False


    def has_object_permission(self, request, view, obj):
        """
        Si el usuario autenticado en request.user tiene permiso para
        realizar acción (GET,PUT o DELETE) sobre el objeto obj
        :param request:
        :param view:
        :param obj:
        :return:
        """
        return request.user.is_superuser or request.user==obj