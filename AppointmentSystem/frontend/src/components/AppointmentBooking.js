import React, { useState } from "react";
import DatePicker from "./DatePicker";
import SlotSelector from "./SlotSelector";
import BookingForm from "./BookingForm";

const AppointmentBooking = () => {
  const [selectedDate, setSelectedDate] = useState("");
  const [selectedSlot, setSelectedSlot] = useState("");

  return (
    <div className="max-w-md mx-auto bg-white shadow-lg rounded-lg p-6">
      <h2 className="text-xl font-bold text-center">Book an Appointment</h2>
      <DatePicker selectedDate={selectedDate} setSelectedDate={setSelectedDate} />
      <SlotSelector selectedDate={selectedDate} selectedSlot={selectedSlot} setSelectedSlot={setSelectedSlot} />
      <BookingForm selectedDate={selectedDate} selectedSlot={selectedSlot} />
    </div>
  );
};

export default AppointmentBooking;
