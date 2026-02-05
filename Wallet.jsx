import React from "react";

const Wallet = () => {
  const balancePro = 125000;
  const usdRate = 0.00002;
  const balanceUsd = (balancePro * usdRate).toFixed(2);

  return (
    <div className="min-h-screen bg-slate-950 text-white p-6">
      <div className="max-w-3xl mx-auto space-y-6">
        <header>
          <h1 className="text-3xl font-bold">Гаманець</h1>
          <p className="text-slate-300">Ваші накопичення PRO#.</p>
        </header>

        <div className="rounded-2xl border border-slate-800 bg-slate-900/70 p-6">
          <div className="space-y-2">
            <p className="text-sm uppercase text-slate-400">Баланс</p>
            <p className="text-3xl font-semibold">{balancePro.toLocaleString()} PRO#</p>
            <p className="text-slate-300">≈ ${balanceUsd}</p>
          </div>
          <button className="mt-6 w-full rounded-xl bg-purple-400 py-3 font-semibold text-slate-950 hover:bg-purple-300 transition">
            Вивести кошти
          </button>
        </div>
      </div>
    </div>
  );
};

export default Wallet;
