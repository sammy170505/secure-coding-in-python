from rest_framework import status

from rest_framework.test import APIClient

import pytest

from ..models import Post, Profile
from .test_utils import author, non_author


@pytest.mark.django_db
def test_author_permissions(client, author, non_author):
    """should only allow authors to read posts"""
    client.force_login(non_author)
    blocked_response = client.get("/posts/")

    client.force_login(author)
    permitted_response = client.get("/posts/")

    assert blocked_response.status_code == status.HTTP_403_FORBIDDEN
    assert (
        blocked_response.json()["detail"]
        == "You do not have permission to perform this action."
    )

    assert permitted_response.status_code == status.HTTP_200_OK
    assert len(permitted_response.json()) == 1
