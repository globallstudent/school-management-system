import React from "react";
import { PieChart, Pie, Cell } from "recharts";
import { FaGraduationCap } from "react-icons/fa"; // Icon uchun

const COLORS = ["#2C3E50", "#F5B041"]; // Erkaklar - dark blue, Ayollar - yellow

const UserCard = ({ type, count, malePercent, femalePercent }) => {
  const data = [
    { name: "Erkaklar", value: malePercent },
    { name: "Ayollar", value: femalePercent },
  ];

  return (
    <div className="bg-white p-4 rounded-2xl shadow-md max-w-[400px] w-full flex items-center gap-4">
      {/* Iconli halqa */}
      <div className="relative w-[70px] h-[80px]">
        <PieChart width={70} height={80}>
          <Pie
            data={data}
            cx="50%"
            cy="50%"
            innerRadius={30}
            outerRadius={35}
            dataKey="value"
            startAngle={90}
            endAngle={-270}
          >
            {data.map((entry, index) => (
              <Cell key={`cell-${index}`} fill={COLORS[index]} />
            ))}
          </Pie>
        </PieChart>
        {/* Icon - markazda */}
        <div className="absolute top-[50%] left-[50%] -translate-x-1/2 -translate-y-1/2">
          <h1 className="text-lg font-bold text-[#233255]">{count}ta</h1>
        </div>
      </div>

      {/* Ma'lumot qismi */}
      <div>
        <h2 className="text-[15px] text-gray-500 font-medium">{type}</h2>
        <div className="text-[11px] mt-1 mb-2">
          <span className="text-[#233255] font-semibold mr-2">
            Erkaklar ({malePercent}%)
          </span>
          <br />
          <span className="text-[#F6AD2B] font-semibold">
            Ayollar ({femalePercent}%)
          </span>
        </div>
      </div>
    </div>
  );
};

export default UserCard;
