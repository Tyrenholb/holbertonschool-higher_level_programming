#!/usr/bin/python3
"""Defines the City class inheriting from Base."""

from sqlalchemy import Column, ForeignKey, Integer, String
from model_state import Base


class City(Base):
    """Represents a city in the cities table."""
    __tablename__ = 'cities'

    """PK for table"""
    id = Column(Integer, primary_key=True, nullable=False)

    name = Column(String(128), nullable=False)

    """FK to the table "State" """
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
