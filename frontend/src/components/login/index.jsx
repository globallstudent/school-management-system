import axios from "axios";
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { toast } from "react-toastify";

const LoginPage = () => {
  const [login, setLogin] = useState("");
  const [password, setPassword] = useState("");
  const [confirm_password, setConfirm_password] = useState("");

  const payload = {
    login,
    password,
  };

  console.log(payload);

  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post(
        "https://testaoron.limsa.uz/api/auth/login",
        payload
      );
      localStorage.setItem("token", res?.data?.data?.access_token);
      navigate("/admin/dashboard");
      toast.success("Sitega muvaffaqiyatli kirdiz");
    } catch (error) {
      console.log(error);
      toast.success(error);
    } finally {
    }
  };

  handleSubmit();

  return (
    <div className="min-h-screen bg-gradient-to-r from-[#e3eafc] via-white to-[#d8e2f7] flex items-center justify-center px-4">
      <div className="w-full max-w-4xl bg-white shadow-2xl rounded-2xl overflow-hidden flex flex-col md:flex-row animate-fade-in">
        {/* Left - Image */}
        <div className="md:w-1/2 hidden md:block">
          <img
            src="/public/logo-1.jpg"
            alt="Harvard"
            className="h-full w-full object-cover"
          />
        </div>

        {/* Right - Form */}
        <div className="w-full md:w-1/2 p-10">
          <h2 className="text-3xl font-extrabold text-center text-[#093f9f] mb-6">
            Harvard School Login
          </h2>
          <form onSubmit={handleSubmit} className="space-y-5">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Login
              </label>
              <input
                onChange={(e) => setLogin(e?.target?.value)}
                type="text"
                value={login}
                placeholder="Enter your login"
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#093f9f] transition"
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Password
              </label>
              <input
                value={password}
                onChange={(e) => setPassword(e?.target?.value)}
                type="password"
                placeholder="Enter your password"
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#093f9f] transition"
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Confirm Password
              </label>
              <input
                value={confirm_password}
                onChange={(e) => setConfirm_password(e?.target?.value)}
                type="password"
                placeholder="Confirm your password"
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#093f9f] transition"
              />
            </div>
            <button
              type="submit"
              className="w-full cursor-pointer bg-[#093f9f] hover:bg-blue-900 text-white py-2 rounded-lg font-semibold transition duration-300"
            >
              Login
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;
