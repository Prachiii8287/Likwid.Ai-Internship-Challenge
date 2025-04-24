
import React, { useEffect, useState } from "react";
import axios from "axios";

function Dashboard() {
  const [data, setData] = useState(null);

  useEffect(() => {
    axios.get("http://127.0.0.1:5000/dashboard").then((res) => {
      setData(res.data);
    });
  }, []);

  return (
    <div className="mt-8">
      <h2 className="text-xl font-semibold text-gray-700 mb-2">Dashboard Data</h2>
      {data ? (
        <pre className="bg-gray-100 p-4 rounded shadow max-h-80 overflow-y-auto text-left text-sm text-gray-800">
          {JSON.stringify(data, null, 2)}
        </pre>
      ) : (
        <p className="text-gray-500">Loading...</p>
      )}
    </div>
  );
}

export default Dashboard;
