from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Enum, DateTime, Text, ForeignKey
import enum
from datetime import datetime

class Base(DeclarativeBase):
    pass

class Region(Base):
    __tablename__ = "region"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(200))
    comunas: Mapped[list["Comuna"]] = relationship(back_populates="region")

class Comuna(Base):
    __tablename__ = "comuna"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(200))
    region_id: Mapped[int] = mapped_column(ForeignKey("region.id"))
    region: Mapped["Region"] = relationship(back_populates="comunas")
    avisos: Mapped[list["AvisoAdopcion"]] = relationship(back_populates="comuna")

class AvisoAdopcion(Base):
    __tablename__ = "aviso_adopcion"
    id: Mapped[int] = mapped_column(primary_key=True)
    fecha_ingreso: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    comuna_id: Mapped[int] = mapped_column(ForeignKey("comuna.id"))
    sector: Mapped[str] = mapped_column(String(100))
    nombre: Mapped[str] = mapped_column(String(200))
    email: Mapped[str] = mapped_column(String(100))
    celular: Mapped[str] = mapped_column(String(15))
    tipo: Mapped[str] = mapped_column(Enum("gato", "perro"))
    cantidad: Mapped[int] = mapped_column(Integer)
    edad: Mapped[int] = mapped_column(Integer)
    unidad_medida: Mapped[str] = mapped_column(Enum("a", "m"))
    fecha_entrega: Mapped[datetime] = mapped_column(DateTime)
    descripcion: Mapped[str] = mapped_column(Text)
    comuna: Mapped["Comuna"] = relationship("Comuna", back_populates="avisos")
    fotos: Mapped[list["Foto"]] = relationship("Foto", back_populates="aviso")
    contactar_por: Mapped[list["ContactarPor"]] = relationship("ContactarPor", back_populates="aviso")
    comentarios: Mapped[list["Comentario"]] = relationship("Comentario", back_populates="aviso")


class Foto(Base):
    __tablename__ = "foto"
    id: Mapped[int] = mapped_column(primary_key=True)
    ruta_archivo: Mapped[str] = mapped_column(String(300))
    nombre_archivo: Mapped[str] = mapped_column(String(300))
    actividad_id: Mapped[int] = mapped_column(ForeignKey("aviso_adopcion.id"))
    aviso: Mapped["AvisoAdopcion"] = relationship("AvisoAdopcion", back_populates="fotos")


class ContactarPor(Base):
    __tablename__ = "contactar_por"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(Enum('whatsapp', 'telegram', 'X', 'instagram', 'tiktok', 'otra'))
    identificador: Mapped[str] = mapped_column(String(150))
    actividad_id: Mapped[int] = mapped_column(ForeignKey("aviso_adopcion.id"))
    aviso: Mapped["AvisoAdopcion"] = relationship("AvisoAdopcion", back_populates="contactar_por")

class Comentario(Base):
    __tablename__ = "comentario"
    id: Mapped[int] = mapped_column(primary_key=True)
    aviso_id: Mapped[int] = mapped_column(ForeignKey("aviso_adopcion.id"), nullable=False)
    nombre: Mapped[str] = mapped_column(String(80), nullable=False)
    texto: Mapped[str] = mapped_column(String(300), nullable=False)
    fecha: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    aviso: Mapped["AvisoAdopcion"] = relationship("AvisoAdopcion", back_populates="comentarios")


