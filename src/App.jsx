import React, { useState } from "react";
import Admin from "./components/Admin.jsx";
import Earn from "./components/Earn.jsx";
import Home from "./components/Home.jsx";
import Wallet from "./components/Wallet.jsx";

const tabs = [
  { id: "home", label: "Головна" },
  { id: "earn", label: "Заробіток" },
  { id: "wallet", label: "Гаманець" },
  { id: "admin", label: "Адмін" },
];

const App = () => {
  const [activeTab, setActiveTab] = useState("home");

  return (
    <div className="min-h-screen bg-slate-950 text-white">
      <nav className="sticky top-0 z-10 border-b border-slate-800 bg-slate-950/80 backdrop-blur">
        <div className="mx-auto flex max-w-4xl items-center gap-2 p-4">
          {tabs.map((tab) => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={`rounded-full px-4 py-2 text-sm font-semibold transition ${
                activeTab === tab.id
                  ? "bg-emerald-400 text-slate-950"
                  : "bg-slate-900 text-slate-200 hover:bg-slate-800"
              }`}
            >
              {tab.label}
            </button>
          ))}
        </div>
      </nav>

      {activeTab === "home" && <Home />}
      {activeTab === "earn" && <Earn />}
      {activeTab === "wallet" && <Wallet />}
      {activeTab === "admin" && <Admin />}
    </div>
  );
};

export default App;
