# 📅 Appointment Booking System

A Django and React.js-based system for booking appointments efficiently, with an intuitive frontend and a robust backend.

## 🚀 Features

✅ Book appointments with available time slots <br>
✅ Secure API for managing bookings<br>
✅ Responsive UI built with React.js<br>
✅ Django-powered backend with sqlite<br>

### 🛠 Technology Stack

#### Backend (Django & DRF)

Django REST Framework (DRF)

#### Frontend (React.js)

React.js <br>
Tailwind CSS for styling<br>
Axios for API requests<br>

### 📌 Installation & Setup

## 1️⃣ Backend Setup (Django)

*Step 1: Clone the Repository*


    git clone https://github.com/your-username/Appointment_system.git
    cd appointment-system/backend

*Step 2: Create a Virtual Environment & Activate It*


    python -m venv env
    source env/bin/activate  # Windows: venv\Scripts\activate

*Step 3: Install Dependencies*


    pip install -r requirements.txt
*Step 4: Apply Database Migrations*


    python manage.py migrate <br>
    python manage.py makemigrations

*Step 5: Run the Development Server*

python manage.py runserver

#### 🖥 Backend will be available at: http://localhost:8000/



## 2️⃣ Frontend Setup (React.js)

*Step 1: Navigate to the Frontend Directory*

    cd ../frontend
    cd appointment_system
    
*Step 2: Install Dependencies*

    npm install
    
*Step 3: Start the React Development Server*

    npm start
    
#### 🌐 Frontend will be available at: http://localhost:3000/

### 🔗 API Endpoints

#### 1️⃣ Get Available Slots

Endpoint: GET /slots/?date=YYYY-MM-DD

Response Example:

{"available_slots":["10:00","11:00","11:30","12:00","12:30","02:00","02:30","03:00","03:30","04:00","04:30"]}


#### 2️⃣ Create an Appointment

Endpoint: POST /book/

Request Body Example:

{
    "name": "John Doe",
    "phone_number": "+1234567890",
    "date": "2025-03-05",
    "time_slot": "14:30"
}

Response Example:

{
  {
    "name": "John Doe",
    "phone_number": "+1234567890",
    "date": "2025-03-05",
    "time_slot": "14:30"
}

}
🎯 Usage Instructions

1️⃣ Open the web application in your browser.<br>
2️⃣ Select a date to view available slots.<br>
3️⃣ Choose a time slot and enter your details.<br>
4️⃣ Click "Book Appointment".<br>
5️⃣ Receive a confirmation message upon successful booking.<br>


📜 License
This project is licensed under the MIT License.

