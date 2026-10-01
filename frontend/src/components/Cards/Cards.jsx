import "./Cards.css";

export default function Cards({ image, imageAlt, title, text, rating=0, price }) {
    return (
        <div className="card p-3 mb-5 rounded">
            <img 
                src={image} 
                className="card-img-top" 
                alt={imageAlt} 
            />
            <div className="card-body">
                <h5 className="card-title">{title}</h5>
                <p className="card-text">{text}</p>
                <div className="precificacao">
                    <div className="avaliacao">
                        {[1, 2, 3, 4, 5].map((star) => {
                            const preenchimento = Math.min(
                                Math.max(rating - star + 1, 0),
                                1
                            );
                            return (
                                <span
                                    key={star}
                                    className="estrela"
                                    style={{"--preenchimento": `${preenchimento * 100}%`}}
                                >
                                    <i className="bi bi-star-fill" />
                                </span>
                            )
                        })}
                    </div>
                    <div className="preco">
                        {price}
                    </div>
                </div>
            </div>
        </div>
    )
}