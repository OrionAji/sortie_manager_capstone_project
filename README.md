This is my capstone project necessary for graduation from ALX. 
The API i am building is a sorties manager for a flying unit. 
It helps track available aircraft and match them with pilots who are able to fly, both physically and mentally.

# Alpha Jet Sortie Manager (AJSM) API ✈️

## 📌 Project Overview
The **Alpha Jet Sortie Manager** is a specialized RESTful API designed for military aviation squadrons. It coordinates the "Golden Triangle" of mission readiness: the **Aircraft**, the **Pilot**, and the **Sortie**. 

This system moves beyond simple scheduling by enforcing tactical safety rules, such as blocking flight assignments for grounded aircraft and ensuring mandatory pilot rest periods.

## 🏆 ALX Capstone Criteria Met
* **Originality:** Custom aviation logic for Alpha Jet fleet management.
* **CRUD Functionality:** Full implementation for Aircraft, Pilots, and Missions.
* **Database Design:** Relational schema using ForeignKeys and status constraints.
* **Error Handling:** Custom validation (400 Bad Request) and logging for safety violations.
* **API Documentation:** Interactive Swagger/OpenAPI documentation.

## 🛠️ Tech Stack
* **Framework:** Django & Django REST Framework (DRF)
* **Database:** SQLite (Development) / PostgreSQL (Production)
* **Documentation:** drf-spectacular (OpenAPI 3.0)
* **Logging:** Python Logging Module

## 🚀 Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone <your-repo-link>
   cd sortie_manager_capstone_project
2. Set up Virtual Environment:Bashpython -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

4. Install Dependencies:Bashpip install -r requirements.txt

5. Apply Migrations:Bashpython manage.py makemigrations
python manage.py migrate

6. Create Admin User:Bashpython manage.py createsuperuser

7. Run Server:Bashpython manage.py runserver
   
📡 API EndpointsMethodEndpointDescriptionGET/api/v1/aircraft/List all Alpha Jets.GET/api/v1/aircraft/readiness_report/Custom: Get fleet MC (Mission Capable) rates.POST/api/v1/sorties/Schedule a mission (Validated against airframe status).GET/api/docs/Swagger UI interactive documentation.
