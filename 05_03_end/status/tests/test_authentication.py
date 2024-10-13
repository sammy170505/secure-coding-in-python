import os
import tempfile

import pytest

from app import app, Author, db, init_db


@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    db.session.query(Author).delete()
    db.session.commit()

    with app.test_client() as client:
        with app.app_context():
            init_db()
        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])


def test_register(client):
    valid_response = client.post(
        '/register', json=dict(handle='foo', email='foz@example.com', password='passs')
    )
    invalide_response = client.post(
        '/register', json=dict(handle='foo', email='fozexample.com', password='passs')
    )
    assert invalide_response.status_code == 409
    assert invalide_response.json == {'email': ['Not a valid email address.']}
    assert valid_response.status_code == 201
    assert valid_response.json['message'] == 'registration successful'
