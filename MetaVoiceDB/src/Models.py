from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User_Profile(Base):
    __tablename__ = 'User_Profiles'

    # Maps Userprofile class to User class
    User = relationship("User", back_populates="User_Profile")

    UserId = Column(Integer, ForeignKey('Users.Id'), primary_key=True )
    Fname = Column(String(20))
    Lname = Column(String(20))
    Company = Column(String(40))
    Address = Column(String(40))
    Premise = Column(String(20))
    Country = Column(String(40))
    City = Column(String(40))
    State = Column(String(20))
    Zipcode = Column(Integer)
    Cell = Column(String(15))

    def __init__(self, UserId=None,Fname=None,Lname=None,Company=None,Address=None, Premise=None,
                Country=None,City=None,State=None,Zipcode=None,Cell=None):
        self.UserId = UserId
        self.Fname = Fname
        self.Lname = Lname
        self.Company = Company
        self.Address = Address
        self.Premise = Premise
        self.Country = Country
        self.City = City
        self.State = State
        self.Zipcode = Zipcode
        self.Cell = Cell
        return

class User(Base):
    __tablename__ = 'Users'

    Id = Column( Integer , primary_key = True)
    Email = Column(String(60))
    Password = Column(String(20))
    IsAdmin = Column(Boolean)

    # Maps Userprofile class to User class
    User_Profile = relationship('User_Profile', uselist = False,
                                order_by=User_Profile.UserId,back_populates="User")

    def __init__(self, Id=None, Email=None, Password=None, IsAdmin=None,User_Profile=None):
        self.Id = Id
        self.Email = Email
        self.Password = Password
        self.IsAdmin = IsAdmin
        self.User_Profile = User_Profile
        return

    def __str__(self):
        return "User(%r, %r, %r)" % (self.Id, self.Username, self.Password)

class Skills(Base):
    __tablename__ = 'Skills'

    SkillId = Column(Integer, primary_key=True)
    UserId = Column(Integer)
    AMZ_SkillId = Column(String(60))
    Status = Column(String(20))
    Category = Column(Integer)      #Make this a string(20)?
    ShortDesc = Column(String(60))
    LongDesc = Column(String(200))
    Keywords = Column(String(200))
    TemplateId = Column(Integer)

    def __init__(self, SkillId=None, UserId=None, AMZ_SkillId=None, Status=None,
                Category=None,ShortDesc=None,LongDesc=None,Keywords=None,TemplateId=None):
        self.SkillId = SkillId
        self.UserId = UserId
        self.AMZ_SkillId = AMZ_SkillId
        self.Status = Status
        self.Category = Category
        self.ShortDesc = ShortDesc
        self.LongDesc = LongDesc
        self.Keywords = Keywords
        self.TemplateId = TemplateId        
        return

class Utterances(Base):
    __tablename__ = 'Utterances'

    UtterId = Column(Integer, primary_key=True)
    SkillId = Column(Integer)
    Utter = Column(String(100))

    def __init(self,UtterId=None,SkillId=None,Utter=None):
        self.UtterId = UtterId
        self.SkillId = SkillId
        self.Utter = Utter
        return

class Response(Base):
    __tablename__ = 'Responses'

    RespId = Column(Integer, primary_key=True)
    SkillId = Column(Integer)
    Resp = Column(String(100))

    def __init__(self,RespId=None,SkillId=None,Resp=None):
        self.RespId = RespId
        self.SkillId = SkillId
        self.Resp = Resp
        return

class Template(Base):
    __tablename__ = 'Templates'

    TemplateId = Column(Integer, primary_key=True)
    Name = Column(String(20))
    
    def __init__(self, TemplateId=None, Name=None):
        self.TemplateId = TemplateId
        self.Name = Name
        return