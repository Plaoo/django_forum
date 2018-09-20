from django.contrib.auth.mixins import UserPassesTestMixin

class StaffMixing(UserPassesTestMixin):
    """Only staff member can create new section"""

    def test_func(self):
            return self.request.user.is_staff
