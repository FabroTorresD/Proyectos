import { Code, Briefcase, GraduationCap, Heart } from "lucide-react";
import "./AboutMe.css";

const skills = [
  "JavaScript", "Python", "React", "Node.js",
  "Java", "SQL", "CSS", "Ingles", "Git"
];

const AboutMe = () => {
  return (
    <section id="about" className="about-section">
      <div className="container">
        <h2 className="section-title">Sobre Mí</h2>

        <div className="about-grid">
          <div className="about-text">
            <p>
              Soy estudiante avanzado en la carrera de Ingenieria en Sistemas de Informacion.
              Me considero una persona autodidacta, con
              una fuerte orientación al aprendizaje
              continuo y la mejora constante. Me destaco
              por ser responsable, proactivo y capaz de
              adaptarme rápidamente a nuevos entornos y
              desafíos.
            </p>
            <p>
              Cuento con habilidades para el
              trabajo en equipo, así como para la resolución
              de problemas de manera eficiente y creativa.
              Mi compromiso con la calidad y la disciplina
              se refleja en cada proyecto que emprendo
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
              <p>Estudiante avanzado en la carrera de Ingenieria en Sistemas de Informacion, en la Universidad 
                Teconologica Nacional, Facultad Regional Cordoba.
              </p>
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
