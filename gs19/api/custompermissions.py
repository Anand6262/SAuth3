#This file is MYPERMISSION to the API to perform only the below CRUD operation
from rest_framework.permissions import BasePermission

class MyPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return False