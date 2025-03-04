

import React, { useState } from "react";
import axios from "axios";

const BookingForm = ({ selectedDate, selectedSlot }) => {
  const [name, setName] = useState("");
  const [phone, setPhone] = useState("");
  const [message, setMessage] = useState("");

  const validatePhone = (phone) => {
    const phonePattern = /^[0-9]{10}$/; // Ensures a 10-digit phone number
    return phonePattern.test(phone);
  };

  const handleBooking = () => {
    if (!name.trim()) {
      setMessage("Name is required.");
      return;
    }

    if (!phone.trim()) {
      setMessage("Phone number is required.");
      return;
    }

    if (!validatePhone(phone)) {
      setMessage("Please enter a valid 10-digit phone number.");
      return;
    }

    if (!selectedSlot) {
      setMessage("Please select a time slot.");
      return;
    }

    axios.post("http://localhost:8000/book/", {
      name,
      phone_number: phone,
      date: selectedDate,
      time_slot: selectedSlot,
    })
    .then(() => setMessage("Appointment booked successfully!"))
    .catch(() => setMessage("Error booking appointment."));
  };

  return (
    <div className="p-4">
      <label className="block text-gray-700">Name:</label>
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
        className="border p-2 rounded w-full"
      />

      <label className="block text-gray-700 mt-2">Phone Number:</label>
      <input
        type="text"
        value={phone}
        onChange={(e) => setPhone(e.target.value)}
        className="border p-2 rounded w-full"
      />

      <button 
        onClick={handleBooking} 
        className="mt-4 bg-blue-600 text-white p-2 rounded w-full"
      >
        Book Appointment
      </button>

      {message && (
  <p className={`mt-2 ${message === "Appointment booked successfully!" ? "text-green-500" : "text-red-500"}`}>
    {message}
  </p>
)}

    </div>
  );
};

export default BookingForm;
