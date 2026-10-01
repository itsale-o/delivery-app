import { Outlet } from "react-router-dom";
import Navbar from "../../components/Navbar/Navbar";
import Footer from "../../components/Footer/Footer";
import "./Home.css";

export default function HomeLayout() {
    return (
        <div className="layout">
            <Navbar />

            <main>
                <Outlet />
            </main>

            <Footer />
        </div>
    )
}