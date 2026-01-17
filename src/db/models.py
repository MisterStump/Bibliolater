from sqlalchemy.orm import DeclarativeBase, Mapped, MappedColumn
from datetime import datetime

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "auth_users"
    id: Mapped[int] = MappedColumn(primary_key=True, autoincrement=True)
    username: Mapped[str] = MappedColumn(unique=True, nullable=False)
    email: Mapped[str] = MappedColumn(unique=True, nullable=False)
    hased_password: Mapped[str] = MappedColumn(nullable=False)
    created_at: Mapped[datetime] = MappedColumn(nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"