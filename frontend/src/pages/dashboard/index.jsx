import React from "react";
import UserCard from "./../../components/user-card/index";
import CountChart from './../../components/count-chart/index';
import AttendanceChart from '../../components/attendance/index';

const DashboardPage = () => {
  return (
    <div className="p-4 flex gap-4 flex-col md:flex-row">
      {/*Left */}
      <div className="w-full lg:w-2/3 flex flex-col gap-8">
        <div className="flex gap-4 justify-between flex-wrap">
          <UserCard type="student" />
          <UserCard type="teacher" />
          <UserCard type="parent" />
          <UserCard type="staff" />
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
          {/*Bottom chart */}
          <div></div>
        </div>
      </div>

      {/*Right */}
      <div className="w-full lg:w-1/3"></div>
    </div>
  );
};

export default DashboardPage;
