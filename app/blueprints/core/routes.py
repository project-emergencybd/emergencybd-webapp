from flask import Blueprint, render_template

core = Blueprint(
    name="core",
    import_name=__name__,
    template_folder="templates",
    static_folder="static",
)


@core.route("/")
def index():
    return render_template("index.html")
