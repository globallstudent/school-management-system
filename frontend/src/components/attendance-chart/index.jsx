import React from "react";
import {
  BarChart,
  Bar,
  Rectangle,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";

const AttendanceChart = () => {
  const data = [
    {
      name: "Dush",
      borlar: 60,
      yoqlar: 40,
    },
    {
      name: "Sesh",
      borlar: 20,
      yoqlar: 90,
    },
    {
      name: "Chor",
      borlar: 55,
      yoqlar: 70,
    },
    {
      name: "Pay",
      borlar: 60,
      yoqlar: 85,
    },
    {
      name: "Jum",
      borlar: 45,
      yoqlar: 70,
    },
  ];
  return (
    <div className="bg-white rounded-lg p-4 h-full">
      <div className="flex justify-between items-center">
        <h1 className="text-lg font-semibold">Yo'qlama</h1>
        <img
          src="/moreDark.png"
          className="w-[20px] h-[20px]"
          alt="moreDarkPng"
        />
      </div>
      <ResponsiveContainer width="100%" height="90%">
        <BarChart width={500} height={300} data={data} boxSize={20}>
          <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#ddd" />
          <XAxis
            dataKey="name"
            axisLine={false}
            tick={{ fill: "#233255" }}
            tickLine={false}
          />
          <YAxis axisLine={false} tick={{ file: "#233255" }} tickLine={false} />
          <Tooltip
            contentStyle={{ borderRadius: "10px", borderColor: "lightgray" }}
          />
          <Legend
            align="left"
            verticalAlign="top"
            wrapperStyle={{ paddingTop: "20px", paddingBottom: "40px" }}
          />
          <Bar
            dataKey="borlar"
            fill="#F6AD2B"
            legendType="circle"
            radius={[10, 10, 0, 0]}
          />
          <Bar
            dataKey="yoqlar"
            fill="#233255"
            legendType="circle"
            radius={[10, 10, 0, 0]}
          />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
};

export default AttendanceChart;
