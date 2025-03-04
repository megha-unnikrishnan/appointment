import React, { useEffect, useState } from "react";
import axios from "axios";

const SlotSelector = ({ selectedDate, selectedSlot, setSelectedSlot }) => {
  const [slots, setSlots] = useState([]);

  useEffect(() => {
    if (selectedDate) {
      axios
        .get(`http://localhost:8000/slots/${selectedDate}/`)
        .then((response) => setSlots(response.data.available_slots))
        .catch(() => setSlots([]));
    }
  }, [selectedDate]);

  return (
    <div className="p-6 bg-white shadow-md rounded-lg">
      <h3 className="text-lg font-semibold text-gray-700 mb-3">Available Time Slots</h3>

      <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
        {slots.length ? (
          slots.map((slot) => (
            <button
              key={slot}
              className={`p-3 rounded-lg text-lg font-medium transition-all duration-200 ease-in-out
                ${
                  selectedSlot === slot
                    ? "bg-blue-600 text-white shadow-lg transform scale-105"
                    : "bg-gray-200 text-gray-700 hover:bg-blue-500 hover:text-white hover:shadow-md"
                }`}
              onClick={() => setSelectedSlot(slot)}
            >
              {slot}
            </button>
          ))
        ) : (
          <p className="text-red-500 text-center col-span-full">No slots available</p>
        )}
      </div>
    </div>
  );
};

export default SlotSelector;
