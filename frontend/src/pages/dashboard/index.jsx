import React from "react";
import { Suspense } from "react";

const CountChart = React.lazy(() =>
  import("./../../components/count-chart/index")
);

const UserCard = React.lazy(() => import("./../../components/user-card/index"));

const AttendanceChart = React.lazy(() =>
  import("../../components/attendance-chart/index")
);

const FinanceChart = React.lazy(() =>
  import("./../../components/finance-chart/index")
);

const EventCalendar = React.lazy(() =>
  import("./../../components/events/index")
);

const Announcement = React.lazy(() =>
  import("./../../components/announcements")
);

import { Helmet } from "react-helmet-async";

const userStats = [
  { type: "O'QUVCHILAR", count: 308, malePercent: 61, femalePercent: 39 },
  { type: "O'QITUVCHILAR", count: 50, malePercent: 40, femalePercent: 60 },
  { type: "OTA-ONALAR", count: 50, malePercent: 40, femalePercent: 60 },
  { type: "XODIMLAR", count: 80, malePercent: 45, femalePercent: 55 },
];

const DashboardPage = () => {
  return (
    <>
      <Helmet>
        <title>Statistic Malumotlar</title>
        <meta name="description" content="CRM tizimida mijozlar ro'yxati" />
        <meta property="og:title" content="Statistik malumotlar" />
        <meta
          property="og:description"
          content="CRM tizimida mijozlar ro'yxati"
        />
        <link
          rel="icon"
          type="image/svg+xml"
          sizes="64x64"
          href="/announcement.png"
        />
        <meta property="og:image" content="/login-icon.svg" />
        <meta property="og:type" content="website" />
        <meta property="og:url" content="https://yourdomain.com/mijozlar" />

        <meta name="twitter:card" content="summary_large_image" />
      </Helmet>
      <div className="flex gap-4 flex-col md:flex-row">
        {/*Left */}
        <div className="w-full lg:w-2/3 flex flex-col gap-8">
          <div className="flex gap-4 justify-between flex-wrap lg:grid lg:grid-cols-2 xl:grid-cols-4">
            {userStats.map((item, idx) => (
              <Suspense fallback={<p>Yuklanmoqda ...</p>}>
                <UserCard
                  key={idx}
                  type={item.type}
                  count={item.count}
                  malePercent={item.malePercent}
                  femalePercent={item.femalePercent}
                />
              </Suspense>
            ))}
          </div>
          {/*Middle chart */}
          <div className="flex gap-4 flex-col lg:flex-row">
            {/*Count  chart */}
            <div className="w-full lg:w-1/3 h-[450px]">
              <Suspense fallback={<p>Yuklanmoqda ...</p>}>
                <CountChart />
              </Suspense>
            </div>
            {/*Attendance chart */}
            <div className="w-full lg:w-2/3 h-[450px]">
              <Suspense fallback={<p>Yuklanmoqda ...</p>}>
                <AttendanceChart />
              </Suspense>
            </div>
          </div>
          {/*Bottom chart */}
          <div className="w-full h-[500px]">
            <Suspense fallback={<p>Yuklanmoqda ...</p>}>
              <FinanceChart />
            </Suspense>
          </div>
        </div>

        {/*Right */}
        <div className="w-full lg:w-1/3 flex flex-col gap-8">
          <Suspense fallback={<p>Yuklanmoqda ...</p>}>
            <EventCalendar />
          </Suspense>
          <Suspense fallback={<p>Yuklanmoqda ...</p>}>
            <Announcement />
          </Suspense>
        </div>
      </div>
    </>
  );
};

export default DashboardPage;
