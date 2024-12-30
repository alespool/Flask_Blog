from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired
from flask_pagedown.fields import PageDownField


class PostForm(FlaskForm):
    """A class to construct the Post Forms that the users will fill out in the website"""
    title = StringField('Title', validators=[DataRequired()])
    content = PageDownField('Content', validators=[DataRequired()])
    is_announcement = BooleanField('Mark as Announcement')
    is_event = BooleanField('Mark as Event')
    submit = SubmitField('Post')
    
