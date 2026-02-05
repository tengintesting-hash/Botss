import React from "react";

const Earn = () => {
  return (
    <div className="min-h-screen bg-slate-950 text-white p-6">
      <div className="max-w-3xl mx-auto space-y-6">
        <header>
          <h1 className="text-3xl font-bold">Заробіток</h1>
          <p className="text-slate-300">Запрошуйте друзів та отримуйте PRO#.</p>
        </header>

        <div className="rounded-2xl border border-slate-800 bg-slate-900/70 p-5">
          <p className="text-lg">Запрошено друзів: <span className="font-semibold">0</span></p>
          <div className="mt-4 space-y-2 text-slate-300">
            <p>Рівень 1: 1000 PRO#</p>
            <p>Рівень 2: 5000 PRO# за депозит</p>
          </div>
          <button className="mt-6 w-full rounded-xl bg-sky-400 py-3 font-semibold text-slate-950 hover:bg-sky-300 transition">
            Копіювати посилання
          </button>
        </div>
      </div>
    </div>
  );
};

export default Earn;
