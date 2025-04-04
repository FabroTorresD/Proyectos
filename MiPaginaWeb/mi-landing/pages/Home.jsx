import "../styles/home.style.css";
import { Link } from "react-router-dom"; // Si querés usar navegación interna
import { ArrowDown } from "lucide-react";


const Home = () => {
  return (
    <section id="home" className="home-container">
      <div className="gradient-overlay"></div>
      <div className="content-wrapper">
        <div className="text-center">
          <h1 className="title">
            <span className="highlight">Hola</span>, soy
            <div className="name">Fabrizio Torres Daniele</div>
          </h1>
          <p className="subtitle">
            Desarrollador Full Stack & Diseñador UI/UX
          </p>
          <div className="button-group">
            <Link to="/proyects" className="btn primary">Ver Proyectos</Link>
            <Link to="/contact" className="btn outline">Contactarme</Link>
          </div>
        </div>
        <div className="scroll-down">
          <a href="#about" aria-label="Scroll to About section">
            <ArrowDown size={32} className="arrow-icon" />
          </a>
        </div>
      </div>
    </section>
  );
};

export default Home;
