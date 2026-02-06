import React from "react";

const Home = () => {
  const offers = [
    {
      id: 1,
      title: "Fortuna Slots",
      reward: "50 000 PRO#",
      limited: true,
    },
    {
      id: 2,
      title: "Vegas Rush",
      reward: "25 000 PRO#",
      limited: true,
    },
  ];

  return (
    <div className="min-h-screen bg-slate-950 text-white p-6">
      <div className="max-w-4xl mx-auto space-y-6">
        <header className="space-y-2">
          <h1 className="text-3xl font-bold">PRO# Hub</h1>
          <p className="text-slate-300">
            Лімітовані пропозиції для швидкого бусту балансу.
          </p>
        </header>

        <div className="grid gap-4 md:grid-cols-2">
          {offers.map((offer) => (
            <div
              key={offer.id}
              className="rounded-2xl border border-slate-800 bg-slate-900/70 p-5 shadow-lg"
            >
              <div className="flex items-center justify-between">
                <h2 className="text-xl font-semibold">{offer.title}</h2>
                {offer.limited && (
                  <span className="rounded-full bg-amber-400/20 px-3 py-1 text-xs text-amber-300">
                    Лімітована пропозиція
                  </span>
                )}
              </div>
              <p className="mt-3 text-slate-300">
                Бонус за депозит: <span className="font-semibold">{offer.reward}</span>
              </p>
              <button className="mt-4 w-full rounded-xl bg-emerald-400 py-3 text-slate-950 font-semibold hover:bg-emerald-300 transition">
                Грати (+50k PRO#)
              </button>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Home;
