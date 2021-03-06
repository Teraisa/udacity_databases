from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ArticlesForm(FlaskForm):
    title = StringField(
        'Article Title',
        validators=[DataRequired("Please enter a valid title.")]
    )
    slug = StringField(
        'Article Slug',
        validators=[DataRequired("Please enter an article slug.")]
    )
    lead = StringField(
        'Lead',
        validators=[DataRequired("Please Enter the lead field.")]
    )
    body = StringField(
        'Body',
        validators=[
            DataRequired("Please enter what you want this article to say.")
        ]
    )
    submit = SubmitField('Add Article')


class AuthorsForm(FlaskForm):
    name = StringField(
        'Name',
        validators=[DataRequired("Please enter the Author's name.")]
    )
    bio = StringField(
        'Bio',
        validators=[DataRequired("Please enter a Bio for the Author.")]
    )
    submit = SubmitField('Add Author')
