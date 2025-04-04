import { useEffect, useState } from 'react';
import { NavLink } from 'react-router-dom';
import './NavBar.css'; // para agregar estilos personalizados si quieres

const NavBar = () => {
  const [isScrolled, setIsScrolled] = useState(true);

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 50);
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <nav
      className={`navbar navbar-expand-sm navbar-dark fixed-top w-100 transition-navbar ${
        isScrolled ? 'bg-dark shadow-sm backdrop-blur' : 'bg-transparent'
      }`}
    >
      <div className="container-fluid">
        <NavLink className="navbar-brand" >Portfolio</NavLink>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#collapsibleNavbar">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="collapsibleNavbar">
          <ul className="navbar-nav ms-auto">
            <li className="nav-item">
              <NavLink className="nav-link" to="/home">Home</NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="nav-link" to="/aboutme">About me</NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="nav-link" to="/proyects">Projects</NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="nav-link" to="/contact">Contact</NavLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default NavBar;
