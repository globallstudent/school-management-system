import { useState } from "react";
import {
  Home,
  Users,
  BookOpen,
  Settings,
  ChevronLeft,
  ChevronRight,
} from "lucide-react";
import { Tooltip as ReactTooltip } from "react-tooltip";
import { NavLink } from "react-router-dom"; // Import NavLink
import useLayoutStore from "./../../store/layout-control/index";

const Sidebar = () => {
  const bgMainColor = "bg-[#093f9f]";

  const { isOpen, setIsOpen } = useLayoutStore();
  const [activeItem, setActiveItem] = useState("Dashboard");

  const navItems = [
    { label: "Dashboard", icon: Home, path: "/dashboard" },
    { label: "Students", icon: Users, path: "/students" },
    { label: "Teachers", icon: BookOpen, path: "/teachers" },
    { label: "Parents", icon: BookOpen, path: "/parents" },
  ];

  return (
    <div
      className={`fixed left-5 top-20 mb-[20px] h-[88%] flex flex-col transition-all duration-300 ease-in-out
        ${isOpen ? "w-64 rounded-[30px]" : "w-[70px] rounded-[50px]"}
        ${bgMainColor}
        border-[#fff] border-[2px]`}
    >
      {/* Toggle button */}
      <button
        onClick={() => setIsOpen(!isOpen)}
        className={`absolute -right-5 top-12 bg-[#fff] w-[30px] h-[70px] flex justify-center items-center cursor-pointer rounded-full p-1 shadow-md z-10
          ${isOpen ? "rotate-180" : ""}`}
      >
        {isOpen ? (
          <ChevronLeft className="text-[#233255] -rotate-180" size={30} />
        ) : (
          <ChevronRight className="text-[#233255]" size={30} />
        )}
      </button>

      {/* Main menu (top part) */}
      <div className="flex-1 flex flex-col pt-5">
        {navItems.map((item) => (
          <NavLink
            key={item.label}
            to={item.path} // Use NavLink's `to` prop for routing
            onClick={() => setActiveItem(item.label)}
            className={`flex items-center cursor-pointer transition-all my-1
              rounded-lg text-[16px] group ${
                isOpen
                  ? "px-3 h-[40px] mx-2"
                  : "flex justify-center mx-auto w-[40px] h-[40px]"
              }
              ${
                activeItem === item.label
                  ? "bg-white bg-opacity-20 text-[#093f9f]"
                  : "hover:bg-blue-100 hover:bg-opacity-10 text-[#093f9f] opacity-70"
              }`}
            data-tooltip-id={item.label} // Tooltip for id
            data-tooltip-content={isOpen ? "" : item.label} // Tooltip is shown only when sidebar is closed
            end // Ensure the active state works correctly
          >
            <item.icon
              size={30}
              className={`${
                activeItem === item.label
                  ? "text-[#093f9f]"
                  : "text-white group-hover:text-[#093f9f] "
              }`}
            />
            {isOpen && (
              <span
                className={`ml-4 block font-medium group-hover:text-[#093f9f] ${
                  activeItem === item.label
                    ? "text-[#093f9f]"
                    : "text-white opacity-70"
                }`}
              >
                {item.label}
              </span>
            )}
          </NavLink>
        ))}
      </div>

      {/* Settings (bottom part) */}
      <NavLink
        to="/settings" // Path for settings
        onClick={() => setActiveItem("Settings")}
        className={`flex items-center cursor-pointer transition-all my-1
          rounded-lg mb-5 text-[16px] group ${
            isOpen
              ? "px-3 h-[40px] mx-2"
              : "flex justify-center mx-auto w-[40px] h-[40px]"
          }
          ${
            activeItem === "Settings"
              ? "bg-white bg-opacity-20 text-[#093f9f] group-hover:text-[#093f9f]"
              : "hover:bg-blue-100 hover:bg-opacity-10 text-white opacity-70"
          }`}
        data-tooltip-id="Settings" // Tooltip for id
        data-tooltip-content={isOpen ? "" : "Settings"} // Tooltip is shown only when sidebar is closed
        end
      >
        <Settings
          size={30}
          className={` group-hover:text-[#093f9f] ${
            activeItem === "Settings"
              ? "text-[#093f9f]"
              : "text-white opacity-70"
          }`}
        />
        {isOpen && (
          <span
            className={`ml-4 group-hover:text-[#093f9f] text-white font-medium ${
              activeItem === "Settings" ? "text-[#093f9f]" : "opacity-70"
            }`}
          >
            Settings
          </span>
        )}
      </NavLink>

      {/* ReactTooltip component with 'place' attribute set to 'right' */}
      <ReactTooltip id="Dashboard" place="right" />
      <ReactTooltip id="Students" place="right" />
      <ReactTooltip id="Lessons" place="right" />
      <ReactTooltip id="Settings" place="right" />
    </div>
  );
};

export default Sidebar;
