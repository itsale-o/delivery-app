import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./pages/Login/Login";
import Home from "./pages/Home/Home";
import Cardapio from "./components/Cardapio/Cardapio";
import Carrinho from "./components/Carrinho/Carrinho";
import Pedidos from "./components/Pedidos/Pedidos";
import './App.css'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/inicio" element={<Home />} />
        <Route path="/cardapio" element={<Cardapio />} />
        <Route path="/carrinho" element={<Carrinho />} />
        <Route path="/pedidos" element={<Pedidos />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
