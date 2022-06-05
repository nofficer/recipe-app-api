"""
Views from the recipe APIs.
"""

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Recipe
from recipe import serializers

class RecipeViewSet(viewsets.ModelViewSet):
    """View from manage recipe APIs."""
    #Define the serializing being used
    serializer_class = serializers.RecipeSerializer
    #Because this is a ModelViewSet we use a model to populate the queryset of objects which will be available
    queryset = Recipe.objects.all()
    #Define whether these APIs require authentication
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    #Override the get_queryset method so that we only return recipes attached to the authenticated user
    def get_queryset(self):
        """Retrieve recipes for authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-id')