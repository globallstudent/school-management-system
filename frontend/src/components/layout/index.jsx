import { Outlet } from "react-router-dom";
import Header from "../header";
import Sidebar from "../sidebar";
import useLayoutStore from './../../store/layout-control/index';
import { useEffect, useState } from 'react';

const Layout = () => {
  const { isOpen , setIsOpen } = useLayoutStore();
      const [width, setWidth] = useState(window.innerWidth);

      useEffect(() => {
        const handleResize = () => {
          if (width < 700) {
            setIsOpen(false);
          }
        };

        window.addEventListener("resize", handleResize);

        return () => {
          window.removeEventListener("resize", handleResize);
        };
      }, [window.innerWidth]);

  return (
    <div className="h-[100%]">
      {/* Header, sidebarning ustida bo'ladi */}
      <Header />
      <div className="flex h-[100%]  flex-1 pb-4 pt-[65px] ">
        {/* Sidebar */}
        <Sidebar />
        <main
          className={`flex flex-1 w-full rounded-[25px] bg-blue-100 overflow-auto scrollbar-thin scrollbar-thumb-rounded scrollbar-thumb-gray-500 scroll-container mr-[20px]  ${
            width < 700 ? "ml-30" : isOpen ? "ml-67" : "ml-30"
          }  transition-all mt-[20px]  p-[20px] duration-300 ease-in-out`}
        >
          <div className=" h-full w-full ">
            <Outlet />
          </div>
        </main>
      </div>
    </div>
  );
};

export default Layout;
