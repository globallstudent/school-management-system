import React from "react";

const Announcement = () => {
  return (
    <div className="bg-white p-4 rounded-md">
      <div className="flex items-center justify-between">
        <h1 className="text-xl font-semibold">E'lonlar</h1>
        <span className="text-xs text-gray-400">Hammasini ko'rish</span>
      </div>
      <div className="flex flex-col gap-4 mt-4">
        <div className="bg-[#F6AD2B] rounded-md p-4">
          <div className="flex items-center justify-between">
            <h2 className="font-medium">Lorem ipsum dolor sit</h2>
            <span className="text-xs text-gray-400 bg-white rounded-md px-1 py-1">
              2025-01-01
            </span>
          </div>
          <p className="text-sm text-gray-900 mt-1">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam
            quibusdam, officiis dolore provident quia cum?
          </p>
        </div>
        <div className="bg-[#233255] rounded-md p-4">
          <div className="flex items-center justify-between">
            <h2 className="font-medium text-white">Lorem ipsum dolor sit</h2>
            <span className="text-xs text-gray-400 bg-white rounded-md px-1 py-1">
              2025-01-01
            </span>
          </div>
          <p className="text-sm text-gray-400 mt-1">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam
            quibusdam, officiis dolore provident quia cum?
          </p>
        </div>
      </div>
    </div>
  );
};

export default Announcement;
