import requests
from flask import current_app
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class StravaService:
    BASE_URL = "https://www.strava.com/api/v3"
    ACCESS_TOKEN = os.getenv('STRAVA_ACCESS_TOKEN')

    @classmethod
    def get_athlete_profile(cls):
        """Fetch comprehensive athlete profile data"""
        endpoint = f"{cls.BASE_URL}/athlete"
        headers = {"Authorization": f"Bearer {cls.ACCESS_TOKEN}"}
        
        try:
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching athlete profile: {e}")
            raise

    @classmethod
    def get_recent_activities(cls, limit=10):
        """Retrieve recent athletic activities"""
        endpoint = f"{cls.BASE_URL}/athlete/activities"
        headers = {"Authorization": f"Bearer {cls.ACCESS_TOKEN}"}
        params = {"per_page": limit}
        
        try:
            response = requests.get(endpoint, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching activities: {e}")
            raise

    @classmethod
    def format_activity_data(cls, activities):
        """Format activities for easy rendering"""
        formatted_activities = []
        for activity in activities:
            formatted_activities.append({
                'name': activity.get('name', 'Unnamed Activity'),
                'type': activity.get('type', 'Unknown'),
                'date': datetime.strptime(activity['start_date_local'], "%Y-%m-%dT%H:%M:%SZ").strftime("%B %d, %Y"),
                'distance': round(activity.get('distance', 0) / 1000, 2),  # Convert to kilometers
                'time': round(activity.get('moving_time', 0) / 60, 2),  # Convert to minutes
            })
        return formatted_activities