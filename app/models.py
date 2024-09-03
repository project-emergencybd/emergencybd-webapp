from app import database
from flask_login import UserMixin
from sqlalchemy import Integer, Column, ForeignKey, String
from sqlalchemy.orm import mapped_column, Mapped, relationship
import app.constants as const


class Volunteer(database.Model, UserMixin):
    __tablename__ = "Volunteers"

    uid: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)  # Column(Unicode, nullable=False)
    gender: Mapped[str] = mapped_column(nullable=False)

    # contact information
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    phone: Mapped[int] = mapped_column(nullable=False, unique=True)

    # filter_by
    area: Mapped[str] = mapped_column(nullable=False)
    blood_group: Mapped[str] = mapped_column(nullable=False)

    # verifier
    verifier: Mapped[str] = mapped_column(nullable=False)
    verification_number: Mapped[int] = mapped_column(nullable=False, unique=True)

    # by_backend
    password: Mapped[str] = mapped_column(nullable=False)
    recovery_key: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[str] = mapped_column(default=const.dhaka_current_time())
    # relational values
    problem_id: Mapped[int] = mapped_column(ForeignKey("Problems.pid"), nullable=True)
    team_id: Mapped[int] = mapped_column(ForeignKey("Teams.tid"), nullable=True)
    deleted: Mapped[bool] = mapped_column(nullable=False)


class Problem(database.Model):
    __tablename__ = "Problems"

    pid: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    # generic fields:
    title: Mapped[str] = mapped_column(nullable=False)
    details: Mapped[str] = mapped_column(nullable=False)
    location: Mapped[str] = mapped_column(nullable=False)

    # identifier
    associated_phone_number: Mapped[str] = mapped_column(nullable=False)
    associated_pin: Mapped[str] = mapped_column(nullable=False)

    status: Mapped[str]  # 3 possible values : 'invalid', 'resolved', null

    associated_volunteers = relationship("Volunteer", backref="problem")


class Team(database.Model):
    __tablename__ = "Teams"

    tid: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    team_name: Mapped[str] = mapped_column(nullable=False, unique=True)
    team_leader_id: Mapped[int]
    team_sub_leader_id: Mapped[int]

    plans = relationship("TeamPlan")
    members = relationship("Volunteer", backref="team")


class TeamPlan(database.Model):
    __tablename__ = "Team_plans"

    tpid: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    start_date: Mapped[str]
    end_date: Mapped[str]

    team_id: Mapped[int] = mapped_column(ForeignKey("Teams.tid"))
    activities = relationship("Activity", backref="plans")


class Activity(database.Model):
    __tablename__ = "Activities"

    aid: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    date: Mapped[str]
    details: Mapped[str]

    plan_id: Mapped[int] = mapped_column(ForeignKey("Team_plans.tpid"))
