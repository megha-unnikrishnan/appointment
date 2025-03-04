import React from "react";
import ReactDOM from "react-dom";
import AppointmentBooking from "./components/AppointmentBooking";

window.renderAppointmentBooking = function (elementId) {
  ReactDOM.render(<AppointmentBooking />, document.getElementById(elementId));
};
