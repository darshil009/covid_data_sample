from app import app
from app import login_manager
from app.model import user

#Hello 
@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))
