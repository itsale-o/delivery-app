import "./Navbar.css";

export default function Navbar() {
    return (
        <div className="navbar">
            <div className="titulo">
                <p>O que você está procurando?</p>
                <div className="filtro">
                    <i className="bi bi-funnel" />
                    Filtro
                </div>
            </div>

            <div className="input-group">
                <i className="bi bi-search" />
                <input type="text" placeholder="Pesquise sua comida favorita..." />
            </div>
        </div>
    )
}