import React, { useState } from "react";

const DatePicker = ({ selectedDate, setSelectedDate }) => {
  const [errorMessage, setErrorMessage] = useState("");

  const handleDateChange = (e) => {
    const selected = e.target.value;
    const today = new Date().toISOString().split("T")[0]; 

    if (selected < today) {
      setErrorMessage("⚠️ Booking for past dates is not allowed. Please select a future date.");
    } else {
      setErrorMessage("");
      setSelectedDate(selected);
    }
  };

  return (
    <div className="p-4 bg-white shadow-md rounded-lg">
      <label className="block text-gray-700 text-lg font-medium mb-2">Select Date:</label>
      <input
        type="date"
        value={selectedDate}
        onChange={handleDateChange}
        min={new Date().toISOString().split("T")[0]}
        className="border p-2 rounded w-full focus:ring focus:ring-blue-300"
      />

      {errorMessage && <p className="text-red-500 mt-2">{errorMessage}</p>}
    </div>
  );
};

export default DatePicker;
