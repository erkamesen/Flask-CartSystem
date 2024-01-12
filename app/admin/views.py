from flask_admin import AdminIndexView, expose
from flask_login import current_user
from app.models import User, Course

class MyAdminIndexView(AdminIndexView):
  @expose("/")
  def index(self):

    users = User.query.count()
    courses = Course.query.count()
    context = {
        "user_count" : users,
        "course_count": courses
    }
    return self.render("admin/admin.html", **context)