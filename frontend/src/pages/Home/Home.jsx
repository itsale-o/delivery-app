import PromocaoSemana from "../../components/PromocaoSemana/PromocaoSemana";
import Cards from "../../components/Cards/Cards";

export default function Home() {
    const produtos = [
        {
            id: 1,
            image: "/src/assets/pizza.jpg",
            imageAlt: "Pizza Crocante",
            title: "Pizza Crocante",
            text: "Joe's Pizza",
            rating: 5,
            price: "R$ 49,00"
        },
        {
            id: 2,
            image: "/src/assets/mexicana.jpg",
            imageAlt: "Comida Mexicana",
            title: "Comida Mexicana",
            text: "Mexican Gourmet",
            rating: 4,
            price: "R$ 60,00"
        },
        {
            id: 3,
            image: "/src/assets/cafe.jpg",
            imageAlt: "Café Completo",
            title: "Café Completo",
            text: "Caffè Italiano",
            rating: 5,
            price: "R$ 25,00"
        },
        {
            id: 4,
            image: "/src/assets/pastel.jfif",
            imageAlt: "Legítimo Pastel",
            title: "Legítimo Pastel",
            text: "Pastel do Léo",
            rating: 4.5,
            price: "R$ 8,00"
        },
        {
            id: 5,
            image: "/src/assets/cheesecake.jfif",
            imageAlt: "Sobremesas Deliciosas",
            title: "Sobremesas Deliciosas",
            text: "Confeitaria da Bê",
            rating: 4,
            price: "R$ 25,00"
        },
        {
            id: 6,
            image: "/src/assets/japonesa.jfif",
            imageAlt: "Comida Japonesa",
            title: "Comida Japonesa",
            text: "Ping's Sushi",
            rating: 3,
            price: "R$ 49,00"
        }
    ]

    return (
        <div className="home">
            <PromocaoSemana></PromocaoSemana>

            <div className="cards">
                {produtos.map((produto) => (
                    <Cards
                        key={produto.id}
                        {...produto}
                    />
                ))}
                
            </div>
        </div> 
    )
}