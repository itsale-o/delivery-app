import Navbar from "../../components/Navbar/Navbar";
import PromocaoSemana from "../../components/PromocaoSemana/PromocaoSemana";
import Footer from "../../components/Footer/Footer";

export default function Home() {
    return (
        <div className="home">
            <Navbar></Navbar>
            <PromocaoSemana></PromocaoSemana>
        </div> 
    )
}