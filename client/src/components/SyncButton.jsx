
// import React from "react";
// import axios from "axios";

// function SyncButton() {
//   const handleSync = async () => {
//     try {
//       await axios.get("http://localhost:5000/sync");
//       alert("Synced from Google Sheet!");
//     } catch (error) {
//       console.error("Sync failed:", error);
//       alert("Failed to sync from Google Sheet.");
//     }
//   };

//   return (
//     <button
//       onClick={handleSync}
//       className="mt-4 px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600"
//     >
//       🔄 Sync from Google Sheet
//     </button>
//   );
// }

// export default SyncButton;

////2
import React from "react";
import axios from "axios";

function SyncButton() {
  const handleSync = async () => {
    try {
      await axios.get("http://localhost:5000/sync");
      alert("Synced from Google Sheet!");
    } catch (error) {
      console.error("Sync failed:", error);
      alert("Failed to sync from Google Sheet.");
    }
  };

  return (
    <button
      onClick={handleSync}
      className="mt-2 px-4 py-2 bg-green-600 text-white rounded hover:bg-green-700"
    >
      🔄 Sync from Google Sheet
    </button>
  );
}

export default SyncButton;
