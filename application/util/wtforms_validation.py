from wtforms.validators import ValidationError


class UniqueField(object):
    def __init__(self, model, message='Value already used.'):
        self.model = model
        self.message = message

    def __call__(self, form, field):
        obj = self.model.query.filter(getattr(self.model, field.id) == field.data).first()
        if obj:
            raise ValidationError(self.message)
