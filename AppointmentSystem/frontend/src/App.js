import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import AppointmentBooking from "./components/AppointmentBooking";


function App() {
  return (
    <Router>
      <div className="min-h-screen flex justify-center items-center bg-gray-100">
        <Routes>
          <Route path="/" element={<AppointmentBooking />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
