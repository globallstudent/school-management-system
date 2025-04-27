import React from "react";
import UserCard from "./../../components/user-card/index";
import CountChart from './../../components/count-chart/index';
import AttendanceChart from '../../components/attendance-chart/index';
import FinanceChart from './../../components/finance-chart/index';
import EventCalendar from './../../components/events/index';
import Announcement from "./../../components/announcements";

const userStats = [
  { type: "O'QUVCHILAR", count: 308, malePercent: 61, femalePercent: 39 },
  { type: "O'QITUVCHILAR", count: 50, malePercent: 40, femalePercent: 60 },
  { type: "OTA-ONALAR", count: 50, malePercent: 40, femalePercent: 60 },
  { type: "XODIMLAR", count: 80, malePercent: 45, femalePercent: 55 },
];

const DashboardPage = () => {
  return (
    <div className="flex gap-4 flex-col md:flex-row">
      {/*Left */}
      <div className="w-full lg:w-2/3 flex flex-col gap-8">
        <div className="flex gap-4 justify-between flex-wrap lg:grid lg:grid-cols-2 xl:grid-cols-4">
          {userStats.map((item, idx) => (
            <UserCard
              key={idx}
              type={item.type}
              count={item.count}
              malePercent={item.malePercent}
              femalePercent={item.femalePercent}
            />
          ))}
        </div>
        {/*Middle chart */}
        <div className="flex gap-4 flex-col lg:flex-row">
          {/*Count  chart */}
          <div className="w-full lg:w-1/3 h-[450px]">
            <CountChart />
          </div>
          {/*Attendance chart */}
          <div className="w-full lg:w-2/3 h-[450px]">
            <AttendanceChart />
          </div>
        </div>
        {/*Bottom chart */}
        <div className="w-full h-[500px]">
          <FinanceChart />
        </div>
      </div>

      {/*Right */}
      <div className="w-full lg:w-1/3 flex flex-col gap-8">
        <EventCalendar/>
        <Announcement/>
      </div>
    </div>
  );
};

export default DashboardPage;
