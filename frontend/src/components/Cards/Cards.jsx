import "./Cards.css";

export default function Cards({ image, imageAlt, title, text, rating=5, price }) {
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
                        {[...Array(rating)].map((_, index) => (
                            <i
                                key={index}
                                className="bi bi-star-fill"
                            />
                        ))}
                    </div>
                    <div className="preco">
                        {price}
                    </div>
                </div>
            </div>
        </div>
    )
}