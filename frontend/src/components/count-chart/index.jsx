import React from "react";
import {
  Legend,
  RadialBar,
  ResponsiveContainer,
  RadialBarChart,
} from "recharts";

const data = [
  {
    name: "Umumiy",
    const: 106,
    fill: "white",
  },
  {
    name: "Qizlar",
    const: 33,
    fill: "#F6AD2B",
  },
  {
    name: "Bolalar",
    const: 73,
    fill: "#233255",
  },
];

const CountChart = () => {
  return (
    <div className="bg-white rounded-xl w-full h-full p-4">
      <div className="flex justify-between items-center">
        <h1 className="text-lg font-semibold">O'quvchilar</h1>
        <img src="/moreDark.png" className="w-[20px] h-[20px]" alt="moreDark" />
      </div>
      <div className="relative w-full h-[75%]">
        <ResponsiveContainer>
          <RadialBarChart
            cy="50%"
            cx="50%"
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
          className="w-[50px]  h-[50px] absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2"
          alt="male-Female"
        />
      </div>

      <div className="flex justify-center gap-4">
        {data?.map((item) => (
          <div className="flex  flex-col gap-1">
            <div
              className={`w-5 h-5 ${
                item?.name === "Total"
                  ? "bg-[#093f9f]"
                  : item?.name === "Boys"
                  ? "bg-[#233255]"
                  : "bg-[#F6AD2B]"
              }  rounded-full`}
            ></div>
            <h1 className="font-bold">{item?.const} ta</h1>
            <h2 className="text-xs text-gray-500">
              {item?.name} {(item?.const / 100) * 100} %
            </h2>
          </div>
        ))}
      </div>
    </div>
  );
};

export default CountChart;
