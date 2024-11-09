class Theme(Base):
  tablename = "theme_table"
  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str]
  description: Mapped[str]
  light: Mapped[dict] = mapped_column(JSON)
  dark: Mapped[dict] = mapped_column(JSON)
  price: Mapped[float] = mapped_column(nullable=True, default=0)
  key:Mapped[str]

  users: Mapped[list["User"]] = relationship(
        back_populates="themes",  
        uselist=True,
        secondary="theme_user_table"  
    )
  
class ThemeUser(Base):
    
    tablename = "theme_user_table"

    user_id:Mapped[int] = mapped_column(ForeignKey("user_table.id"), primary_key=True)
    theme_id:Mapped[int] = mapped_column(ForeignKey("theme_table.id"), primary_key=True)
    

class User(Base):
    
    tablename = "user_table"

    id:Mapped[int] = mapped_column(primary_key=True)    
    user_tg:Mapped[list["UserTg"]] = relationship(uselist=True, back_populates="user")

    # служебная инфа
    role:Mapped[Role] = mapped_column(default=Role.user)
    password:Mapped[bytes]
    created_at:Mapped[created_at]
    
    # running
    running_points:Mapped[int] = mapped_column(default=0)

    # user инфа
    email:Mapped[str] = mapped_column(unique=True)
    name:Mapped[str]
    surname:Mapped[str]
    dob:Mapped[datetime.date]
    balance: Mapped[int] = mapped_column(default=0)
    
    
    # analytics data 
    words_per_minute:Mapped[str] = mapped_column(default=json.dumps([120]))
    themes: Mapped[list["Theme"]] = relationship(
        back_populates="users",
        uselist=True,
        secondary="theme_user_table"
    )