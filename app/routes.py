from flask import Blueprint, render_template
from .strava_service import StravaService

# Create a blueprint
main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def index():
    """Main landing page"""
    try:
        athlete = StravaService.get_athlete_profile()
        return render_template('index.html', athlete=athlete)
    except Exception as e:
        return f"Error fetching athlete profile: {str(e)}", 500

@main_blueprint.route('/activities')
def activities():
    """Display recent activities"""
    try:
        raw_activities = StravaService.get_recent_activities()
        formatted_activities = StravaService.format_activity_data(raw_activities)
        return render_template('activities.html', activities=formatted_activities)
    except Exception as e:
        return f"Error fetching activities: {str(e)}", 500