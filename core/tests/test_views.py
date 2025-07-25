import pytest
from django.urls import reverse
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_homepage_accessible(client):
    # Create a test user
    user = User.objects.create_user(username='testuser', password='testpass123')

    # Log in the user
    client.login(username='testuser', password='testpass123')

    # Access the dashboard
    url = reverse('dashboard')
    response = client.get(url)
    assert response.status_code == 200
