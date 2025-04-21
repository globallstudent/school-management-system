import React, { useState } from "react";
import Layout from "./components/layout/index";
import { BrowserRouter, Routes, Route } from "react-router-dom"; // Route import qilishni unutmang
import DashboardPage from "./pages/dashboard";
import TeachersPage from "./pages/teachers";
import StudentsPage from "./pages/students";
import ParentsPage from "./pages/parents";

const App = () => {
  return (
    <BrowserRouter>
      {" "}
      {/* To'g'ri nomlash */}
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route path={"dashboard"} element={<DashboardPage />} />
          <Route path={"teachers"} element={<TeachersPage />} />
          <Route path={"students"} element={<StudentsPage />} />
          <Route path={"parents"} element={<ParentsPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
};

export default App;
