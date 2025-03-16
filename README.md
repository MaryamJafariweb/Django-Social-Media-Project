Django Social Media App
Overview
This is a Django-based social media platform that allows users to create and share posts, like posts, follow/unfollow other users, and comment on posts. It provides a dynamic and interactive space for social engagement.

Features
User Authentication: Register, login, and manage profiles
Post Creation: Users can create and share posts
Like System: Users can like or unlike posts
Follow/Unfollow: Users can follow and unfollow others
Comment System: Users can leave comments under posts
User Profiles: Each user has a profile page showing their posts and followers
Responsive Design: Optimized for both desktop and mobile devices
Technologies Used
Backend: Django, Django REST Framework
Database: PostgreSQL / SQLite
Frontend: HTML, CSS, Bootstrap
Authentication: Django’s built-in authentication system
Version Control: Git & GitHub

## Installation & Setup  
1. Clone the repository:  
   `bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies:
pip install -r requirements.txt
4. Run migrations and start the server:
python manage.py migrate
python manage.py runserver
Future Improvements
Direct Messaging: Private chat between users
Stories Feature: Temporary posts that disappear after 24 hours
Notifications: Alerts for likes, comments, and follows
