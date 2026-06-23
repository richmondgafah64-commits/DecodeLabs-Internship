import {

  BarChart,

  Bar,

  XAxis,

  YAxis,

  CartesianGrid,

  Tooltip,

  ResponsiveContainer,

} from "recharts";



import { salesData } from "./data/salesData";



function App() {

  return (

    <div

      style={{

        width: "90%",

        height: "500px",

        margin: "40px auto",

      }}

    >

      <h1 style={{ textAlign: "center" }}>Sales Dashboard</h1>



      <ResponsiveContainer width="100%" height="100%">

        <BarChart data={salesData}>

          <CartesianGrid strokeDasharray="3 3" />



          <XAxis dataKey="month" />



          <YAxis />



          <Tooltip />



          <Bar dataKey="sales" fill="#8884d8" />

        </BarChart>

      </ResponsiveContainer>

    </div>

  );

}



export default App;