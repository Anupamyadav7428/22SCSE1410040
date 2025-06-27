<!-- # 22SCSE1410040 -->


A simple Django REST API that converts long URLs into short, easy-to-share links. Perfect for developers who need to integrate URL shortening into their applications.
Feature 
Create short URLs from long ones
Track click counts
JWT authentication for security
RESTful endpoints for easy integration

Setup
Installation
git clone https://github.com/anupamyadav7428/22scse1410040

setup virtual env
python -m venv venv
./env/scripts/activate
pip install -r requirements.txt


run migations 
python manage.py migrate

create superuser
python manage.py createsuperuser

Endpoint	                    Method	Description
/api/auth/register/	            POST	Register new user
/api/auth/login/	            POST	Get JWT tokens
/api/auth/login/refresh/    	POST	Refresh access token

URL Shortener
Endpoint	        Method	Description
/api/urls/	        POST	Create short URL
/api/urls/	        GET	    List your short URLs
/{short_code}/	    GET	    Redirect to original URL



Register
<!-- curl -X POST http://localhost:8000/api/auth/register/  -->
-H "Content-Type: application/json" \
-d '{"username":"fakeusername", "email":"fakeemailid@gmail.com", "password":"testpass123"}'


Login
<!-- curl -X POST http://localhost:8000/api/auth/login/ \ -->
-H "Content-Type: application/json" \
-d '{"username":"testuser", "password":"testpass123"}'



create short url 
<!-- curl -X POST http://localhost:8000/api/urls/ \ -->
-H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
-H "Content-Type: application/json" \
-d '{"original_url":"https://example.com/very/long/url"}'


<!-- user shortcut -->
http://localhost:8000/abc123
