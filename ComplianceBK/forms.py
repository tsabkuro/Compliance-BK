import phonenumbers
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, TextAreaField)
from wtforms.validators import DataRequired, Length, Email, ValidationError


class ContactForm(FlaskForm):
    name    = StringField ('Name', validators=[DataRequired(), Length(min=1, max=30)])
    email   = StringField('Email', validators=[DataRequired(), Email()])
    phone   = StringField('Phone', validators=[DataRequired()])
    message = TextAreaField('Questions/Comments', validators=[Length(max=500)])
    submit  = SubmitField('Submit')

    def validate_phone(form, field):
        for i in field.data:
            if not i.isnumeric() or i == '-' or i ==' ':
                raise ValidationError('Invalid phone number.')
        try:
            input_number = phonenumbers.parse(field.data)
            if not (phonenumbers.is_valid_number(input_number)):
                raise ValidationError('Invalid phone number.')
        except:
            input_number = phonenumbers.parse("+1"+field.data)
            if not (phonenumbers.is_valid_number(input_number)):
                raise ValidationError('Invalid phone number.')