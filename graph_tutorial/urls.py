# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

# <UrlConfSnippet>
from django.contrib import admin
from django.urls import include, path

from tutorial import views

urlpatterns = [
    path("", include("tutorial.urls")),
    path("admin/", admin.site.urls),
]
# </UrlConfSnippet>
