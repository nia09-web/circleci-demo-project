from user_manager import UserManager

def test_add_user():
    um = UserManager()
    assert um.add_user("alice") == True
    assert um.add_user("alice") == False

def test_user_exists():
    um = UserManager()
    um.add_user("bob")
    assert um.user_exists("bob") == True
    assert um.user_exists("charlie") == False

def test_get_all_users():
    um = UserManager()
    um.add_user("alice")
    um.add_user("bob")
    assert um.get_all_users() == ["alice", "bob"]
