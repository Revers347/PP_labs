from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
import os

DB_SCHEME = 'mysql'
DB_USERNAME = 'root'
DB_PASSWORD = '1235'
DB_SERVER = 'localhost'
DB_PORT = '3306'
DB_NAME = 'blog'

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
connection_string = '{}://{}:{}@{}:{}/{}'.format(
    DB_SCHEME,
    DB_USERNAME,
    DB_PASSWORD,
    DB_SERVER,
    DB_PORT,
    DB_NAME
)

engine = create_engine(connection_string, echo=True)
Base = declarative_base()

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer(), autoincrement=True, primary_key=True, unique=True)
    name = Column(String(50), nullable=False)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer(), autoincrement=True, primary_key=True, unique=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    firstName = Column(String(50))
    lastName = Column(String(50))
    email = Column(String(80), unique=True)
    phone = Column(String(20))
    userRole = Column(String(10))


tag_blog = Table('tag_blog',
                 Base.metadata,
                 Column('tag_id', Integer(), ForeignKey('tag.id')),
                 Column('blog_id', Integer(), ForeignKey('blog.id'))
                 )


class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer(), autoincrement=True, primary_key=True, unique=True)
    name = Column(String(50), nullable=False)
    blogs = relationship("Blog", secondary=tag_blog, lazy='dynamic')


class Blog(Base):
    __tablename__ = 'blog'
    id = Column(Integer(), autoincrement=True, primary_key=True, unique=True)
    author = Column(String(50), ForeignKey('user.username'))
    category_id = Column(Integer(), ForeignKey('category.id'))
    title = Column(String(150), nullable=False)
    contents = Column(String(2000), nullable=False)
    auth = relationship("User")
    category = relationship("Category")
    editedBlog = relationship("EditedBlog")
    tags = Column(String(150))


class EditedBlog(Base):
    __tablename__ = 'edited_blog'
    id = Column(Integer(), autoincrement=True, primary_key=True, unique=True)
    title = Column(String(150))
    contents = Column(String(2000))
    originalBlog_id = Column(Integer(), ForeignKey('blog.id'))
    originalBlog = relationship("Blog", uselist=False)
