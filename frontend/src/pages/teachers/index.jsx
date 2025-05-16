import React, { useState } from "react";
import axios from "axios";
import { Helmet } from "react-helmet-async";

const TeachersPage = () => {
  const [imageUrl, setImageUrl] = useState(""); // Tasvir URL
  const [fullName, setFullName] = useState("");
  const [positionDe, setPositionDe] = useState("");
  const [positionRu, setPositionRu] = useState("");
  const [positionEn, setPositionEn] = useState("");

  // Tasvir URL o'zgartirish
  const handleImageChange = (e) => {
    const file = e.target.files[0];
    // Faylni serverga yuklash va URL olish
    // Agar siz faylni URL sifatida yubormoqchi bo'lsangiz,
    // faylni serverga yuklab, olingan URLni setImageUrl ga saqlang
    const imageUrl = "https://example.com/" + file.name; // Bu faqat misol
    setImageUrl(imageUrl);
  };

  // Yuborish
  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!imageUrl) {
      alert("Iltimos, tasvirni yuklang!");
      return;
    }

    try {
      const payload = {
        image: imageUrl,
        full_name: fullName,
        position_de: positionDe,
        position_ru: positionRu,
        position_en: positionEn,
      };

      const token = localStorage.getItem("token");

      const response = await axios.post(
        "https://example.com/api/team-member", // Bu sizning API endpointingiz
        payload,
        {
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
          },
        }
      );

      console.log("Success:", response.data);
      alert("Jamoa a'zosi muvaffaqiyatli yaratildi!");
    } catch (error) {
      console.error("Xatolik:", error.response?.data || error.message);
      alert("Yuborishda xatolik yuz berdi.");
    }
  };

  return (
    <>
      <Helmet>
        <title>CRM - Mijozlar</title>
        <meta name="description" content="CRM tizimida mijozlar ro'yxati" />

        <meta property="og:title" content="CRM - Mijozlar" />
        <meta
          property="og:description"
          content="CRM tizimida mijozlar ro'yxati"
        />
        <link rel="icon" type="image/svg+xml" sizes="64x64" href="/announcement.png" />
        <meta property="og:image" content="/login-icon.svg" />
        <meta property="og:type" content="website" />
        <meta property="og:url" content="https://yourdomain.com/mijozlar" />

        <meta name="twitter:card" content="summary_large_image" />
      </Helmet>

      <form onSubmit={handleSubmit} className="p-6 flex flex-col gap-4">
        <div className="grid grid-cols-2 gap-4">
          <input
            type="text"
            placeholder="Full Name"
            value={fullName}
            onChange={(e) => setFullName(e.target.value)}
          />
          <input
            type="text"
            placeholder="Position (DE)"
            value={positionDe}
            onChange={(e) => setPositionDe(e.target.value)}
          />
          <input
            type="text"
            placeholder="Position (RU)"
            value={positionRu}
            onChange={(e) => setPositionRu(e.target.value)}
          />
          <input
            type="text"
            placeholder="Position (EN)"
            value={positionEn}
            onChange={(e) => setPositionEn(e.target.value)}
          />
          <input type="file" accept="image/*" onChange={handleImageChange} />
        </div>

        <button
          type="submit"
          className="bg-blue-600 text-white px-4 py-2 rounded"
        >
          Yaratish
        </button>
      </form>
    </>
  );
};

export default TeachersPage;
