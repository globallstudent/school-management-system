import React, { useState } from "react";

const ClassesPage = () => {
  // Har bir sinf uchun darslar ma'lumotlari
  const [classes, setClasses] = useState([
    // Dushanba
    {
      title: "Math",
      teacher: "Mr. Smith",
      room: "101",
      time: "08:00 AM",
      day: "Monday",
      classLevel: "1",
      className: "A",
    },
    {
      title: "Physics",
      teacher: "Dr. Johnson",
      room: "102",
      time: "10:00 AM",
      day: "Monday",
      classLevel: "1",
      className: "A",
    },
    {
      title: "History",
      teacher: "Ms. Brown",
      room: "103",
      time: "12:00 PM",
      day: "Monday",
      classLevel: "1",
      className: "A",
    },
    {
      title: "English",
      teacher: "Ms. Green",
      room: "105",
      time: "02:00 PM",
      day: "Monday",
      classLevel: "1",
      className: "B",
    },
    // Seshanba
    {
      title: "History",
      teacher: "Ms. Brown",
      room: "103",
      time: "08:00 AM",
      day: "Tuesday",
      classLevel: "2",
      className: "B",
    },
    {
      title: "Math",
      teacher: "Mr. Smith",
      room: "101",
      time: "10:00 AM",
      day: "Tuesday",
      classLevel: "2",
      className: "B",
    },
    {
      title: "Physics",
      teacher: "Dr. Johnson",
      room: "102",
      time: "12:00 PM",
      day: "Tuesday",
      classLevel: "2",
      className: "B",
    },
    {
      title: "Mother Tongue",
      teacher: "Mr. White",
      room: "104",
      time: "02:00 PM",
      day: "Tuesday",
      classLevel: "2",
      className: "C",
    },
    // Chorshanba
    {
      title: "English",
      teacher: "Ms. Green",
      room: "105",
      time: "08:00 AM",
      day: "Wednesday",
      classLevel: "3",
      className: "A",
    },
    {
      title: "Math",
      teacher: "Mr. Smith",
      room: "101",
      time: "10:00 AM",
      day: "Wednesday",
      classLevel: "3",
      className: "A",
    },
    {
      title: "Physics",
      teacher: "Dr. Johnson",
      room: "102",
      time: "12:00 PM",
      day: "Wednesday",
      classLevel: "3",
      className: "C",
    },
    {
      title: "History",
      teacher: "Ms. Brown",
      room: "103",
      time: "02:00 PM",
      day: "Wednesday",
      classLevel: "3",
      className: "A",
    },
    // Payshanba
    {
      title: "Math",
      teacher: "Mr. Smith",
      room: "101",
      time: "08:00 AM",
      day: "Thursday",
      classLevel: "3",
      className: "A",
    },
    {
      title: "History",
      teacher: "Ms. Brown",
      room: "103",
      time: "10:00 AM",
      day: "Thursday",
      classLevel: "3",
      className: "B",
    },
    {
      title: "English",
      teacher: "Ms. Green",
      room: "105",
      time: "12:00 PM",
      day: "Thursday",
      classLevel: "3",
      className: "A",
    },
    {
      title: "Physics",
      teacher: "Dr. Johnson",
      room: "102",
      time: "02:00 PM",
      day: "Thursday",
      classLevel: "3",
      className: "C",
    },
    // Juma
    {
      title: "Math",
      teacher: "Mr. Smith",
      room: "101",
      time: "08:00 AM",
      day: "Friday",
      classLevel: "1",
      className: "C",
    },
    {
      title: "Physics",
      teacher: "Dr. Johnson",
      room: "102",
      time: "10:00 AM",
      day: "Friday",
      classLevel: "1",
      className: "C",
    },
    {
      title: "History",
      teacher: "Ms. Brown",
      room: "103",
      time: "12:00 PM",
      day: "Friday",
      classLevel: "1",
      className: "C",
    },
    {
      title: "Mother Tongue",
      teacher: "Mr. White",
      room: "104",
      time: "02:00 PM",
      day: "Friday",
      classLevel: "1",
      className: "C",
    },
  ]);

  // Sinf raqami va sinf bo'linmasini tanlash uchun state
  const [selectedClassLevel, setSelectedClassLevel] = useState("1");
  const [selectedClassName, setSelectedClassName] = useState("A");

  // Filtred classes (tanlangan sinf va bo'linmaga asoslangan darslar)
  const filteredClasses = classes.filter(
    (cls) =>
      cls.classLevel === selectedClassLevel &&
      cls.className === selectedClassName
  );

  // Sinf raqamlari (1-sinf, 2-sinf, va hokazo)
  const classLevels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"];

  // Sinf bo'linmalari (A, B, C)
  const classNames = ["A", "B", "C"];

  // Kunlar va dars vaqti
  const daysOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"];
  const times = ["08:00 AM", "10:00 AM", "12:00 PM", "02:00 PM"];

  return (
    <div className="p-6 bg-gray-100 min-h-screen">
      {/* Sinf raqami tanlash */}
      <div className="mb-4">
        <label className="text-lg font-semibold">Select Class Level:</label>
        <select
          onChange={(e) => setSelectedClassLevel(e.target.value)}
          value={selectedClassLevel}
          className="p-2 border rounded-md"
        >
          {classLevels.map((level) => (
            <option key={level} value={level}>
              {level}-Sinf
            </option>
          ))}
        </select>
      </div>

      {/* Sinf bo'linmasini tanlash */}
      <div className="mb-4">
        <label className="text-lg font-semibold">Select Class Name:</label>
        <select
          onChange={(e) => setSelectedClassName(e.target.value)}
          value={selectedClassName}
          className="p-2 border rounded-md"
        >
          {classNames.map((name) => (
            <option key={name} value={name}>
              Class {name}
            </option>
          ))}
        </select>
      </div>

      {/* Dars jadvali */}
      <div className="overflow-x-auto">
        <table className="min-w-full table-auto bg-white shadow-lg rounded-lg">
          <thead>
            <tr className="text-white bg-blue-600">
              <th className="px-4 py-2 text-left">Time</th>
              {daysOfWeek.map((day) => (
                <th key={day} className="px-4 py-2 text-center">
                  {day}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {times.map((time) => (
              <tr key={time} className="border-t">
                <td className="px-4 py-2 text-left bg-gray-200">{time}</td>
                {daysOfWeek.map((day) => {
                  const classAtTime = filteredClasses.find(
                    (cls) => cls.time === time && cls.day === day
                  );
                  return (
                    <td key={day} className="px-4 py-2">
                      {classAtTime ? (
                        <div className="bg-blue-100 p-2 rounded-lg shadow-sm">
                          <p className="font-bold">{classAtTime.title}</p>
                          <p className="text-sm">{classAtTime.teacher}</p>
                          <p className="text-xs text-gray-500">
                            {classAtTime.room}
                          </p>
                        </div>
                      ) : (
                        <div className="h-full flex items-center justify-center text-gray-500">
                          {/* Bo'sh vaqt uchun default height */}
                          <div className="min-h-[80px] flex items-center justify-center text-gray-400">
                            No Class
                          </div>
                        </div>
                      )}
                    </td>
                  );
                })}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default ClassesPage;
