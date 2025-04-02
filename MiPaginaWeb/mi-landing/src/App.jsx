import { useState } from 'react'
import './App.css'
import NavBar from './components/Navbar'
import Home from './components/Home'
import AboutMe from './components/AboutMe'
import Proyects from './components/Projects'
import Contact from './components/Contact'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'

function App() {
  return (
    <>
      <NavBar />
      <Routes>
        <Route path='/' element={<Home />} />  
        <Route path='/aboutme' element={<AboutMe/>} />  
        <Route path='/proyects' element={<Proyects />} /> 
        <Route path='/contact' element={<Contact />} /> 
      </Routes>
      </>
  )
}

export default App
