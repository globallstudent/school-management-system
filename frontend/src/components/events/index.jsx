import React, { useState } from 'react'
import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css'

const events = [
  {
    id: 2,
    title: "Zakovat",
    time: "12:00 PM - 2:00 PM",
    description:
      "Zakovat turneri 3-bosqichi taqdirlash marosimi munosabati bilan tadbirmiz o'tkaziladi",
  },
  {
    id: 1,
    title: "Bitiruv marosimi",
    time: "12:00 PM - 2:00 PM",
    description:
      "11-sunfalrimizning bitiruv marsomini 27-may kuni o'tkazish rajalashtirildi",
  },
  {
    id: 3,
    title: "Navruz bayrami",
    time: "12:00 PM - 2:00 PM",
    description: "Navruz bayrami munosabati bilan katta tadbir uyushtiladigan bo'ldi",
  },
];

const EventCalendar = () => {
  const [value , onChange] = useState(new Date());
  return (
    <div className="bg-white p-4 rounded-md">
      <Calendar onChange={onChange} value={value} />
      <div className="flex items-center justify-between">
        <h1 className="text-xl font-semibold my-4">Events</h1>
        <img className="w-[20px] h-[20px]" src="/moreDark.png" alt="moreDark" />
      </div>
      <div className="flex flex-col gap-4">
        {events?.map((event) => (
          <div
            className="p-5 rounded border-2 border-gray-100 border-t-4 odd:border-t-[#F6AD2B] even:border-t-[#233255]"
            key={event?.id}
          >
            <div className="flex items-center justify-between">
              <h1 className="font-semibold text-gray-600">{event.title}</h1>
              <span className="text-gray-400 text-xs">{event.time}</span>
            </div>
            <p className='mt-2 text-gray-400 text-sm'>{event.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default EventCalendar