// import FileUpload from "./components/FileUpload";
// import Dashboard from "./components/Dashboard";
// import SyncButton from "./components/SyncButton";

// function App() {
//   return (
//     <div className="min-h-screen bg-gray-100 p-6 text-center">
//       <h1 className="text-3xl font-bold mb-6">📊 MSME Data Dashboard</h1>
//       <FileUpload />
//       <SyncButton />
//       <Dashboard />
//     </div>
//   );
// }

// export default App;

/////2
import FileUpload from "./components/FileUpload";
import Dashboard from "./components/Dashboard";
import SyncButton from "./components/SyncButton";

function App() {
  return (
    <div className="min-h-screen bg-gray-50 flex items-center justify-center p-6">
      <div className="w-full max-w-3xl bg-white rounded-2xl shadow-lg p-8">
        <h1 className="text-3xl font-bold text-center mb-6 text-gray-800">
          📊  Data Dashboard
        </h1>
        <div className="flex flex-col items-center space-y-4">
          <FileUpload />
          <SyncButton />
        </div>
        <Dashboard />
      </div>
    </div>
  );
}

export default App;
