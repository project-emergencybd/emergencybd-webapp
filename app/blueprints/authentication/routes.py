from flask import Blueprint, render_template, request
from app.models import Volunteer
from werkzeug.security import generate_password_hash
import pyotp
from app import database

authentication = Blueprint(
    name="authentication",
    import_name=__name__,
    template_folder="templates",
    static_folder="static",
)


@authentication.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # get the form values
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        verifier = request.form["verifier"]  # possible values: NID, brn
        verification_number = (
            request.form["NID"] if verifier == "NID" else request.form["BRN"]
        )  # get verification number from the form data,
        # if verifier is NID,
        # then verification number would be the NID number,
        # otherwise it will be the Birth Registration Number
        gender = request.form["gender"]
        blood_group = request.form["bloodGroup"]
        area = request.form["area"]
        password = request.form["password"]

        # print("name:", name)
        # print("email:", email)
        # print("phone:", phone)
        # print("verifier:", verifier)
        # print("verification num:", verification_number)
        # print("gender:", gender)
        # print("blood group:", blood_group)
        # print("area:", area)
        # print("password:", password)

        new_volunteer = Volunteer(
            name=name,
            gender=gender,
            email=email,
            phone=phone,
            area=area,
            blood_group=blood_group,
            verifier=verifier,
            verification_number=verification_number,
            password=generate_password_hash(password=password),
            recovery_key=pyotp.random_base32(),
            deleted=False,
        )

        # print("Volunteer:", new_volunteer)

        database.session.add(new_volunteer)
        database.session.commit()

    return render_template("register.html")


@authentication.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")
