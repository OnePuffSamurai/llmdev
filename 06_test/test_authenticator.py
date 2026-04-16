from authenticator import Authenticator
import pytest

@pytest.fixture
def authenticator():
    auth = Authenticator()
    yield auth

# ユーザー登録のテスト
def test_register(authenticator):
    authenticator.register("user1", "password1")
    assert authenticator.users["user1"] == "password1"
    with pytest.raises(ValueError, match="ユーザーは既に存在します。"):
        authenticator.register("user1", "password2")

# ユーザーログインのテスト
def test_login(authenticator):
    authenticator.register("user1", "password1")
    assert authenticator.login("user1", "password1") == "ログイン成功"
    with pytest.raises(ValueError, match="ユーザー名またはパスワードが正しくありません。"):
        authenticator.login("user1", "wrongpassword")