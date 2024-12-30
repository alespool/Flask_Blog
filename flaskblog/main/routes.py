from flask import render_template, request, Blueprint, jsonify
from flaskblog.models import Post, Event

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    """
    The home route shows all posts in the database ordered by the
    Post.date_posted in descending order (newest posts first). The
    posts are paginated in groups of 3. The page number is passed as
    a query argument, and defaults to 1.
    """
    page  = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template('home.html', posts=posts)

@main.route("/about")
def about():
    """
    The about route renders the about.html template with the title 'About'.
    """
    return render_template('about.html', title='About')

@main.route("/announcements")
# TODO: Make this function for admins only
def announcements():
    """
    The announcement route renders the announcements.html template with the title 'Announcements'.
    """
    announcement_posts = Post.query.filter_by(is_announcement=True).order_by(Post.date_posted.desc()).all()
    return render_template('announcements.html', recent_posts=announcement_posts)

@main.route('/calendar')
def calendar():
    return render_template('calendar.html')

@main.route('/get-events')
def get_events():
    # Query the Event table
    events = Event.query.all()

    # Format events for FullCalendar
    events_data = [
        {
            "id": event.id,
            "title": event.title,
            "start": event.start.isoformat(),
            "end": event.end.isoformat() if event.end else None,
        }
        for event in events
    ]

    return jsonify(events_data)

