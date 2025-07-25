import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_user_can_create_and_list_engineers():
    client = APIClient()

    # 🔐 Create and authenticate a user
    user = User.objects.create_user(username="testuser", password="testpass123")
    client.force_authenticate(user=user)

    # ✅ Step 1: Create Engineer
    create_response = client.post("/api/engineers/", {
        "name": "E2E Tester",
        "email": "tester@e2e.com",
        "specialty": "All-Rounder"
    }, format='json')

    assert create_response.status_code in [200, 201]

    # ✅ Step 2: List Engineers
    list_response = client.get("/api/engineers/")
    assert list_response.status_code == 200
    assert any(e["email"] == "tester@e2e.com" for e in list_response.json())
