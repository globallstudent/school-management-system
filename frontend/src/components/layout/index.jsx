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
    <div className="h-screen">
      {/* Header, sidebarning ustida bo'ladi */}
      <Header />
      <div className="flex flex-1 pb-10  ">
        {/* Sidebar */}
        <Sidebar />
        <main
          className={`flex-1  ${
            width < 700 ? "ml-30" : isOpen ? "ml-77" : "ml-30"
          } h-full  transition-all mt-[60px]  p-[20px] duration-300 ease-in-out  overflow-y-auto`}
        >
          <Outlet />
        </main>
      </div>
    </div>
  );
};

export default Layout;
