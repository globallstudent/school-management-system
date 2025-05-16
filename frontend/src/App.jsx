import React from "react";
import Layout from "./components/layout/index";
import { BrowserRouter, Routes, Route, Outlet } from "react-router-dom"; // Outlet ham kerak
import DashboardPage from "./pages/dashboard";
import TeachersPage from "./pages/teachers";
import StudentsPage from "./pages/students";
import ParentsPage from "./pages/parents";
import SubjectsPage from "./pages/subjects";
import LessonsPage from "./pages/lessons";
import ClassesPage from "./pages/classes";
import ExamsPage from "./pages/exams";
import AssignmentsPage from "./pages/assignments";
import ResultsPage from "./pages/results";
import AttendancePage from "./pages/attendance";
import EventsPage from "./pages/events";
import SettingsPage from "./pages/settings";
import LoginPage from "./components/login";

const role = "admin";

const token = localStorage.getItem("token");

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<LoginPage />} />

        {token ? (
          <Route path="/" element={<Layout />}>
            {role === "admin" ? (
              <Route path="admin" element={<Outlet />}>
                <Route path="dashboard" element={<DashboardPage />} />
                <Route path="teachers" element={<TeachersPage />} />
                <Route path="students" element={<StudentsPage />} />
                <Route path="parents" element={<ParentsPage />} />
                <Route path="subjects" element={<SubjectsPage />} />
                <Route path="classes" element={<ClassesPage />} />
                <Route path="lessons" element={<LessonsPage />} />
                <Route path="exams" element={<ExamsPage />} />
                <Route path="assignments" element={<AssignmentsPage />} />
                <Route path="results" element={<ResultsPage />} />
                <Route path="attendance" element={<AttendancePage />} />
                <Route path="events" element={<EventsPage />} />
                <Route path="settings" element={<SettingsPage />} />
              </Route>
            ) : (
              ""
            )}

            {role === "teacher" ? (
              <Route path="teacher" element={<Outlet />}>
                <Route path="teachers" element={<TeachersPage />} />
                <Route path="students" element={<StudentsPage />} />
                <Route path="subjects" element={<SubjectsPage />} />
                <Route path="lessons" element={<LessonsPage />} />
                <Route path="exams" element={<ExamsPage />} />
                <Route path="assignments" element={<AssignmentsPage />} />
                <Route path="results" element={<ResultsPage />} />
                <Route path="attendance" element={<AttendancePage />} />
                <Route path="events" element={<EventsPage />} />
              </Route>
            ) : (
              <Route path="/" element={<LoginPage />} />
            )}
          </Route>
        ) : (
          ""
        )}
      </Routes>
    </BrowserRouter>
  );
};

export default App;
