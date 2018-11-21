from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
   return User.query.get(int(user_id))


class User(UserMixin, db.Model):
   __tablename__ = 'users'

   id = db.Column(db.Integer,primary_key = True)
   username = db.Column(db.String(255),unique = True)
   email = db.Column(db.String(255),unique = True,index = True)
   bio = db.Column(db.String(255))
   profile_pic_path = db.Column(db.String())
   pass_secure = db.Column(db.String(255))
   post = db.relationship('Post',backref = 'user',lazy = 'dynamic')
   comments = db.relationship('Comment',backref = 'user',lazy = 'noload')

   @property
   def password(self):
       raise AttributeError('You cannot read the password attribute')

   @password.setter
   def password(self, password):
       self.pass_secure = generate_password_hash(password)

   def verify_password(self,password):
       return check_password_hash(self.pass_secure,password)

   def __repr__(self):
       return f' User {self.username}'


class Post(db.Model):
   __tablename__ = 'posts'

   id = db.Column(db.Integer,primary_key = True)
   post_category = db.Column(db.String)
   post_title = db.Column(db.String)
   post_text = db.Column(db.String)
   post_time = db.Column(db.DateTime, default = datetime.utcnow)
   post_votes = db.Column(db.Integer)
   user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
   comments = db.relationship('Comment',backref = 'post',lazy = 'dynamic')

   def save_post(self):
       db.session.add(self)
       db.session.commit()

   @classmethod
   def get_posts(cls,category):
       posts = Post.query.filter_by(post_category = category).order_by(Post.post_time.desc()).all()
       return posts

   @classmethod
   def get_user_posts(cls,user):
       posts = Post.query.\
           filter_by(user_id = user).\
           order_by(Post.post_time).all()
       return posts


class Comment(db.Model):
   __tablename__ = 'comments'

   id = db.Column(db.Integer,primary_key = True)
   comment_text = db.Column(db.String)
   comment_time = db.Column(db.DateTime, default = datetime.utcnow)
   post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
   user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

   def save_comment(self):
       db.session.add(self)
       db.session.commit()

   @classmethod
   def get_comments(cls,id):
       comments = Comment.query.filter_by(post_id = id).all()
       return  comments