from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField
from wtforms.validators import Required, DataRequired


class UpdateProfile(FlaskForm):
   bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
   submit = SubmitField('submit')

class PostForm(FlaskForm):
   pitch = SelectField('pitch',choices=[('pickup lines','pickup lines'),('interview pitch','interview pitch'),('product pitch','product pitch')])
   title = StringField('Post title',validators=[DataRequired()])
   post = TextAreaField('Write your post',validators=[DataRequired()])
   submit = SubmitField('submit')

class CommentForm(FlaskForm):
   comment = TextAreaField('Write your comment',validators=[DataRequired()])
   submit = SubmitField('submit')