from flask import (render_template, url_for, flash,
                   redirect, request, jsonify, Blueprint)
from flaskblog import db
from flaskblog.models import Post, Event
from datetime import timedelta, datetime

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

@main.route("/get-events")
def get_events():
    events = Post.query.filter_by(is_event=True).all()
    events_data = []
    
    for event in events:
        event_data = {
            'title': event.title,
            'start': event.date_posted.isoformat(), 
            'end': (event.date_posted + timedelta(hours=1)).isoformat(), 
        }
        events_data.append(event_data)
    
    return jsonify(events_data)

@main.route("/create-recurring-events", methods=['POST'])
def create_recurring_events():
    start_time = datetime(2025, 1, 1, 7, 0)  # Start time for the recurring event (e.g., 7 AM)
    for i in range(30):  # Create events for 30 days
        event_time = start_time + timedelta(days=i)
        event = Post(
            title="Daily Study Session",
            content="Time for Bot AI Programming!",
            date_posted=event_time,
            is_event=True
        )
        db.session.add(event)
    
    db.session.commit()
    flash('Recurring study sessions created!', 'success')
    return redirect(url_for('main.home'))
