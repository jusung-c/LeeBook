from django.contrib.auth.forms import UserCreationForm


class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # username 못바꾸도록 잠구기
        self.fields['username'].disabled = True