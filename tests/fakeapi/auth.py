def fake_basic_auth(username, password, context, required_scopes=None):
    if username == password:
        return {'uid': username}
    return None
