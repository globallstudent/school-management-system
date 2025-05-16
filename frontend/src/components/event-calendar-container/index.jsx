import React from "react";
import EventLists from "../event-lists";

const EventCalendarContainer = async () => {
  return (
    <div className="bg-white p-4 rounded-md">
      <Calendar />
      <div className="flex items-center justify-between">
        <h1 className="text-xl font-semibold my-4">Events</h1>
        <img className="w-[20px] h-[20px]" src="/moreDark.png" alt="moreDark" />
      </div>
      <div className="flex flex-col gap-4">
        <EventLists/>
      </div>
    </div>
  );
};

export default EventCalendarContainer;
