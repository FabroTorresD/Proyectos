import { motion } from "framer-motion";
import { FaLaptopCode, FaTabletAlt, FaMobileAlt, FaMicrochip, FaServer } from "react-icons/fa";
import "../styles/Home.css"; // Importamos los estilos



const Home = () => {
  return (
    <div className="home-container">
      {/* Texto principal con efecto neón */}
      <motion.h1
        initial={{ opacity: 0, y: -50 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 1 }}
        className="neon-text"
      >
        WELCOME TO MY WEBSITE
      </motion.h1>

    </div>
  );
};

export default Home;