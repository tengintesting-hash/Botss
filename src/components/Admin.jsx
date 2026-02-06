import React from "react";

const Admin = () => {
  const endpoints = [
    { id: 1, title: "Користувачі", path: "/admin/users" },
    { id: 2, title: "Оффери", path: "/admin/offers" },
    { id: 3, title: "Канали", path: "/admin/channels" },
    { id: 4, title: "Транзакції", path: "/admin/transactions" },
  ];

  return (
    <div className="min-h-screen bg-slate-950 text-white p-6">
      <div className="max-w-4xl mx-auto space-y-6">
        <header className="space-y-2">
          <h1 className="text-3xl font-bold">Адмін-панель</h1>
          <p className="text-slate-300">
            Використовуйте токен адміністратора у заголовку <span className="font-semibold">X-Admin-Token</span>.
          </p>
        </header>

        <div className="grid gap-4 md:grid-cols-2">
          {endpoints.map((endpoint) => (
            <div
              key={endpoint.id}
              className="rounded-2xl border border-slate-800 bg-slate-900/70 p-5"
            >
              <h2 className="text-xl font-semibold">{endpoint.title}</h2>
              <p className="mt-2 text-slate-300">API: {endpoint.path}</p>
              <button className="mt-4 w-full rounded-xl bg-amber-400 py-3 text-slate-950 font-semibold hover:bg-amber-300 transition">
                Відкрити список
              </button>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Admin;
