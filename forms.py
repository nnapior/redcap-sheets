from wtforms import Form, PasswordField, validators


class SettingsForm(Form):
    redcap_api_key = PasswordField('REDcap API Key', [
        validators.DataRequired(),
        validators.Length(min=32, max=32)
    ])
