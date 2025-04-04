import { Code, Briefcase, GraduationCap, Heart } from "lucide-react";
import "./AboutMe.css";

const skills = [
  "JavaScript", "TypeScript", "React", "Node.js",
  "Express", "MongoDB", "CSS/SCSS", "Tailwind CSS", "Git"
];

const AboutMe = () => {
  return (
    <section id="about" className="about-section">
      <div className="container">
        <h2 className="section-title">Sobre Mí</h2>

        <div className="about-grid">
          <div className="about-text">
            <p>
              Soy un desarrollador apasionado con experiencia en crear aplicaciones web atractivas y funcionales.
              Me encanta resolver problemas complejos y transformar ideas en productos digitales utilizando las tecnologías más modernas.
            </p>
            <p>
              Con más de 5 años de experiencia en el desarrollo web, he trabajado en proyectos de diversos tamaños,
              desde pequeñas páginas web hasta aplicaciones empresariales complejas.
            </p>

            <div className="skills">
              {skills.map((skill) => (
                <span key={skill} className="skill-badge">{skill}</span>
              ))}
            </div>
          </div>

          <div className="about-cards">
            <div className="about-card">
              <div className="icon-wrapper">
                <Code className="icon" size={24} />
              </div>
              <h3>Desarrollo</h3>
              <p>Creo aplicaciones web responsivas y accesibles con las últimas tecnologías.</p>
            </div>

            <div className="about-card">
              <div className="icon-wrapper">
                <Briefcase className="icon" size={24} />
              </div>
              <h3>Experiencia</h3>
              <p>He trabajado en proyectos tanto para startups como para grandes empresas.</p>
            </div>

            <div className="about-card">
              <div className="icon-wrapper">
                <GraduationCap className="icon" size={24} />
              </div>
              <h3>Educación</h3>
              <p>Licenciado en Ciencias de la Computación con formación continua en nuevas tecnologías.</p>
            </div>

            <div className="about-card">
              <div className="icon-wrapper">
                <Heart className="icon" size={24} />
              </div>
              <h3>Pasión</h3>
              <p>Entusiasta de las nuevas tecnologías y el aprendizaje constante.</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default AboutMe;
