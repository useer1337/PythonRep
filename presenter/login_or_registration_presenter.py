from view.login_or_registration_view import LoginOrPasswordView


class LoginOrRegistrationPresenter:
    def __init__(self, view:LoginOrPasswordView, ):
        self.view = view
        self.service = service()
