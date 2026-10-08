import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./pages/Login/Login";
import CriarConta from "./pages/CriarConta/CriarConta";
import Home from "./pages/Home/Home";
import Cardapio from "./components/Cardapio/Cardapio";
import Carrinho from "./components/Carrinho/Carrinho";
import Pedidos from "./components/Pedidos/Pedidos";
import Layout from "./components/Layout/Layout";
import HomeLayout from "./pages/Home/HomeLayout";
import './App.css'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/criar-conta" element={<CriarConta />} />

        <Route element={<HomeLayout/>}>
          <Route path="/inicio" element={<Home />} />
        </Route>

        <Route element={<Layout />}>
          
          
          <Route path="/cardapio" element={<Cardapio />} />
          <Route path="/carrinho" element={<Carrinho />} />
          <Route path="/pedidos" element={<Pedidos />} />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App
