import React from "react";
import {
  Legend,
  RadialBar,
  ResponsiveContainer,
  RadialBarChart,
} from "recharts";

const data = [
  {
    name: "Total",
    const: 106,
    fill: "white",
  },
  {
    name: "Girls",
    const: 53,
    fill: "#fae27c",
  },
  {
    name: "Boys",
    const: 53,
    fill: "#c3ebfa",
  },
];

const CountChart = () => {
  return (
    <div className="bg-white rounded-xl w-full h-full p-4">
      <div className="flex justify-between items-center">
        <h1 className="text-lg font-semibold">S tudents</h1>
        <img src="/moreDark.png" alt="moreDark" />
      </div>
      <div className="relative w-full h-[75%]">
        <ResponsiveContainer>
          <RadialBarChart
            cx="50%"
            cy="50%"
            innerRadius="40%"
            outerRadius="100%"
            barSize={32}
            data={data}
          >
            <RadialBar background dataKey="const" />
          </RadialBarChart>
        </ResponsiveContainer>
        <img
          src="/maleFemale.png"
          className="w-[50px] h-[50px] absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2"
          alt="male-Female"
        />
      </div>

      <div className="flex justify-center gap-16">
        <div className="flex flex-col gap-1">
          <div className="w-5 h-5 bg-[#c3ebfa] rounded-full"></div>
          <h1 className="font-bold">1,234</h1>
          <h2 className="text-xs text-gray-300">Boys (55%)</h2>
        </div>
        <div className="flex flex-col gap-1">
          <div className="w-5 h-5 bg-[#fae27c] rounded-full"></div>
          <h1 className="font-bold">1,124</h1>
          <h2 className="text-xs text-gray-300">Girls (45%)</h2>
        </div>
      </div>
    </div>
  );
};

export default CountChart;
