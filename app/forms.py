from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class PropertyForm(FlaskForm):
    title           = TextAreaField('Property Title', validators=[DataRequired()])
    no_of_rooms     = TextAreaField('No. of Bedrooms', validators=[DataRequired()])
    no_of_bathrooms = TextAreaField('No. of Bathrooms', validators=[DataRequired()])
    location        = TextAreaField('Location', validators=[DataRequired()])
    price           = TextAreaField('Price', validators=[DataRequired()])
    prop_type       = SelectField('Property Type',
                                  choices=[('House', 'House'), ('Apartment', 'Apartment')],
                                  validators=[DataRequired()])
    description     = TextAreaField('Description', validators=[DataRequired()])
    photo           = FileField('Photo', validators=[
                          FileRequired(),
                          FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images only!')
                      ])